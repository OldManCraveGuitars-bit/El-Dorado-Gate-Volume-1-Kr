"""Standalone v0.75 patch installer; never edits a selected original image."""
from pathlib import Path
import argparse
import hashlib
import json
import os
import queue
import shlex
import shutil
import subprocess
import sys
import threading


def digest(path):
    with Path(path).open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def resource(name):
    base = Path(getattr(sys, '_MEIPASS', Path(__file__).resolve().parent))
    return base / name


def external_base():
    return Path(sys.executable).parent if getattr(sys, 'frozen', False) else Path(__file__).resolve().parent


def read_manifest():
    return json.loads(resource('hashes.json').read_text('utf-8-sig'))


def original_tracks(gdi):
    gdi = Path(gdi).resolve(strict=True)
    lines = gdi.read_text('utf-8-sig').splitlines()
    if len(lines) != 4 or lines[0].strip() != '3':
        raise ValueError('지원하는 원본은 3트랙 GDI입니다.')
    tracks = {}
    expected = [(1, 0, 4, 2352, 0), (2, 450, 0, 2352, 0), (3, 45000, 4, 2352, 0)]
    for line, layout in zip(lines[1:], expected):
        fields = shlex.split(line)
        if len(fields) != 6:
            raise ValueError('GDI 트랙 정보가 올바르지 않습니다.')
        actual = tuple(int(fields[n]) for n in (0, 1, 2, 3, 5))
        if actual != layout:
            raise ValueError('원본 GDI의 트랙 구성이 지원 대상과 다릅니다.')
        filename = fields[4]
        if Path(filename).name != filename or '/' in filename or '\\' in filename or ':' in filename:
            raise ValueError('GDI 트랙 파일은 GDI와 같은 폴더에 있어야 합니다.')
        track = (gdi.parent / filename).resolve(strict=True)
        if track.parent != gdi.parent:
            raise ValueError('GDI 폴더 밖의 트랙은 사용할 수 없습니다.')
        tracks[f'track{layout[0]:02}.bin' if layout[0] != 2 else 'track02.raw'] = track
    return gdi, tracks


def apply(gdi, output, patch=None, notify=lambda message: None):
    manifest = read_manifest()
    output = Path(output).resolve()
    if output.exists():
        raise ValueError('출력 폴더가 이미 있습니다. 새 폴더 이름을 선택하세요.')
    gdi, tracks = original_tracks(gdi)
    notify('원본 3개 트랙의 크기와 SHA-256 확인 중…')
    for name, path in tracks.items():
        row = manifest['tracks'][name]
        if path.stat().st_size != row['bytes'] or digest(path) != row['before_sha256']:
            raise ValueError(f'{name} 원본 해시가 다릅니다. 일본판 Vol.1 v1.002 원본을 선택하세요.')
    patch = Path(patch or external_base() / manifest['patch']['file']).resolve(strict=True)
    if digest(patch) != manifest['patch']['sha256']:
        raise ValueError('패치 파일 해시가 다릅니다. 릴리스 ZIP을 다시 압축 해제하세요.')
    engine = resource('xdelta3.exe')
    if digest(engine) != manifest['xdelta']['sha256']:
        raise ValueError('패치 엔진 해시가 다릅니다.')
    output.parent.mkdir(parents=True, exist_ok=True)
    output.mkdir()  # Atomic refusal if another process created it meanwhile.
    created = []
    try:
        target = output / 'track03.bin'
        created.append(target)
        notify('한글화와 보너스 아이템 언락 적용 중…')
        env = dict(os.environ)
        env.pop('XDELTA', None)
        result = subprocess.run([str(engine), '-d', '-D', '-R', '-s', str(tracks['track03.bin']), str(patch), str(target)],
                                capture_output=True, env=env,
                                creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0)
        if result.returncode:
            raise RuntimeError('xdelta 적용에 실패했습니다. 원본과 출력 경로의 디스크 공간을 확인하세요.')
        notify('패치 적용 후 SHA-256 확인 중…')
        row = manifest['tracks']['track03.bin']
        if target.stat().st_size != row['bytes'] or digest(target) != row['after_sha256']:
            raise RuntimeError('패치 적용 결과가 검증된 한글판 해시와 다릅니다.')
        for name in ('track01.bin', 'track02.raw'):
            target = output / name
            created.append(target)
            shutil.copyfile(tracks[name], target)
            if digest(target) != manifest['tracks'][name]['after_sha256']:
                raise RuntimeError(f'{name} 복사 후 해시가 다릅니다.')
        target = output / manifest['output_gdi']
        created.append(target)
        target.write_bytes(manifest['gdi_contents'].encode('ascii'))
        if digest(target) != manifest['gdi_sha256']:
            raise RuntimeError('출력 GDI 해시가 다릅니다.')
        receipt = dict(version=manifest['version'], source_gdi=gdi.name,
                       output_gdi=target.name, original_files_modified=False,
                       all_output_hashes_verified=True, bonus_items_unlocked=5,
                       tracks=manifest['tracks'])
        target = output / 'patch-result.json'
        created.append(target)
        target.write_text(json.dumps(receipt, ensure_ascii=False, indent=2)+'\n', 'utf8')
        notify('완료: 새 폴더의 GDI를 실행하세요.')
        return receipt
    except Exception:
        # Only files created by this invocation in its newly created directory.
        for target in reversed(created):
            assert target.resolve().parent == output
            target.unlink(missing_ok=True)
        output.rmdir()
        raise


def gui(smoke_result=None):
    import tkinter as tk
    from tkinter import filedialog, messagebox, ttk
    manifest = read_manifest()
    root = tk.Tk()
    root.title('엘도라도 게이트 Vol.1 한글 패치 v0.75')
    root.geometry('700x480')
    root.resizable(False, False)
    panel = ttk.Frame(root, padding=20)
    panel.pack(fill='both', expand=True)
    ttk.Label(panel, text='엘도라도 게이트 Vol.1 · 한글 패치 v0.75', font=('맑은 고딕', 17, 'bold')).pack(anchor='w')
    ttk.Label(panel, text='대사 · UI · 오프닝 자막 + 보너스 장신구 5종 언락', font=('맑은 고딕', 11)).pack(anchor='w', pady=(8,14))
    source = tk.StringVar()
    destination = tk.StringVar()
    source_row = ttk.Frame(panel); source_row.pack(fill='x', pady=4)
    ttk.Label(source_row, text='원본 GDI', width=12).pack(side='left')
    ttk.Entry(source_row, textvariable=source, width=60).pack(side='left', fill='x', expand=True)
    def choose_source():
        filename = filedialog.askopenfilename(parent=root, title='일본판 Vol.1 v1.002 원본 GDI 선택', filetypes=[('GDI 이미지','*.gdi')])
        if filename:
            source.set(filename)
            if not destination.get():
                destination.set(str(Path(filename).parent.parent/'El-Dorado-Gate-Volume-1-Kr-v0.75'))
    ttk.Button(source_row, text='선택', command=choose_source).pack(side='left', padx=(7,0))
    output_row = ttk.Frame(panel); output_row.pack(fill='x', pady=4)
    ttk.Label(output_row, text='새 출력 폴더', width=12).pack(side='left')
    ttk.Entry(output_row, textvariable=destination, width=60).pack(side='left', fill='x', expand=True)
    def choose_output():
        folder = filedialog.askdirectory(parent=root, title='새 출력 폴더를 만들 위치 선택')
        if folder: destination.set(str(Path(folder)/'El-Dorado-Gate-Volume-1-Kr-v0.75'))
    ttk.Button(output_row, text='선택', command=choose_output).pack(side='left', padx=(7,0))
    ttk.Label(panel, text='일본판 v1.002 원본 3트랙 GDI에 적용합니다.\n원본·결과 해시를 검사하고, 결과는 새 폴더에 만듭니다.\n전체 플레이 검증은 아직 완료되지 않았습니다.', font=('맑은 고딕',10)).pack(anchor='w', pady=(15,9))
    messages = queue.Queue()
    status = tk.StringVar(value='원본 GDI와 새 출력 폴더를 선택하세요.')
    ttk.Label(panel, textvariable=status, wraplength=650).pack(anchor='w', pady=8)
    bar = ttk.Progressbar(panel, mode='indeterminate'); bar.pack(fill='x', pady=4)
    running = [False]
    def begin():
        if running[0]: return
        if not source.get() or not destination.get():
            messagebox.showerror('경로 확인', '원본 GDI와 새 출력 폴더를 선택하세요.', parent=root); return
        selected_source, selected_output = source.get(), destination.get()
        running[0] = True; button.configure(state='disabled'); bar.start()
        def worker():
            try:
                receipt = apply(selected_source, selected_output, notify=lambda text:messages.put(('status', text)))
                messages.put(('done', receipt))
            except Exception as error: messages.put(('error', str(error)))
        threading.Thread(target=worker, daemon=True).start()
    button = ttk.Button(panel, text='한글 패치 적용', command=begin); button.pack(anchor='e', pady=(7,0))
    def poll():
        while not messages.empty():
            kind, value = messages.get()
            if kind == 'status': status.set(value)
            else:
                running[0] = False; button.configure(state='normal'); bar.stop()
                if kind == 'done':
                    status.set('완료: 새 폴더의 GDI를 실행하세요.')
                    messagebox.showinfo('패치 완료', '한글화와 보너스 장신구 5종 언락 적용을 확인했습니다.\n새 폴더의 GDI를 실행하세요.', parent=root)
                else:
                    status.set('패치를 적용하지 못했습니다.')
                    messagebox.showerror('패치 실패', value, parent=root)
        root.after(100, poll)
    def close():
        if running[0]:
            messagebox.showinfo('패치 적용 중', '패치 적용이 끝난 후 창을 닫으세요.', parent=root)
        else: root.destroy()
    root.protocol('WM_DELETE_WINDOW', close)
    if smoke_result:
        root.update_idletasks(); root.update()
        assert root.winfo_width() == 700 and root.winfo_height() == 480
        assert button.cget('text') == '한글 패치 적용'
        assert manifest['version'] == 'v0.75' and manifest['bonus_items']['count'] == 5
        Path(smoke_result).write_text(json.dumps(dict(success=True, version=manifest['version'],
            gui_created=True, embedded_manifest_loaded=True, original_files_modified=False)), 'utf8')
        root.destroy()
    else:
        root.after(100, poll); root.mainloop()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--apply', type=Path)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--patch', type=Path)
    parser.add_argument('--result', type=Path)
    parser.add_argument('--smoke-test', type=Path)
    args = parser.parse_args()
    try:
        if args.smoke_test:
            gui(args.smoke_test)
        elif args.apply:
            if not args.output: parser.error('--output is required')
            result = apply(args.apply, args.output, args.patch)
            if args.result: args.result.write_text(json.dumps(dict(success=True, result=result),ensure_ascii=False,indent=2), 'utf8')
        else: gui()
    except Exception as error:
        if args.result: args.result.write_text(json.dumps(dict(success=False,error=str(error)),ensure_ascii=False), 'utf8')
        else: print(str(error), file=sys.stderr)
        raise SystemExit(1)


if __name__ == '__main__':
    main()

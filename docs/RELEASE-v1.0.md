# 엘도라도 게이트 Vol.1 · 비공식 한글판 v1.0

드림캐스트 **엘도라도 게이트 Vol.1 일본판 v1.002**에 적용하는 비공식 한글 패치입니다.
대사와 메뉴, 아이템·마법 이름, 저장 제목, 시나리오 제목 이미지, 오프닝 자막과 엔딩 크레딧을 한글화했습니다.
원작 로고와 화면 디자인을 살리고, 플레이 중 제보된 글씨 넘침·숫자·기호 정렬 문제를 반영했습니다.

**한글화: 기타 깎는 노인** · 공개 버전 **v1.0** · 기준 게임 빌드 **1.7.13** · 배포일 **2026년 10월 28일**

[**v1.0 다운로드**](https://github.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-1-Kr/releases/tag/v1.0) · [오류 제보](https://github.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-1-Kr/issues) · [상세 해시](https://github.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-1-Kr/blob/v1.0/docs/HASHES.md)

![한글 타이틀 화면](https://raw.githubusercontent.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-1-Kr/v1.0/screenshots/title.png)

타이틀·대사·설정·저장 화면은 앞서 촬영한 에뮬레이터 캡처입니다. 촬영 버전과 시험 조건은 아래에 표시했습니다.
**전체 정상 플레이와 실기 검증은 완료되지 않았습니다.** v1.0은 지금까지의 수정 사항을 묶은 배포 버전입니다.

## 다운로드와 적용 방법

1. [v1.0 릴리스](https://github.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-1-Kr/releases/tag/v1.0)의 **`El-Dorado-Gate-Volume-1-Kr-v1.0.zip`**을 받습니다.
2. ZIP **전체를 압축 해제**합니다. 패처 EXE와 `track03-v1.0.xdelta`를 같은 폴더에 둡니다.
3. **`El-Dorado-Gate-Volume-1-Kr-v1.0-Patcher.exe`**를 실행합니다.
4. **일본판 v1.002 원본 GDI**를 선택하고, 결과를 만들 **새 출력 폴더**를 지정합니다.
5. **한글 패치 적용**을 누르고 완료 메시지를 기다립니다.
6. 결과 폴더의 **`DC-El-Dorado-Gate-Volume-1.gdi`**를 에뮬레이터에서 실행합니다.

Windows 64비트용이며 Python을 따로 설치할 필요가 없습니다. 결과를 만들 여유 공간은 약 1.2GB 이상 필요합니다.
패처는 원본 3개 트랙과 패치 파일의 SHA-256을 확인하고, 적용 후 결과도 다시 검사합니다.
원본 파일은 읽기만 하며, 이미 있는 출력 폴더에는 덮어쓰지 않습니다.

### 지원하는 원본

`Eldorado Gate Vol. 1 v1.002 (2000)(Capcom)(NTSC)(JP)[!]`

원본 GDI와 `track01.bin`, `track02.raw`, `track03.bin`을 준비하세요.
GDI와 트랙들은 같은 폴더에 있어야 합니다. 적용 후에도 생성된 GDI와 세 트랙을 함께 보관하세요.
**이전 한글판에 덧씌우지 말고, 일본판 원본에 새로 적용하세요.** CHD·CDI는 이 패처의 직접 입력 형식이 아닙니다.
원본 해시가 다르다는 메시지가 나오면 [지원 원본 해시](https://github.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-1-Kr/blob/v1.0/docs/HASHES.md)를 확인하세요.

배포물은 차이 패치와 Windows 적용 도구입니다. 원본/완성 ROM, BIOS, VMU 저장 파일은 포함하지 않습니다.

## 한글화 범위

| 구분 | 적용 내용 |
| --- | --- |
| 대사·시스템 | 시나리오 대사, 안내·확인 메시지, 전투·필드 아이템/돈 획득 문구 |
| 메뉴·UI | 타이틀, 설정, 상점, 합성, 장비, 저장/불러오기 등 |
| 이름·설명 | 아이템명 레코드 10,941개, 적 이름 44개, 마법·효과 설명 |
| 저장 정보 | 제목 한글화, `제 1 권 제 1 화 [제목]` 표기와 숫자 위치 |
| 이미지 | 원작 디자인을 반영한 한글 로고, 지역 이름, 시나리오 제목, 관련 UI |
| 오프닝 | 화면 문구 16구간과 확인된 노랫말 9구간의 한글 자막 |
| 엔딩 | 3개 크레딧 리소스의 총 66개 페이지, 역할·이름 및 마지막 한글화 표기 |
| 내장 웹 메뉴 | 관련 안내·메뉴 한글화. 게임 진행을 위한 인터넷 접속은 필요하지 않음 |
| 보너스 | Vol.1 디스크에 들어 있는 보너스 장신구 5종의 오프라인 상점 언락 |

추출 목록 **16,319개 중 16,188개를 번역**했습니다. 나머지 131개는 원본 유지 또는 비언어 데이터입니다.
이 수치는 추출 목록 기준이며, 모든 플레이 상황의 누락 없음이나 전체 클리어 검증을 뜻하지는 않습니다.
원문의 의미와 캐릭터 말투를 기준으로 검수하고, 글자 수 제약이 있는 곳은 뜻을 유지하며 다듬었습니다.
띄어쓰기는 반각 공백을 사용합니다. 자판·영문 간판·배경 그래픽은 원본을 유지하고, 이미 번역한 영어 메뉴는 유지했습니다.

## v0.77 이후 v1.0에서 바뀐 내용

- **엔딩 크레딧 한글화:** 역할과 제작진 이름을 반영하고 마지막에 **`한글화 기타 깎는 노인`**을 추가했습니다. 원래 페이지 순서·표시 위치·타이밍·그림을 유지했습니다.
- **시나리오 3 제목 이미지 추가:** 누락된 `泥棒娘ラディア`를 **`도둑 소녀 라디아`**로 수정했습니다. 원래 영문 SCENARIO 표기와 문장·캐릭터 그래픽은 유지했습니다.
- **대사 넘침 일괄 점검:** 네이티브 글자 크기·줄 수·삽입 이름·제어 코드를 기준으로 16,188개 번역 항목을 점검하고, 넘침이 잡힌 74개 항목을 줄바꿈 또는 표현 조정으로 수정했습니다. 원래 대형 글씨와 대사 타이밍은 유지했습니다.
- **문자 폭 계산 보정:** 영문·숫자·문장부호도 게임의 실제 전각 폭으로 검사하고, 반각 공백과 구분합니다. 편집기 미리보기와 빌드 검사에도 반영했습니다.
- **상태 아이콘 9종 정리:** 원작 네모 안의 한자를 지우고 **갈무리7** 한 글자로 표시했습니다. 배경·테두리·그림자를 보존했으며 `염`의 획도 정리했습니다.
- **전투 불능 표기 수정:** 좁은 캐릭터 상태 칸에는 **`사`** 한 글자를 사용합니다.
- **합성·장비 비교 괄호 수정:** 비교값이 없을 때 나오는 원작의 `****` 표시와 숫자가 괄호 안에 들어가도록 공통 표시 8곳을 수정했습니다. 능력치·계산 방식은 그대로입니다.
- **클리어 정보 숫자 정렬:** 찾은 스톤 수의 숫자와 `/` 위치를 맞췄습니다. 수집 수와 총수는 원래 게임 값을 사용합니다.
- **좁은 UI 제목 정리:** **`특수능력`**, **`합성결과`**처럼 불필요한 공백을 빼고 칸 안에 들어가도록 했습니다.

v0.77의 필드 획득 메시지 추가 번역, `보유량`, `리커버` 계열과 `아이스(회피)`·`히트(마비)` 효과 표기, 기존 문맥 수정도 포함합니다.

## 인게임 스크린샷

아래 11장은 **실제 에뮬레이터 출력**입니다. 타이틀은 1.7.3, 일반 대사·설정·저장 및 보너스 관련 화면은 1.7.1,
오프닝은 1.7.2에서 촬영했습니다. **v1.0을 새로 촬영한 화면은 아닙니다.** 현재 오프닝 영상은 해당 자막 검증본과 같습니다.

### 대사 화면

성 안의 대화. 한글 대사와 원래 대화창·캐릭터 그래픽의 조합을 보여줍니다.

![성 안의 대화](https://raw.githubusercontent.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-1-Kr/v1.0/screenshots/dialogue-hall.png)

장소 안내 대화.

![장소 안내 대화](https://raw.githubusercontent.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-1-Kr/v1.0/screenshots/dialogue-guide.png)

사령실 앞의 대화.

![사령실 앞의 대화](https://raw.githubusercontent.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-1-Kr/v1.0/screenshots/dialogue-command-room.png)

대사 캡처는 당시의 장면 선택 시험 환경을 사용했습니다. 해당 시험용 연결은 배포 패치에 들어 있지 않습니다.

### 설정과 저장/불러오기

X/Y 화면 위치 수치를 분리하고, 스테레오/모노와 방식 A/B를 정렬했습니다.

![설정 화면](https://raw.githubusercontent.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-1-Kr/v1.0/screenshots/options.png)

저장 정보의 제목과 권·화 표기, 파일 선택 안내를 한글화했습니다.

![저장/불러오기 화면](https://raw.githubusercontent.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-1-Kr/v1.0/screenshots/save-load.png)

### 오프닝 자막

확인된 노랫말 9구간을 반영했습니다. 노랫말이 없다고 확인한 두 구간은 비워 두었습니다.
원래 영문 화면은 유지하고 한글 자막을 추가했으며, 화면 문구와 노랫말이 겹치는 구간은 위/아래로 구분했습니다.
원본 ADX 음성과 디코딩한 PCM이 같은 것을 확인했습니다.

![오프닝 가사 자막](https://raw.githubusercontent.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-1-Kr/v1.0/screenshots/opening-lyrics.png)

![화면 문구와 노랫말의 동시 표시](https://raw.githubusercontent.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-1-Kr/v1.0/screenshots/opening-both-captions.png)

![추가 화면 문구 자막](https://raw.githubusercontent.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-1-Kr/v1.0/screenshots/opening-fight-caption.png)

자막은 게임 영상에 반영되어 있습니다. ZIP에 동봉한 SRT는 참고 자료이며 따로 불러올 필요가 없습니다.

## 보너스 장신구 5종 언락

Vol.1 디스크에 원래 들어 있던 장신구 데이터와 다운로드 상점 코드를 사용합니다.
사령실의 해당 NPC와 원래 대화를 마치면 상점을 열도록 연결했으며,
외부 다운로드 데이터가 없는 저장 파일에도 다음 5종이 재고에 표시되도록 했습니다.
**인터넷 연결이나 다른 권의 추가 데이터 없이 이용하는 방식입니다.**

| 아이템 | 원본 ID |
| --- | --- |
| 크리스마스 트리 | `0xF5` |
| 목도리 | `0xF9` |
| 21CENTURY | `0xFE` |
| 눈사람 | `0xF7` |
| 스케이트화 | `0xF8` |

인벤토리에 자동 지급하지 않으며 상점에서 구매합니다. **원래 가격·능력치·효과를 유지합니다.**

![보너스 장신구와 장비 표시](https://raw.githubusercontent.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-1-Kr/v1.0/screenshots/bonus-items.png)

시험 환경에서 5종 구매·장비 표시·VMU 저장/재불러오기·필드 복귀를 확인했습니다.
위 장비 화면은 공개 게임 이미지로 새 부팅한 뒤 시험 VMU를 불러와 확인한 것입니다.
구매·저장 시험에는 무료 가격과 여관 저장 연결을 사용했고, **시험용 변경과 저장 파일은 배포물에서 제외**했습니다.
정상 스토리 경로로 상점에 도달하여 원래 가격으로 구매하는 전 과정은 미검증입니다.

<details>
<summary>상점 시험 화면 보기 — 이 캡처의 0 가격은 시험용입니다</summary>

![시험용 보너스 재고 화면](https://raw.githubusercontent.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-1-Kr/v1.0/screenshots/bonus-shop-test.png)

배포 패치는 일본판 원래 가격을 사용합니다.

</details>

## 최신 그래픽 수정 자료

이 절의 3장은 **인게임 스크린샷이 아니라 롬 그래픽 또는 편집 원본의 미리보기**입니다.

### 시나리오 3 제목

![시나리오 3 한글 제목 그래픽](https://raw.githubusercontent.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-1-Kr/v1.0/screenshots/chapter3-title-preview.png)

`도둑 소녀 라디아`. 제목 부분만 바꾸고 같은 리소스의 다른 캐릭터 그래픽과 영문 표기는 보존했습니다.

### 갈무리7 상태 아이콘

![상태 아이콘 갈무리9 이전안과 갈무리7 최종안 비교](https://raw.githubusercontent.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-1-Kr/v1.0/screenshots/status-galmuri7-comparison.png)

비교 이미지의 오른쪽이 최종 갈무리7입니다. `독`·`혼`·`마`·`사`·`공`·`방`·`염`·`속`·`회`를 원작 네모 안에 넣었습니다.

<details>
<summary>엔딩 마지막 한글화 표기 미리보기</summary>

![마지막 크레딧의 한글화 표기 그래픽](https://raw.githubusercontent.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-1-Kr/v1.0/screenshots/ending-localization-credit-preview.png)

검은 배경 위에 크레딧 글자만 표시한 편집 원본입니다. 엔딩 전체 재생을 촬영한 화면은 아닙니다.

</details>

## 검증 범위

- 최신 로컬 빌드 1.7.13의 3트랙 SHA-256을 배포 기준으로 고정했습니다.
- 변경 게임 파일 **53개를 완성 디스크에서 읽어 확인**하고 변경 섹터의 EDC/ECC를 검사했습니다.
- 번역 **16,188개 항목**의 레이아웃 점검에서 오류 0건을 확인했습니다. 원래 대형 글씨와 삽입 이름을 포함한 검사입니다.
- 저장된 이미지 편집 **110개**의 네이티브 미리보기를 확인했습니다.
- 대사 레이아웃·시나리오 3 제목·비교 괄호·클리어 숫자에 대한 개별 회귀 검사를 수행했습니다.
- Windows 배포 패처 EXE를 원본 GDI에 실제 적용하고, 결과가 기준 빌드와 같은지 검사했습니다. [적용 검증 결과](https://github.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-1-Kr/blob/v1.0/docs/installer-verification.json).

**미검증 범위:** 전체 정상 플레이, 정상 경로의 보너스 상점 접근/원래 가격 구매, 엔딩 전체 재생, 실기 및 실제 BIOS 구동.
자동 폭 검사로 잡히지 않는 상황별 배치나 문맥 문제가 남을 수 있습니다.
엔딩은 66페이지의 그래픽 반영과 읽기 검사를 마쳤지만, 전체 재생 검증은 포함하지 않았습니다.

[검증 요약](https://github.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-1-Kr/blob/v1.0/docs/verification.json) · [패처 적용 검증](https://github.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-1-Kr/blob/v1.0/docs/installer-verification.json) · [이미지 출처와 시험 조건](https://github.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-1-Kr/blob/v1.0/docs/screenshot-provenance.json) · [53개 변경 파일 해시](https://github.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-1-Kr/blob/v1.0/docs/changed-files-sha256.json)

오류 제보에는 사용 버전, 시나리오/장소, 문제 문구와 스크린샷을 남겨 주세요.

## 원본과 적용 후 SHA-256

| 파일 | 원본 SHA-256 | v1.0 적용 후 SHA-256 |
| --- | --- | --- |
| `track01.bin` | `5b4a5857228be738a116dd8487255a0eca81e6874ab6febdca646369e7ea81bf` | 동일 |
| `track02.raw` | `cd7c82d88f21e4ebb32a94c65f15f625df871c933d6d78cbf85c671778a6ffca` | 동일 |
| `track03.bin` | `85d40e5ded0b29bb5a6e3c9e53054ec15bafe2bbf65a10b7c81a7612b75a7b80` | `da0bb860f9d1a79441df87712f93ae9660b67370ad61e6c9163ec3878a099429` |

패치 파일 해시와 상세 내용은 [HASHES.md](https://github.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-1-Kr/blob/v1.0/docs/HASHES.md), 기계 판독용 정보는 [hashes.json](https://github.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-1-Kr/blob/v1.0/hashes.json)에 있습니다.

## 사용 도구·글꼴·크레딧

**한글화: 기타 깎는 노인**

- 적용 패처 소스: [tools/patcher.py](https://github.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-1-Kr/blob/v1.0/tools/patcher.py), MIT 라이선스.
- xdelta3 3.2.1: [공식 소스/릴리스](https://github.com/jmacd/xdelta/releases/tag/v3.2.1), Apache 2.0.
- 갈무리 및 MaruMinya: SIL Open Font License 1.1. [라이선스 전문](https://github.com/OldManCraveGuitars-bit/El-Dorado-Gate-Volume-1-Kr/tree/v1.0/licenses/).
- Python과 PyInstaller 관련 라이선스도 배포 ZIP에 포함합니다.

이 저장소의 패처 소스는 배포용 적용 도구입니다. 대사·이미지 비교 편집기는 별도의 작업 도구이며 ZIP에 포함하지 않습니다.
원작 게임과 상표의 권리는 원 권리자에게 있습니다. 이 한글판은 비공식입니다.

### 패처 소스 빌드

Python 3.13, PyInstaller 6.22.3과 공식 xdelta3 3.2.1 Windows x64 바이너리를 사용합니다.

```powershell
python -m pip install PyInstaller==6.22.3
.\tools\build-patcher.ps1 -Xdelta 'C:\경로\xdelta3.exe'
```

`dist`의 EXE와 릴리스 ZIP의 `track03-v1.0.xdelta`를 같은 폴더에 두면 실행할 수 있습니다.

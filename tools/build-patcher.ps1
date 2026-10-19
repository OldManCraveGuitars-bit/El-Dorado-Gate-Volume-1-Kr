param(
    [Parameter(Mandatory=$true)][string]$Xdelta,
    [string]$Python = 'python'
)
$ErrorActionPreference = 'Stop'
$taskRepo = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..')).Path
$taskEngine = (Resolve-Path -LiteralPath $Xdelta).Path
$taskManifest = Get-Content -LiteralPath (Join-Path $taskRepo 'hashes.json') -Raw | ConvertFrom-Json
$taskEngineHash = (Get-FileHash -LiteralPath $taskEngine -Algorithm SHA256).Hash.ToLowerInvariant()
if ($taskEngineHash -ne $taskManifest.xdelta.sha256) { throw 'xdelta3 3.2.1 Windows x64 release binary required' }
& $Python -m PyInstaller --noconfirm --onefile --windowed `
    --name 'El-Dorado-Gate-Volume-1-Kr-v0.77-Patcher' `
    --distpath (Join-Path $taskRepo 'dist') `
    --workpath (Join-Path $taskRepo 'build') `
    --specpath (Join-Path $taskRepo 'build') `
    --add-data ((Join-Path $taskRepo 'hashes.json') + ';.') `
    --add-binary ($taskEngine + ';.') `
    (Join-Path $PSScriptRoot 'patcher.py')
if ($LASTEXITCODE -ne 0) { throw 'PyInstaller build failed' }
Write-Output 'Place track03-v0.77.xdelta from the release ZIP beside the resulting EXE.'

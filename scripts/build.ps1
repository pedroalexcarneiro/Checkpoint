param(
    [string]$Python = 'python',
    [string]$BuildDirectory = (Join-Path $PSScriptRoot '..\work\pyinstaller')
)
$ErrorActionPreference = 'Stop'
$projectDirectory = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..'))
$distributionDirectory = Join-Path $projectDirectory 'dist'
if (-not ([IO.Path]::GetFullPath($distributionDirectory).StartsWith($projectDirectory + [IO.Path]::DirectorySeparatorChar))) { throw 'Destino de build inseguro.' }
$buildPath = [IO.Path]::GetFullPath($BuildDirectory)
New-Item -ItemType Directory -Force $buildPath | Out-Null
$env:PYINSTALLER_CONFIG_DIR = Join-Path $buildPath 'cache'
Push-Location $projectDirectory
try {
    # Preserve dados adicionais exigidos pelo runtime SSL utilizado no build.
    # Não altera nem desativa a política TLS do Python fornecido pelo ambiente.
    $runtimeTlsData = & $Python -c "import ssl,pathlib; p=pathlib.Path(ssl.__file__).parent/'codex-rejected-cas.pem'; print(str(p) if p.is_file() else '')"
    $runtimeTlsArgs = @()
    if ($runtimeTlsData) { $runtimeTlsArgs = @('--add-data', "$($runtimeTlsData);.") }
    $iconPath = Join-Path $buildPath 'checkpoint.ico'
    & $Python scripts/create_icon.py $iconPath
    if ($LASTEXITCODE -ne 0) { throw 'Falha ao gerar ícone.' }
    & $Python -m PyInstaller @runtimeTlsArgs --noconfirm --windowed --onedir --name Checkpoint --icon $iconPath --distpath $distributionDirectory --workpath $buildPath --specpath $buildPath --collect-data checkpoint --hidden-import keyring.backends.Windows --copy-metadata keyring run_checkpoint.py
    if ($LASTEXITCODE -ne 0) { throw 'Falha no empacotamento.' }
    $portable = Join-Path $distributionDirectory 'Checkpoint'
    & $Python -m PyInstaller --noconfirm --onedir --console --name CheckpointUpdater --distpath (Join-Path $buildPath 'helper-dist') --workpath (Join-Path $buildPath 'helper-build') --specpath $buildPath run_updater.py
    if ($LASTEXITCODE -ne 0) { throw 'Falha ao empacotar atualizador.' }
    Copy-Item -LiteralPath (Join-Path $buildPath 'helper-dist\CheckpointUpdater') -Destination $portable -Recurse
    Copy-Item -LiteralPath (Join-Path $PSScriptRoot 'LEIA-ME.txt') -Destination $portable
    foreach ($doc in @('PROJECT_STATUS.md','SETUP.md','INTEGRATIONS.md','THIRD_PARTY_NOTICES.md')) {
        Copy-Item -LiteralPath (Join-Path $projectDirectory $doc) -Destination $portable
    }
} finally { Pop-Location }

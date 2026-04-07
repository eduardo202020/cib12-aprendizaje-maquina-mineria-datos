$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $PSScriptRoot
$venv = Join-Path $root ".venv311"
$pythonExe = "py -3.11"

if (-not (Test-Path $venv)) {
    & py -3.11 -m venv $venv
}

$venvPython = Join-Path $venv "Scripts\python.exe"

& $venvPython -m pip install --upgrade pip setuptools wheel
& $venvPython -m pip install -r (Join-Path $root "requirements-py311.txt")
& $venvPython -m pip install -e (Join-Path $root "vendor\rssi_capturing_filtering_library") -e (Join-Path $root "vendor\models_fingerprint_positioning") --no-deps

Write-Host ""
Write-Host "Entorno listo en $venv"
Write-Host "Activalo con:"
Write-Host "  $venv\Scripts\Activate.ps1"

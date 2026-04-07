$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $PSScriptRoot
$python = Join-Path $root ".venv311\Scripts\python.exe"

if (-not (Test-Path $python)) {
    throw "No existe el entorno .venv311. Ejecuta primero scripts/bootstrap_env.ps1"
}

& $python (Join-Path $root "src\prepare_datasets.py") --fingerprint-name lab02_ble_ferrero
& $python (Join-Path $root "src\train_m2.py") --fingerprint-name lab02_ble_ferrero --variant with_empty_values
& $python (Join-Path $root "src\train_m2.py") --fingerprint-name lab02_ble_ferrero --variant without_empty_values
& $python (Join-Path $root "src\evaluate_m2.py") --fingerprint-name lab02_ble_ferrero --variant with_empty_values
& $python (Join-Path $root "src\evaluate_m2.py") --fingerprint-name lab02_ble_ferrero --variant without_empty_values

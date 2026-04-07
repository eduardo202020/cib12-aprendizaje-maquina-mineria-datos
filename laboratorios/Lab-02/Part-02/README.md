# Part-02

Esta carpeta esta destinada a la implementacion y reproduccion experimental del paper.

## Estructura

- `src`: scripts y modulos del proyecto
- `notebooks`: notebooks de exploracion, pruebas o analisis
- `datos`: dataset original o versiones procesadas
- `resultados`: metricas, tablas, graficos y evidencias

## Objetivo

Aqui se desarrollara la Parte II del laboratorio:

- preparacion del entorno
- descarga o adaptacion del dataset
- implementacion del pipeline
- entrenamiento y evaluacion
- comparacion con los resultados reportados en el paper

## Estado actual

Ya se ejecuto la fase de preparacion del pipeline:

- se clono el repo de modelos en `vendor/models_fingerprint_positioning`
- se clono la libreria de captura y filtrado en `vendor/rssi_capturing_filtering_library`
- se descargo el dataset en `datos/raw/Position-Annotated-BLE-RSSI-Dataset`
- se generaron los CSV procesados offline y online

## Scripts implementados

- `src/prepare_datasets.py`: genera fingerprints offline y online para las variantes `with_empty_values` y `without_empty_values`
- `src/train_m2.py`: entrenamiento del modelo M2
- `src/evaluate_m2.py`: evaluacion del modelo M2 sobre trayectorias online
- `src/run_pipeline.py`: orquestador del pipeline completo
- `src/common.py`: rutas y utilidades compartidas

## Resultados ya generados

Se generaron estos archivos procesados:

- `datos/processed/fingerprints/lab02_ble_ferrero/with_empty_values.csv`
- `datos/processed/fingerprints/lab02_ble_ferrero/without_empty_values.csv`
- `datos/processed/online/lab02_ble_ferrero/with_empty_values.csv`
- `datos/processed/online/lab02_ble_ferrero/without_empty_values.csv`
- `datos/processed/online/lab02_ble_ferrero/preparation_summary.json`

Resumen actual:

- `with_empty_values`: 213558 filas offline y 662 filas online
- `without_empty_values`: 141713 filas offline y 486 filas online

## Comandos de ejecucion

Preparar datasets:

```powershell
python laboratorios\Lab-02\Part-02\src\prepare_datasets.py --fingerprint-name lab02_ble_ferrero
```

Entrenar M2:

```powershell
python laboratorios\Lab-02\Part-02\src\train_m2.py --fingerprint-name lab02_ble_ferrero --variant with_empty_values
python laboratorios\Lab-02\Part-02\src\train_m2.py --fingerprint-name lab02_ble_ferrero --variant without_empty_values
```

Evaluar M2:

```powershell
python laboratorios\Lab-02\Part-02\src\evaluate_m2.py --fingerprint-name lab02_ble_ferrero --variant with_empty_values
python laboratorios\Lab-02\Part-02\src\evaluate_m2.py --fingerprint-name lab02_ble_ferrero --variant without_empty_values
```

Pipeline completo:

```powershell
python laboratorios\Lab-02\Part-02\src\run_pipeline.py --fingerprint-name lab02_ble_ferrero
```

## Bloqueo actual del entorno

El entrenamiento y la evaluacion no pudieron ejecutarse todavia en esta maquina porque el interprete disponible es `Python 3.14`, y TensorFlow para el pipeline del paper requiere normalmente `Python 3.10` o `3.11`.

El bloqueo ya esta manejado en los scripts:

- `train_m2.py` valida la version de Python antes de arrancar
- `evaluate_m2.py` hace la misma validacion

Por tanto, la reproduccion ya avanzo hasta la fase de preparacion real del dataset y queda lista para continuar apenas se disponga de un entorno compatible con TensorFlow.

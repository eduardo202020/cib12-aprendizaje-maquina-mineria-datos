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
- se creo un entorno compatible en `.venv311`
- se entreno `M2` para ambas variantes
- se evaluo `M2` sobre trayectorias online

## Scripts implementados

- `src/prepare_datasets.py`: genera fingerprints offline y online para las variantes `with_empty_values` y `without_empty_values`
- `src/train_m2.py`: entrenamiento del modelo M2
- `src/evaluate_m2.py`: evaluacion del modelo M2 sobre trayectorias online
- `src/run_pipeline.py`: orquestador del pipeline completo
- `src/common.py`: rutas y utilidades compartidas
- `scripts/bootstrap_env.ps1`: crea y prepara `.venv311`
- `scripts/run_all.ps1`: ejecuta el pipeline completo con el entorno local

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

## Entorno compatible

Se preparo un entorno local compatible en:

- `.venv311`

Versiones usadas:

- Python `3.11`
- TensorFlow `2.15.1`
- NumPy `1.26.4`
- Pandas `2.2.3`
- SciPy `1.11.4`
- scikit-learn `1.4.2`

Preparar el entorno desde cero:

```powershell
powershell -ExecutionPolicy Bypass -File laboratorios\Lab-02\Part-02\scripts\bootstrap_env.ps1
```

Activarlo manualmente:

```powershell
laboratorios\Lab-02\Part-02\.venv311\Scripts\Activate.ps1
```

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

Pipeline completo con el entorno local:

```powershell
powershell -ExecutionPolicy Bypass -File laboratorios\Lab-02\Part-02\scripts\run_all.ps1
```

## Resultados obtenidos

Ya se entreno y evaluo `M2` en ambas variantes. Los artefactos quedaron en:

- `resultados/models/M2/with_empty_values`
- `resultados/models/M2/without_empty_values`
- `resultados/metrics/m2_with_empty_values_evaluation.json`
- `resultados/metrics/m2_without_empty_values_evaluation.json`

Metricas actuales:

- `with_empty_values`
  media: `2.3690 m`
  mediana: `2.1413 m`
- `without_empty_values`
  media: `2.0750 m`
  mediana: `1.8430 m`

## Comparacion rapida con el paper

- Paper `with_empty_values`: media `2.0368`, mediana `1.8199`
- Reproduccion actual `with_empty_values`: media `2.3690`, mediana `2.1413`
- Paper `without_empty_values`: media `2.0559`, mediana `1.7745`
- Reproduccion actual `without_empty_values`: media `2.0750`, mediana `1.8430`

La variante sin valores vacios quedo muy cercana a lo reportado por el paper.  
La variante con valores vacios todavia muestra una brecha mayor, lo que sugiere que ahi puede haber diferencias en el preprocesamiento, en la construccion exacta de fingerprints o en la forma en que el paper manejo los valores faltantes.

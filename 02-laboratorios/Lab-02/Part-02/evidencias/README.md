# Evidencias de Ejecucion

Esta carpeta resume la evidencia minima de la Parte II del laboratorio y ahora esta organizada por tipo de uso.

## Estructura

- `base`: evidencia general de la reproduccion principal
- `seed_sweep/with_empty_values`: espacio para evidencia de barrido de semillas
- `semana-01` a `semana-04`: material de avance para exponer cada semana

## Entorno utilizado

- Python `3.11.9`
- TensorFlow `2.15.1`
- NumPy `1.26.4`
- Pandas `2.2.3`
- SciPy `1.11.4`
- scikit-learn `1.4.2`

## Codigo fuente usado

- Repositorio del curso: `https://github.com/eduardo202020/cib12-aprendizaje-maquina-mineria-datos`
- Implementacion principal:
  - `src/prepare_datasets.py`
  - `src/train_m2.py`
  - `src/evaluate_m2.py`
  - `src/run_pipeline.py`

## Resultados resumidos

- `with_empty_values`: media `2.3690 m`, mediana `2.1413 m`
- `with_empty_values_seed21`: media `2.3169 m`, mediana `1.9804 m`
- `without_empty_values`: media `2.0750 m`, mediana `1.8430 m`

## Evidencia incluida

- `base/metricas-reproduccion.csv`: tabla compacta de metricas
- `base/comandos-ejecutados.txt`: comandos principales del pipeline

## Nota

Los modelos, CSV procesados y metricas JSON completas existen en `resultados/`, pero no se versionan para evitar commits pesados. Esta carpeta conserva la evidencia resumida necesaria para sustentar la ejecucion real.

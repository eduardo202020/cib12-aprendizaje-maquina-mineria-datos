# Part-02

Esta carpeta contiene la reproduccion experimental del paper y ahora esta organizada para trabajarse en **4 semanas**, mostrando avances graduales en clase.

## Objetivo

Reproducir de forma defendible el pipeline principal del paper:

- preparar el entorno,
- generar fingerprints offline y online,
- entrenar el modelo `M2`,
- evaluar sobre trayectorias reales,
- comparar los resultados con el paper,
- y documentar el proceso con evidencia.

## Estructura principal

- `docs`: plan, cronograma, implementacion e informe
- `src`: scripts del pipeline
- `scripts`: utilidades PowerShell para entorno y ejecucion completa
- `datos`: dataset crudo y versiones procesadas
- `resultados`: modelos, metricas y salidas del experimento
- `evidencias`: soporte de ejecucion organizado en `base`, `seed_sweep` y `semana-*`
- `vendor`: repositorios originales usados para la reproduccion

## Ruta de trabajo en 4 semanas

- `Semana 1`: entorno, dataset, verificacion metodologica y generacion de fingerprints
- `Semana 2`: entrenamiento y evaluacion base de `M2` en `without_empty_values`
- `Semana 3`: entrenamiento y evaluacion de `M2` en `with_empty_values` y exploracion de semillas
- `Semana 4`: comparacion final con el paper, tablas, figuras y consolidacion del informe

La guia detallada esta en:

- [docs/PLAN-4-SEMANAS.md](C:/Users/pc/Documents/trabajos/cib12-aprendizaje-maquina-mineria-datos/laboratorios/Lab-02/Part-02/docs/PLAN-4-SEMANAS.md)
- [docs/cronograma/semana-01.md](C:/Users/pc/Documents/trabajos/cib12-aprendizaje-maquina-mineria-datos/laboratorios/Lab-02/Part-02/docs/cronograma/semana-01.md)
- [docs/cronograma/semana-02.md](C:/Users/pc/Documents/trabajos/cib12-aprendizaje-maquina-mineria-datos/laboratorios/Lab-02/Part-02/docs/cronograma/semana-02.md)
- [docs/cronograma/semana-03.md](C:/Users/pc/Documents/trabajos/cib12-aprendizaje-maquina-mineria-datos/laboratorios/Lab-02/Part-02/docs/cronograma/semana-03.md)
- [docs/cronograma/semana-04.md](C:/Users/pc/Documents/trabajos/cib12-aprendizaje-maquina-mineria-datos/laboratorios/Lab-02/Part-02/docs/cronograma/semana-04.md)

## Scripts ya disponibles

- `src/prepare_datasets.py`: genera fingerprints offline y online
- `src/train_m2.py`: entrena el modelo `M2`
- `src/evaluate_m2.py`: evalua `M2` sobre trayectorias online
- `src/run_pipeline.py`: ejecuta el pipeline completo
- `src/common.py`: rutas y utilidades compartidas
- `scripts/bootstrap_env.ps1`: prepara `.venv311`
- `scripts/run_all.ps1`: ejecuta el pipeline completo con el entorno local

## Estado tecnico actual

Ya estan disponibles:

- entorno local `.venv311`
- dataset en `datos/raw/Position-Annotated-BLE-RSSI-Dataset`
- CSV procesados offline y online
- entrenamiento de `M2` para ambas variantes
- evaluaciones base y exploratorias

Documentacion principal:

- `docs/implementacion.md`
- `docs/PLAN-4-SEMANAS.md`
- `docs/informe/informe.tex`
- `docs/informe/informe.pdf`

## Resultados ya generados

Artefactos principales:

- `datos/processed/fingerprints/lab02_ble_ferrero/with_empty_values.csv`
- `datos/processed/fingerprints/lab02_ble_ferrero/without_empty_values.csv`
- `datos/processed/online/lab02_ble_ferrero/with_empty_values.csv`
- `datos/processed/online/lab02_ble_ferrero/without_empty_values.csv`
- `resultados/experimentos/M2/base/with_empty_values`
- `resultados/experimentos/M2/base/without_empty_values`
- `resultados/comparativas/metricas/M2/base/with_empty_values_evaluation.json`
- `resultados/comparativas/metricas/M2/base/without_empty_values_evaluation.json`

Resumen actual:

- `with_empty_values`: media `2.3690 m`, mediana `2.1413 m`
- `with_empty_values_seed21`: media `2.3169 m`, mediana `1.9804 m`
- `without_empty_values`: media `2.0750 m`, mediana `1.8430 m`

## Carpetas de avance semanal

Para ir mostrando progreso de a poco se dejaron listas estas carpetas:

- `evidencias/base`
- `evidencias/seed_sweep/with_empty_values`
- `resultados/semana-01`
- `resultados/semana-02`
- `resultados/semana-03`
- `resultados/semana-04`
- `evidencias/semana-01`
- `evidencias/semana-02`
- `evidencias/semana-03`
- `evidencias/semana-04`

Cada semana deberia dejar al menos:

- una nota corta de lo realizado,
- los comandos ejecutados,
- una tabla o metrica resumida,
- y una evidencia que puedas mostrar en clase.

## Comandos base

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

## Recomendacion de ejecucion

No conviene volver a presentar el pipeline como una sola corrida grande. Para clase es mejor partirlo asi:

1. preparar y explicar los datos,
2. mostrar una primera reproduccion cercana al paper,
3. mostrar el escenario mas dificil y el ajuste de semillas,
4. cerrar con comparacion, discusion y conclusiones.

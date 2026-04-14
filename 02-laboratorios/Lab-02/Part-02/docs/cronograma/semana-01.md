# Semana 1

## Objetivo de la semana

Dejar listo el experimento a nivel de datos y demostrar que el pipeline de preparacion reproduce la logica metodologica del paper.

## Actividades realizadas

- se verifico el dataset en `datos/raw/Position-Annotated-BLE-RSSI-Dataset`
- se ejecuto la preparacion de fingerprints offline y online
- se generaron las variantes `with_empty_values` y `without_empty_values`
- se reviso el resumen metodologico en `preparation_summary.json`

## Comandos ejecutados

```powershell
python 01-organizacion-cib12\02-laboratorios\Lab-02\Part-02\src\prepare_datasets.py --fingerprint-name lab02_ble_ferrero
```

## Archivos generados o revisados

- `datos/processed/fingerprints/lab02_ble_ferrero/with_empty_values.csv`
- `datos/processed/fingerprints/lab02_ble_ferrero/without_empty_values.csv`
- `datos/processed/online/lab02_ble_ferrero/with_empty_values.csv`
- `datos/processed/online/lab02_ble_ferrero/without_empty_values.csv`
- `datos/processed/online/lab02_ble_ferrero/preparation_summary.json`

## Resultados obtenidos

| Metrica | with_empty_values | without_empty_values |
|---|---:|---:|
| sensores | 12 | 12 |
| filas offline | 213558 | 141713 |
| filas online | 662 | 486 |
| sensores minimos validos | 10 | 12 |

## Interpretacion breve

La preparacion de datos fue exitosa y ya deja dos escenarios comparables con el paper. La diferencia central entre ambos no esta en el entorno ni en la arquitectura del experimento, sino en la regla de validacion de sensores, lo que afecta cuantas muestras entran al pipeline.

## Que voy a mostrar en clase

- origen del dataset
- diferencia entre fase `offline` y `online`
- conteo de filas generadas por variante
- parametros del paper que se respetaron en la preparacion

## Dificultades encontradas

- el pipeline no era facil de leer porque habia demasiados archivos mezclados
- fue necesario ordenar la estructura de `Part-02` para que la evidencia fuera trazable

## Siguiente paso

La siguiente semana se entrenara y evaluara `M2` en el escenario `without_empty_values`, porque es la variante mas estable y la mas cercana a lo reportado por el paper.

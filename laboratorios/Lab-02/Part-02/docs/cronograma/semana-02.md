# Semana 2

## Objetivo de la semana

Mostrar una primera reproduccion fuerte usando el escenario mas estable: `without_empty_values`.

## Actividades realizadas

- se entreno el modelo `M2` sobre la variante `without_empty_values`
- se evaluo el modelo sobre trayectorias online
- se guardaron modelo, escalador y resumen de entrenamiento
- se compararon media y mediana con el paper

## Comandos ejecutados

```powershell
python laboratorios\Lab-02\Part-02\src\train_m2.py --fingerprint-name lab02_ble_ferrero --variant without_empty_values
python laboratorios\Lab-02\Part-02\src\evaluate_m2.py --fingerprint-name lab02_ble_ferrero --variant without_empty_values
```

## Archivos generados o revisados

- `resultados/experimentos/M2/base/without_empty_values/model.keras`
- `resultados/experimentos/M2/base/without_empty_values/scaler.pkl`
- `resultados/experimentos/M2/base/without_empty_values/training_summary.json`
- `resultados/comparativas/metricas/M2/base/without_empty_values_evaluation.json`

## Resultados obtenidos

| Metrica | Valor |
|---|---:|
| media | 2.0750 m |
| mediana | 1.8430 m |
| minimo | 0.0517 m |
| maximo | 8.1161 m |
| muestras | 486 |
| epocas | 30 |

## Comparacion con el paper

| Escenario | Paper | Reproduccion | Diferencia |
|---|---:|---:|---:|
| media | 2.0559 | 2.0750 | 0.0191 |
| mediana | 1.7745 | 1.8430 | 0.0685 |

## Interpretacion breve

Esta reproduccion quedo muy cercana al paper, especialmente en el error medio. Eso respalda que el pipeline general, el preprocesamiento y la configuracion de entrenamiento de `M2` son consistentes con lo descrito por los autores.

## Que voy a mostrar en clase

- parametros de entrenamiento de `M2`
- numero de epocas ejecutadas
- media y mediana de error
- comparacion corta contra el paper

## Dificultades encontradas

- fue necesario reorganizar `resultados` para separar modelos entrenados de metricas comparativas

## Siguiente paso

La siguiente semana se trabajara `with_empty_values`, que es el escenario mas dificil, y se hara una exploracion de semillas para intentar reducir la brecha con el paper.

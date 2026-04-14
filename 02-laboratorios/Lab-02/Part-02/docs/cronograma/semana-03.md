# Semana 3

## Objetivo de la semana

Experimentar con el escenario mas desafiante: `with_empty_values`, y mostrar mejoras parciales sobre la corrida base.

## Actividades realizadas

- se entreno la corrida base de `M2` con `with_empty_values`
- se evaluo la corrida base sobre trayectorias online
- se ejecutaron corridas exploratorias con distintas semillas
- se identifico `seed21` como la mejor corrida exploratoria disponible

## Comandos ejecutados

```powershell
python 01-organizacion-cib12\02-laboratorios\Lab-02\Part-02\src\train_m2.py --fingerprint-name lab02_ble_ferrero --variant with_empty_values
python 01-organizacion-cib12\02-laboratorios\Lab-02\Part-02\src\evaluate_m2.py --fingerprint-name lab02_ble_ferrero --variant with_empty_values
python 01-organizacion-cib12\02-laboratorios\Lab-02\Part-02\src\train_m2.py --fingerprint-name lab02_ble_ferrero --variant with_empty_values --seed 21 --tag seed21
python 01-organizacion-cib12\02-laboratorios\Lab-02\Part-02\src\evaluate_m2.py --fingerprint-name lab02_ble_ferrero --variant with_empty_values --tag seed21
```

## Archivos generados o revisados

- `resultados/experimentos/M2/base/with_empty_values`
- `resultados/experimentos/M2/seed_sweep/with_empty_values/seed21`
- `resultados/comparativas/metricas/M2/base/with_empty_values_evaluation.json`
- `resultados/comparativas/metricas/M2/seed_sweep/with_empty_values/seed21_evaluation.json`

## Resultados obtenidos

| Corrida | Media | Mediana | Min | Max |
|---|---:|---:|---:|---:|
| base | 2.3690 | 2.1413 | 0.0743 | 15.9757 |
| seed21 | 2.3169 | 1.9804 | 0.1214 | 16.1974 |

## Comparacion con el paper

| Escenario | Paper | Reproduccion | Diferencia |
|---|---:|---:|---:|
| media base | 2.0368 | 2.3690 | 0.3322 |
| mediana base | 1.8199 | 2.1413 | 0.3214 |
| media seed21 | 2.0368 | 2.3169 | 0.2801 |
| mediana seed21 | 1.8199 | 1.9804 | 0.1605 |

## Interpretacion breve

El escenario con valores vacios es claramente mas sensible que el escenario sin vacios. La exploracion de semillas mejoro la reproduccion, pero aun queda una brecha visible respecto al paper, lo que sugiere sensibilidad a la inicializacion y posibles diferencias de detalle en el preprocesamiento o en la construccion exacta de fingerprints.

## Que voy a mostrar en clase

- por que este escenario es mas dificil
- diferencia entre corrida base y `seed21`
- brecha restante respecto al paper
- hipotesis sobre la causa de la diferencia

## Dificultades encontradas

- el escenario con vacios es mas inestable
- la mejora existe, pero no alcanza todavia el valor del paper

## Siguiente paso

La siguiente semana se consolidaran todas las metricas, se armara la comparacion final con el paper y se cerrara el informe tecnico.

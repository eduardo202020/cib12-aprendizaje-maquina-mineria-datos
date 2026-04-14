# Semana 4

## Objetivo de la semana

Consolidar la reproduccion completa y cerrar con una comparacion critica contra el paper.

## Actividades realizadas

- se consolidaron las metricas de `without_empty_values`, `with_empty_values` y `seed21`
- se organizo una tabla final de comparacion con el paper
- se actualizo la estructura de `resultados` y `evidencias`
- se dejo listo el material para el informe tecnico y la exposicion final

## Archivos generados o revisados

- `evidencias/base/metricas-reproduccion.csv`
- `resultados/comparativas/metricas/M2/base/without_empty_values_evaluation.json`
- `resultados/comparativas/metricas/M2/base/with_empty_values_evaluation.json`
- `resultados/comparativas/metricas/M2/seed_sweep/with_empty_values/seed21_evaluation.json`
- `docs/informe/informe.tex`

## Resultados obtenidos

| Escenario | Media | Mediana |
|---|---:|---:|
| with_empty_values | 2.3690 | 2.1413 |
| with_empty_values_seed21 | 2.3169 | 1.9804 |
| without_empty_values | 2.0750 | 1.8430 |

## Comparacion final con el paper

| Escenario | Paper media | Reproduccion media | Paper mediana | Reproduccion mediana |
|---|---:|---:|---:|---:|
| with_empty_values | 2.0368 | 2.3690 | 1.8199 | 2.1413 |
| with_empty_values_seed21 | 2.0368 | 2.3169 | 1.8199 | 1.9804 |
| without_empty_values | 2.0559 | 2.0750 | 1.7745 | 1.8430 |

## Interpretacion breve

La reproduccion fue metodologicamente consistente. El escenario `without_empty_values` quedo muy cercano al paper y confirma que el pipeline general funciona bien. El escenario `with_empty_values` mantuvo una brecha mayor, incluso despues de explorar semillas, lo que sugiere que esa parte del problema depende mas de detalles finos del preprocesamiento y de la inicializacion.

## Que voy a mostrar en clase

- tabla final comparativa
- escenario mas cercano al paper
- escenario con mayor brecha
- conclusion sobre si la reproduccion fue exitosa

## Dificultades encontradas

- el escenario con vacios no replica tan de cerca como el escenario sin vacios
- fue necesario reorganizar carpetas para que el laboratorio quede claro y defendible

## Siguiente paso

Cerrar la redaccion del informe y preparar las capturas finales desde los notebooks semanales.

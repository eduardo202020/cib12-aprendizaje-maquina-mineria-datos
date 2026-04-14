# Resultados

Esta carpeta agrupa las salidas del experimento por tipo de uso.

## Estructura

- `experimentos/`: artefactos de entrenamiento por modelo y corrida
- `comparativas/`: metricas listas para contrastar con el paper
- `semana-01` a `semana-04`: resumenes semanales para presentar avances
- `logs/`: salidas auxiliares si se decide registrar ejecuciones futuras

## Convencion usada para M2

### Corridas base

- `experimentos/M2/base/with_empty_values`
- `experimentos/M2/base/without_empty_values`

### Barrido de semillas

- `experimentos/M2/seed_sweep/with_empty_values/seed1`
- `experimentos/M2/seed_sweep/with_empty_values/seed7`
- `experimentos/M2/seed_sweep/with_empty_values/seed21`
- `experimentos/M2/seed_sweep/with_empty_values/seed42`
- `experimentos/M2/seed_sweep/with_empty_values/seed84`

### Metricas comparativas

- `comparativas/metricas/M2/base/with_empty_values_evaluation.json`
- `comparativas/metricas/M2/base/without_empty_values_evaluation.json`
- `comparativas/metricas/M2/seed_sweep/with_empty_values/*.json`

## Criterio

La idea es separar:

- donde se guarda el modelo entrenado,
- donde se guarda la metrica de comparacion,
- y donde se deja el material semanal para exponer.

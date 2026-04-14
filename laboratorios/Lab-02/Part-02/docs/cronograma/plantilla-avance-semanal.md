# Plantilla de Avance Semanal

Usa esta plantilla para registrar cada semana lo que hiciste, lo que obtuviste y lo que vas a mostrar en clase.

## Semana

`Semana X`

## Objetivo de la semana

Escribe en una o dos lineas que buscabas lograr.

Ejemplo:

`Entrenar y evaluar el modelo M2 en la variante without_empty_values para verificar si el pipeline reproduce resultados cercanos al paper.`

## Actividades realizadas

- actividad 1
- actividad 2
- actividad 3

Ejemplo:

- active el entorno `.venv311`
- ejecute el script de entrenamiento de `M2`
- ejecute la evaluacion online
- revise las metricas generadas en `resultados/comparativas/metricas`

## Comandos ejecutados

```powershell
# pega aqui los comandos realmente usados
```

## Archivos generados o revisados

- archivo 1
- archivo 2
- archivo 3

Ejemplo:

- `resultados/experimentos/M2/base/without_empty_values`
- `resultados/comparativas/metricas/M2/base/without_empty_values_evaluation.json`
- `evidencias/base/metricas-reproduccion.csv`

## Resultados obtenidos

Registra aqui los resultados mas importantes.

| Metrica | Valor |
|---|---|
| media | |
| mediana | |
| minimo | |
| maximo | |
| muestras | |

## Comparacion con el paper

| Escenario | Paper | Reproduccion | Diferencia |
|---|---:|---:|---:|
| media | | | |
| mediana | | | |

## Interpretacion breve

Escribe un parrafo corto contestando:

- que significa el resultado,
- si esta cerca o lejos del paper,
- y por que crees que paso eso.

Ejemplo:

`La reproduccion quedo bastante cerca del paper en la variante sin valores vacios. Esto sugiere que el pipeline general y los parametros de entrenamiento son consistentes. La brecha restante podria estar asociada a diferencias de semilla, version de librerias o detalles no totalmente especificados en el articulo.`

## Que voy a mostrar en clase

- punto 1
- punto 2
- punto 3

Ejemplo:

- arquitectura general del pipeline
- tabla con media y mediana
- comparacion rapida contra el paper

## Dificultades encontradas

- dificultad 1
- dificultad 2

## Siguiente paso

Escribe cual es el paso concreto de la siguiente semana.

Ejemplo:

`La siguiente semana trabajare la variante with_empty_values y realizare una exploracion controlada de semillas para ver si puedo reducir la brecha con el paper.`

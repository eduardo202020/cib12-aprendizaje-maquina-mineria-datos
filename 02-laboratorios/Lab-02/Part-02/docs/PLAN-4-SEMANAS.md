# Plan de Trabajo en 4 Semanas

Este plan divide la reproduccion experimental del paper en cuatro bloques manejables para que puedas avanzar y exponer resultados de manera progresiva.

## Vista general

| Semana | Enfoque | Resultado visible |
|---|---|---|
| 1 | Preparacion y datos | Fingerprints generados y pipeline entendido |
| 2 | Reproduccion base estable | `M2` entrenado y evaluado en `without_empty_values` |
| 3 | Escenario dificil y ajustes | `M2` en `with_empty_values` y barrido de semillas |
| 4 | Cierre experimental | Comparacion final, tablas, graficos e informe |

## Semana 1

Objetivo:
dejar listo el entorno y demostrar que el dataset fue transformado correctamente al formato del experimento.

Debes completar:

- activar `.venv311`
- revisar estructura de `datos/raw`
- ejecutar `prepare_datasets.py`
- verificar las dos variantes:
  - `with_empty_values`
  - `without_empty_values`
- registrar cuantos fingerprints offline y online se generaron

Debes mostrar:

- el dataset usado
- el diagrama `offline -> online`
- los CSV procesados generados
- el resumen de preparacion

Entregable semanal:

- evidencia en `evidencias/semana-01`
- resumen en `resultados/semana-01`

## Semana 2

Objetivo:
realizar la primera reproduccion fuerte con el escenario mas estable, `without_empty_values`.

Debes completar:

- entrenar `M2` en `without_empty_values`
- evaluar en trayectorias online
- guardar modelo y metricas
- comparar de forma preliminar con el paper

Debes mostrar:

- configuracion de entrenamiento
- curva simple de entrenamiento si la tienes
- media y mediana de error
- comparacion corta contra el paper

Meta:

este escenario ya esta cerca del paper y sirve como demostracion de que el pipeline es consistente.

## Semana 3

Objetivo:
trabajar el escenario mas dificil, `with_empty_values`, y mostrar una mejora incremental.

Debes completar:

- entrenar `M2` en `with_empty_values`
- evaluar la corrida base
- correr exploracion de semillas
- identificar la mejor corrida

Debes mostrar:

- por que este escenario es mas dificil
- diferencia entre corrida base y mejor corrida exploratoria
- brecha restante respecto al paper
- posibles causas tecnicas de la diferencia

Meta:

esta semana debe verse como una experimentacion real, no solo como repeticion del pipeline.

## Semana 4

Objetivo:
cerrar la reproduccion con comparacion final, organizacion de evidencia y redaccion del informe.

Debes completar:

- consolidar metricas finales
- armar una tabla comparativa con paper vs reproduccion
- generar 1 o 2 graficos simples
- redactar discusion y conclusiones
- dejar el informe casi listo

Debes mostrar:

- tabla final comparativa
- conclusion sobre si la reproduccion fue exitosa
- fortalezas, limitaciones y proximos pasos

## Criterio de avance

Si en una semana no alcanzas a hacer todo, prioriza siempre este orden:

1. reproducibilidad
2. metrica visible
3. comparacion con el paper
4. presentacion bonita

## Archivos de referencia

- [implementacion.md](C:/Users/pc/Documents/trabajos/cib12-aprendizaje-maquina-mineria-datos/02-laboratorios/Lab-02/Part-02/docs/implementacion.md)
- [cronograma/plantilla-avance-semanal.md](C:/Users/pc/Documents/trabajos/cib12-aprendizaje-maquina-mineria-datos/02-laboratorios/Lab-02/Part-02/docs/cronograma/plantilla-avance-semanal.md)
- [cronograma/semana-01.md](C:/Users/pc/Documents/trabajos/cib12-aprendizaje-maquina-mineria-datos/02-laboratorios/Lab-02/Part-02/docs/cronograma/semana-01.md)
- [cronograma/semana-02.md](C:/Users/pc/Documents/trabajos/cib12-aprendizaje-maquina-mineria-datos/02-laboratorios/Lab-02/Part-02/docs/cronograma/semana-02.md)
- [cronograma/semana-03.md](C:/Users/pc/Documents/trabajos/cib12-aprendizaje-maquina-mineria-datos/02-laboratorios/Lab-02/Part-02/docs/cronograma/semana-03.md)
- [cronograma/semana-04.md](C:/Users/pc/Documents/trabajos/cib12-aprendizaje-maquina-mineria-datos/02-laboratorios/Lab-02/Part-02/docs/cronograma/semana-04.md)

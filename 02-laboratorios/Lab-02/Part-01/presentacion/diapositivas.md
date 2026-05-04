# Exposicion - Paper Individual

## Paper elegido

- Titulo: `Bluetooth low energy indoor positioning: A fingerprinting neural network approach`
- Autores: Alberto Ferrero-Lopez, Antonio Javier Gallego y Miguel Angel Lozano
- Revista: `Internet of Things`
- Ano: 2025
- DOI: `10.1016/j.iot.2025.101565`

## Idea central de la exposicion

El paper propone una metodologia completa para localizacion indoor con BLE.  
No se limita a entrenar una red neuronal, sino que integra:

- captura de senales RSSI;
- filtrado de ruido;
- construccion de fingerprints;
- comparacion entre varios modelos;
- evaluacion en trayectorias reales.

## Diapositiva 1 - Portada

- Presentar el titulo del paper.
- Indicar autores, revista, ano y curso.
- Explicar brevemente por que se eligio este paper.

## Diapositiva 2 - Referencia del paper

- El articulo pertenece al area de IA aplicada a telecomunicaciones.
- Usa BLE, RSSI y aprendizaje automatico para resolver localizacion indoor.
- Su valor para el laboratorio es que tiene paper, dataset y repositorios publicos.

## Diapositiva 3 - Introduccion al problema

- El GPS funciona mal en interiores.
- En interiores aparecen atenuacion, obstaculos y efecto multipath.
- BLE es una alternativa de bajo costo y bajo consumo.
- El RSSI sirve como insumo, pero es ruidoso e inestable.

## Diapositiva 4 - Antecedentes

- Fingerprinting probabilistico.
- Fingerprinting con redes neuronales.
- Trilateracion BLE como baseline clasico.

Idea critica:

Muchos trabajos previos no explican bien la captura de senal, el filtrado o la evaluacion real sobre trayectorias.

## Diapositiva 5 - Objetivo e hipotesis inferida

- Objetivo: analizar un pipeline completo de posicionamiento indoor con BLE y fingerprinting.
- Se optimiza la etapa de captura y filtrado antes del modelo.
- Se comparan ocho arquitecturas neuronales y trilateracion.

Hipotesis inferida:

Si la senal RSSI se captura y filtra adecuadamente, y luego se usa una red neuronal apropiada, se puede superar a la trilateracion clasica y al estado del arte previo.

## Diapositiva 6 - Metodologia general

Fase 1:

- beacon BLE emite senales;
- 12 sensores capturan RSSI;
- una ventana temporal almacena lecturas recientes;
- se filtran los datos y se construye un fingerprint.

Fase 2:

- el fingerprint entra a un modelo de regresion o clasificacion;
- tambien se compara con trilateracion.

## Diapositiva 7 - Datos y configuracion experimental

- Dataset: `Position-Annotated-BLE-RSSI-Dataset`
- Sala: `20.66 x 17.64 m`
- Sensores: `12`
- Ground truth: vision por computador con marcadores ArUco
- Fase offline: huellas para entrenamiento
- Fase online: trayectorias reales para prueba

## Diapositiva 8 - Modelos y parametros

Modelos:

- `M1`: baseline denso
- `M2`: red densa mas profunda
- `M3` y `M4`: modelos con mascara para valores vacios
- `M5`: CNN 1D
- `M6`, `M7`, `M8`: clasificacion por grillas

Parametros clave:

- `Sreads_min = 2`
- `Svalid_min = 10` o `12`
- filtro `Max`
- `omega_min = 0.5 s`
- `omega_max = 2.5 s`

## Diapositiva 9 - Resultados principales

Con valores vacios:

- `M4`: `1.8957 m`
- `M2`: `2.0368 m`

Sin valores vacios:

- `M2`: `2.0559 m`
- `M5`: `2.0766 m`

Comparacion:

- trilateracion: mas de `3.3 m`
- estado del arte previo: `3.064 m`

Conclusion parcial:

Los modelos de regresion superan a los de clasificacion.

## Diapositiva 10 - Discusion

- M2 destaca por estabilidad entre escenarios.
- M3 y M4 funcionan mejor cuando hay datos faltantes.
- Las metricas de entrenamiento no bastan para medir rendimiento real.
- La distancia euclidiana es mejor que accuracy para este problema.

## Diapositiva 11 - Analisis critico

Fortalezas:

- metodologia completa;
- comparacion entre varios modelos;
- evaluacion en trayectorias reales;
- disponibilidad de dataset y codigo.

Limitaciones:

- dependencia de un entorno experimental concreto;
- generalizacion incierta a otros edificios;
- inconsistencia documental en la ficha editorial sobre el uso de datos.

Pregunta clave:

- cuanto de la mejora proviene del modelo y cuanto del filtrado y la construccion del fingerprint.

## Diapositiva 12 - Conclusiones

- BLE mas fingerprinting mas redes neuronales mejora la localizacion indoor.
- `M4` es mejor con valores vacios.
- `M2` es el modelo mas estable.
- El mayor aporte del paper es el pipeline completo, no solo una arquitectura.
- Para la Parte II del laboratorio, `M2` es el mejor candidato para reproducir.

## Mensaje final para la exposicion

Este paper fue una buena eleccion porque:

- trata un problema real de telecomunicaciones;
- aplica inteligencia artificial de forma concreta;
- reporta resultados cuantitativos comparables;
- y permite pasar naturalmente a la reproduccion experimental del laboratorio.

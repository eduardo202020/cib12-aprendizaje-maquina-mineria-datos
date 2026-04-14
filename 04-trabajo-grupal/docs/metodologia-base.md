# Metodologia Base del Proyecto

## Enfoque

La investigacion se plantea con enfoque cuantitativo porque busca medir el desempeno de un modelo de aprendizaje profundo con mecanismos de atencion sobre datos de localizacion indoor y contrastarlo con metricas objetivas de calidad del servicio.

## Tipo y nivel

- Tipo: investigacion aplicada.
- Nivel: explicativo.

La finalidad no es solo describir el problema, sino proponer y evaluar una solucion basada en inteligencia artificial para un contexto concreto: museos y espacios culturales.

## Diseno

Se propone un diseno cuasi experimental con comparacion entre:

- un enfoque base o baseline de localizacion indoor;
- y un modelo propuesto con mecanismos de atencion.

## Unidad de analisis

- huellas de senal Wi-Fi/BLE;
- predicciones de posicion, sala o zona;
- eventos de activacion del servicio de guia virtual.

## Poblacion y muestra

Poblacion:

- registros de senales y observaciones de usuarios en espacios culturales con infraestructura Wi-Fi/BLE.

Muestra:

- dataset de fingerprints indoor separado en entrenamiento, validacion y prueba;
- escenarios con variacion temporal, heterogeneidad de dispositivos y cambios del entorno.

## Tecnicas e instrumentos de recoleccion

Tecnicas:

- captura de RSSI o fingerprints;
- organizacion de etiquetas por sala, zona o punto de referencia;
- registro de condiciones del entorno.

Instrumentos:

- smartphone o dispositivo de captura;
- puntos Wi-Fi/BLE;
- scripts de preprocesamiento;
- hojas de registro o archivos CSV/JSON.

## Tecnicas e instrumentos de procesamiento

Tecnicas:

- limpieza de datos;
- normalizacion o escalado;
- entrenamiento del modelo;
- evaluacion comparativa con metricas.

Instrumentos:

- Python;
- notebooks;
- librerias de machine learning o deep learning;
- tablas y graficos de resultados.

## Metricas sugeridas

- accuracy;
- precision, recall y F1-score;
- error promedio de localizacion;
- desviacion o estabilidad entre corridas;
- tasa de activacion contextual correcta del servicio.

## Estructura sugerida del articulo

1. Introduccion.
2. Antecedentes y marco teorico.
3. Metodologia.
4. Recoleccion de datos.
5. Experimentos.
6. Resultados y discusion.
7. Conclusiones.
8. Trabajos futuros.

## Siguiente paso recomendado

Convertir esta metodologia base en una version mas formal con:

- dataset especifico;
- baseline definido;
- arquitectura del modelo;
- protocolo experimental;
- tabla de variables, dimensiones e indicadores.

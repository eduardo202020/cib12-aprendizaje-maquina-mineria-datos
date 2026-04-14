# Parte II: Reproduccion Experimental del Paper

Este documento adapta la implementacion del Laboratorio 02 a las actividades pedidas en la **Parte II: Reproduccion Experimental del Paper**.

El objetivo no es proponer un metodo nuevo, sino **reproducir de forma defendible** la metodologia central del paper:

*Bluetooth low energy indoor positioning: A fingerprinting neural network approach*.

## 1. Paper a reproducir

- **Titulo**: *Bluetooth low energy indoor positioning: A fingerprinting neural network approach*
- **Autores**: Alberto Ferrero-Lopez, Antonio Javier Gallego, Miguel Angel Lozano
- **Revista**: *Internet of Things*
- **Ano**: 2025
- **DOI**: `10.1016/j.iot.2025.101565`

## 2. Objetivo de la Parte II

Reproducir experimentalmente el pipeline principal del paper usando:

- el dataset BLE RSSI publico,
- la libreria de captura y filtrado liberada por los autores,
- la libreria de modelos neuronales del paper,
- y una comparacion cuantitativa entre mis resultados y los resultados reportados en el articulo.

## 3. Alcance de la reproduccion

La reproduccion se centrara en el modelo **M2**, porque:

- es el modelo mas estable entre escenarios segun el paper,
- tiene soporte mas claro en el repositorio publico,
- y permite cumplir la reproduccion experimental sin empezar por la variante mas compleja.

Como extension opcional, se puede incluir **M4** en el escenario con valores vacios.

## 4. Actividades de la Parte II

La Parte II se organiza en tres actividades principales:

1. reproducir el experimento del paper,
2. documentar el proceso de implementacion y ejecucion,
3. comparar criticamente los resultados obtenidos con los del articulo.

---

## Actividad 1. Reproduccion del experimento

### 1.1 Que se va a reproducir

Se reproducira el siguiente flujo experimental:

1. obtener el dataset BLE RSSI,
2. generar fingerprints a partir de las lecturas RSSI,
3. preparar dos variantes del dataset:
   - `with_empty_values`
   - `without_empty_values`
4. entrenar el modelo **M2**,
5. evaluar sobre trayectorias reales usando distancia euclidiana,
6. comparar con los valores del paper.

### 1.2 Recursos necesarios

Para esta reproduccion se usarán tres recursos principales:

- **Paper original**
- **Repositorio de modelos**
  `models_fingerprint_positioning`
- **Repositorio de captura y filtrado**
  `rssi_capturing_filtering_library`
- **Dataset**
  `Position-Annotated-BLE-RSSI-Dataset`

### 1.3 Dataset a utilizar

Del dataset publico se usarán estas carpetas:

- `hst/`: datos estacionarios para la fase **offline**
- `trk/`: trayectorias reales para la fase **online**
- `cnf/`: archivos de configuracion del entorno y sensores

### 1.4 Interpretacion metodologica

La logica experimental del paper distingue dos fases:

- **Fase offline**:
  se construyen fingerprints en posiciones conocidas y se entrena el modelo.
- **Fase online**:
  se prueba el modelo con trayectorias reales no vistas durante el entrenamiento.

### 1.5 Parametros que deben respetarse

Para la generacion de fingerprints y el entrenamiento se respetaran los parametros reportados por el paper:

- `Sreads_min = 2`
- `Svalid_min = 10` para `with_empty_values`
- `Svalid_min = 12` para `without_empty_values`
- filtro `Max`
- `omega_min = 0.5 s`
- `omega_max = 2.5 s`
- valor invalido por sensor: `100`

Para el entrenamiento de **M2**:

- perdida: `MSE`
- salida: lineal
- `batch_size = 256`
- hasta `1000` epocas
- `early stopping` con `delta = 0.0001`
- `patience = 10`
- optimizador:
  - `Adam, 0.0001` con vacios
  - `Adam, 0.001` sin vacios

### 1.6 Preprocesamiento

El preprocesamiento a reproducir es:

- estandarizacion de RSSI con `(x - mu) / sigma`,
- escalado min-max de coordenadas `(x, y)`,
- generacion de fingerprints con el mismo orden fijo de sensores,
- uso del valor `100` como marcador de dato faltante.

### 1.7 Implementacion practica

La implementacion debe seguir este orden:

#### Paso 1. Preparar el entorno

- clonar los repositorios,
- crear un entorno virtual,
- instalar dependencias,
- verificar versiones.

#### Paso 2. Preparar estructura de trabajo

La carpeta `Part-02` queda organizada asi:

- `datos/`: dataset crudo o procesado
- `src/`: scripts de procesamiento, entrenamiento y evaluacion
- `notebooks/`: exploracion o pruebas
- `resultados/`: metricas, modelos, figuras y evidencias

#### Paso 3. Construir fingerprints

- leer sensores desde `cnf/`,
- procesar archivos de `hst/`,
- aplicar ventana temporal y filtrado,
- exportar fingerprints para ambas variantes.

#### Paso 4. Entrenar M2

- usar la libreria publica de modelos,
- entrenar con `with_empty_values`,
- entrenar con `without_empty_values`,
- guardar modelo, escaladores y metricas.

#### Paso 5. Evaluar con trayectorias reales

- usar `trk/` como fase online,
- generar fingerprints de prueba con la misma logica,
- comparar coordenadas reales y predichas,
- calcular distancia euclidiana.

### 1.8 Resultado esperado de la actividad

Al finalizar esta actividad se debe tener:

- el dataset procesado,
- fingerprints generados,
- modelo M2 entrenado,
- resultados numericos de evaluacion,
- archivos de salida como `model.keras`, `scaler.pkl` y `score.json`.

---

## Actividad 2. Documentacion del proceso de implementacion

### 2.1 Que se debe documentar

La guia exige dejar evidencia clara de como se hizo la reproduccion.  
Por eso se debe documentar:

- el entorno usado,
- las librerias instaladas,
- los comandos ejecutados,
- la estructura del proyecto,
- los scripts usados,
- y los resultados obtenidos.

### 2.2 Evidencias minimas a conservar

- version de Python
- `pip freeze`
- comandos de instalacion
- captura de clonado o descarga del dataset
- scripts de procesamiento
- scripts de entrenamiento
- logs de entrenamiento
- salida de `score.json`
- archivo `model.keras`
- archivo `scaler.pkl`
- tablas o figuras de resultados

### 2.3 Texto base para el informe

Se reprodujo el pipeline experimental del articulo utilizando el dataset publico `Position-Annotated-BLE-RSSI-Dataset`, junto con la libreria de captura y filtrado de RSSI y la libreria publica de modelos neuronales liberadas por los autores. Se generaron dos variantes del dataset filtrado, con y sin valores vacios, respetando los parametros reportados en el paper. Posteriormente, se entreno el modelo M2 y se evaluo su precision sobre trayectorias reales mediante distancia euclidiana en el plano `(x, y)`.

### 2.4 Entregables de esta actividad

Esta actividad debe dejar:

- documentacion tecnica de la reproduccion,
- scripts organizados,
- trazabilidad del pipeline,
- y evidencias suficientes para sustentar el trabajo.

---

## Actividad 3. Analisis comparativo con el paper

### 3.1 Que se debe comparar

La comparacion no debe quedarse en “el modelo funciono”, sino que debe contrastar directamente:

- mis metricas de error,
- las metricas reportadas por el paper,
- y las posibles causas de diferencia.

### 3.2 Resultados de referencia del paper para M2

#### Escenario con valores vacios

- media: `2.0368 m`
- mediana: `1.8199 m`

#### Escenario sin valores vacios

- media: `2.0559 m`
- mediana: `1.7745 m`

### 3.3 Referencias contextuales del paper

- trilateracion con vacios: `3.7252 m`
- trilateracion sin vacios: `3.3583 m`
- estado del arte previo: media `3.064 m`, mediana `2.223 m`

### 3.4 Formato sugerido de comparacion

#### with_empty_values

- Paper M2: mean `2.0368`, median `1.8199`
- Mi reproduccion M2: mean `2.3690`, median `2.1413`
- Diferencia absoluta: mean `0.3322`, median `0.3214`
- Diferencia porcentual: mean `16.31%`, median `17.66%`
- Mejor corrida exploratoria: mean `2.3169`, median `1.9804`
- Mejor diferencia absoluta: mean `0.2801`, median `0.1605`
- Mejor diferencia porcentual: mean `13.75%`, median `8.82%`

#### without_empty_values

- Paper M2: mean `2.0559`, median `1.7745`
- Mi reproduccion M2: mean `2.0750`, median `1.8430`
- Diferencia absoluta: mean `0.0191`, median `0.0685`
- Diferencia porcentual: mean `0.93%`, median `3.86%`

### 3.5 Reflexion critica esperada

La reproduccion se considerara exitosa si:

- mantiene la misma logica metodologica del paper,
- usa parametros consistentes con el articulo,
- y produce errores del mismo orden de magnitud.

Si existen diferencias, se deben discutir causas posibles como:

- diferencias en el procesamiento final del CSV,
- variacion del subconjunto offline,
- semillas aleatorias,
- versiones de librerias,
- o falta de especificacion completa de artefactos intermedios.

---

## 5. Entregables finales de la Parte II

La Parte II debe culminar con estos productos:

### Informe tecnico

Debe incluir:

1. introduccion
2. paper reproducido
3. metodologia reproducida
4. implementacion
5. resultados propios
6. comparacion con el paper
7. discusion
8. conclusiones

### Codigo

Debe incluir como minimo:

- script de generacion de fingerprints
- script de entrenamiento de M2
- script de evaluacion
- README con instrucciones de ejecucion

### Evidencia

- logs
- metricas
- modelos guardados
- tablas
- figuras
- capturas o pruebas del proceso

### Estado actual de ejecucion

La ejecucion ya se realizo con un entorno local compatible basado en `Python 3.11` y `TensorFlow 2.15.1`.

Se completaron estas fases:

- generacion de fingerprints offline y online,
- entrenamiento de `M2` con `with_empty_values`,
- entrenamiento de `M2` con `without_empty_values`,
- evaluacion online de ambas variantes.

Artefactos generados:

- modelos en `resultados/experimentos/M2/...`
- metricas en `resultados/comparativas/metricas/M2/...`
- entorno local en `.venv311`

---

## 6. Verificacion metodologica

Para dejar clara la validez de la reproduccion, se puede afirmar:

- si se replico el uso de BLE RSSI con fingerprinting y redes neuronales,
- si se uso la separacion offline y online,
- si se respetaron los parametros de filtrado del paper,
- si se utilizo la distancia euclidiana como metrica final,
- y si el resultado final es comparable con el articulo.

Tambien debe declararse una limitacion importante:

- la ficha editorial del articulo indica “No data was used”, pero el propio paper si describe un dataset publico y repositorios asociados. Esto debe mencionarse como una limitacion de trazabilidad documental y no como un error de implementacion.

## 7. Resultados obtenidos en esta reproduccion

### Variante with_empty_values

- media: `2.3690 m`
- mediana: `2.1413 m`
- minimo: `0.0743 m`
- maximo: `15.9757 m`

Comparacion con el paper:

- paper: media `2.0368 m`, mediana `1.8199 m`
- reproduccion: media `2.3690 m`, mediana `2.1413 m`

Mejor corrida exploratoria:

- etiqueta: `with_empty_values_seed21`
- media: `2.3169 m`
- mediana: `1.9804 m`
- minimo: `0.1214 m`
- maximo: `16.1974 m`

### Variante without_empty_values

- media: `2.0750 m`
- mediana: `1.8430 m`
- minimo: `0.0517 m`
- maximo: `8.1161 m`

Comparacion con el paper:

- paper: media `2.0559 m`, mediana `1.7745 m`
- reproduccion: media `2.0750 m`, mediana `1.8430 m`

### Interpretacion

La reproduccion de `without_empty_values` quedo muy cercana a los valores del paper, lo que respalda que el pipeline general es consistente.

La reproduccion base de `with_empty_values` quedo algo por encima de lo reportado. Sin embargo, una exploracion controlada de semillas mejoro ese escenario hasta `2.3169 m` de media y `1.9804 m` de mediana, lo que muestra sensibilidad del entrenamiento a la inicializacion. Aun asi, la brecha con el paper sigue siendo visible, lo cual sugiere diferencias posibles en:

- el preprocesamiento exacto,
- la construccion de ventanas,
- la seleccion final de fingerprints,
- la inicializacion aleatoria del modelo,
- o detalles no completamente especificados por los autores.

---

## 8. Recomendacion practica de ejecucion

Para resolver correctamente la Parte II:

- hacer **M2** como reproduccion obligatoria,
- dejar **M4** como extension opcional,
- no empezar por modelos mas complejos como M8,
- no rehacer AutoML completo en esta primera iteracion.

## 9. Conclusion operativa

La mejor forma de cumplir la Parte II del laboratorio es reproducir el pipeline central del paper de forma ordenada y justificable:

- preparar el dataset,
- generar fingerprints,
- entrenar M2,
- evaluar con trayectorias reales,
- documentar todo,
- y comparar cuantitativamente con los resultados publicados.

Con esto, la Parte II queda alineada con la guia del laboratorio y lista para pasar a la fase de implementacion real en `src/`, `datos/` y `resultados/`.

Sí. Te lo dejo **aterrizado a tu guía** y **listo para ejecutar** con el paper de Ferrero-López y sus repositorios.

Tu guía pide dos cosas:
**Parte I**: seleccionar, analizar y presentar un paper científico de IA aplicada a telecomunicaciones.
**Parte II**: reproducir experimentalmente lo descrito en el paper, documentarlo, compararlo con el original y entregar informe, código y evidencia. Eso está explícito en tu PDF de laboratorio.  

## 1) Paper elegido y por qué sí sirve

**Paper**: *Bluetooth low energy indoor positioning: A fingerprinting neural network approach*
**Autores**: Alberto Ferrero-López, Antonio Javier Gallego, Miguel Angel Lozano
**Journal**: *Internet of Things*
**Año**: 2025
**DOI**: 10.1016/j.iot.2025.101565
**Estado**: open access bajo licencia Creative Commons en ScienceDirect. ([ScienceDirect][1])

Sí encaja con tu curso porque estudia **IA aplicada a telecomunicaciones** usando **BLE, RSSI, fingerprinting y redes neuronales** para localización indoor. Además, compara varios modelos, define parámetros experimentales, usa dataset público y libera código en GitHub, lo cual lo hace mucho más útil para la **Parte II** de reproducción.   ([ScienceDirect][1])

## 2) Lo que debes decir en la **Parte I** del laboratorio

### Problema de investigación

El paper busca resolver la baja precisión de la localización indoor usando BLE cuando se trabaja con señales RSSI ruidosas, atenuadas y con multipath. Los autores sostienen que no basta con entrenar una red; también hay que **capturar, filtrar y estructurar bien la señal** antes de predecir posición. 

### Objetivo del paper

Analizar una metodología completa de posicionamiento indoor basada en BLE que combine:

1. captura y filtrado de RSSI para formar fingerprints,
2. comparación de ocho diseños de redes neuronales y trilateración,
3. evaluación en trayectorias reales,
4. análisis de qué tan bien reflejan las métricas de entrenamiento el desempeño real. 

### Hipótesis

El paper **no formula una hipótesis explícita en una frase formal**, así que en tu exposición conviene decirlo así:
“**Hipótesis inferida**: un pipeline de captura/filtrado de RSSI más redes neuronales de fingerprinting puede superar a la trilateración clásica y a métodos previos del estado del arte en error medio de localización indoor.” Esa inferencia está respaldada por el resumen, los objetivos y los resultados reportados.  ([ScienceDirect][1])

### Antecedentes

Los autores organizan los antecedentes en tres grupos:

* métodos probabilísticos de fingerprinting,
* redes neuronales para fingerprinting,
* trilateración con BLE RSSI.
  Critican que varios trabajos previos no detallan bien captura, preprocesamiento o evaluación real, y remarcan que **loss/accuracy** de entrenamiento no siempre representan el rendimiento online real. 

### Metodología

La metodología tiene **dos fases**:

**Fase 1: Captura y filtrado de RSSI**
Se reciben señales BLE desde un beacon hacia varios sensores; se almacenan en una ventana temporal; luego se decide cuándo cerrar la ventana y se genera un fingerprint con un valor por sensor. Si un sensor no cumple el mínimo de lecturas, se le asigna el valor **100** como marcador de dato vacío. 

**Fase 2: Localización indoor**
Ese fingerprint alimenta el algoritmo de localización:

* modelos de **regresión** para predecir coordenadas (x,y),
* modelos de **clasificación** por celdas,
* y **trilateración** como baseline. 

### Dataset usado

Usan el **Position-Annotated-BLE-RSSI-Dataset**, con una sala de **20.66 × 17.64 m**, **12 sensores BLE** y un beacon. La verdad-terreno se obtuvo con cámaras y etiquetas ArUco, con precisión alrededor de **0.05 m**. El dataset tiene fase offline con puntos de referencia y fase online con trayectorias reales. El entrenamiento usa la malla **9×9** de la fase offline y la evaluación se hace con las trayectorias online; además, hacen partición **80/20** entre entrenamiento y validación.  ([GitHub][2])

### Modelos comparados

Comparan 8 modelos:

* **M1** baseline,
* **M2** densa más profunda,
* **M3** y **M4** con máscara de valores vacíos,
* **M5** CNN 1D,
* **M6**, **M7**, **M8** como clasificación por grillas,
* además de **trilateración**.
  Las arquitecturas están especificadas en la tabla del paper. 

### Resultados clave

Con dataset **con valores vacíos permitidos**, el mejor resultado medio fue **M4 = 1.8957 m**, seguido por **M2 = 2.0368 m**; trilateración quedó en **3.7252 m** y el estado del arte citado en **3.064 m** de media. 

Con dataset **sin valores vacíos**, los autores resumen que **M5 y M2** son preferibles; en la tabla visible, **M2 = 2.0559 m**, **M5 = 2.0766 m**, **M4 = 2.1137 m**, mientras trilateración queda en **3.3583 m** y el estado del arte en **3.064 m** de media.  

La conclusión fuerte del paper es:

* **M4** es mejor cuando hay datos vacíos o ruido,
* **M2** es el más estable entre escenarios,
* los modelos de **regresión** superan en general a los de clasificación,
* y las métricas de entrenamiento **no garantizan** el mejor rendimiento real.  

## 3) Qué presentar en tus diapositivas de 15 minutos

Hazlo así y ya queda alineado con tu guía. 

**Diapositiva 1**
Título del paper, autores, journal, año, DOI, por qué lo elegiste. ([ScienceDirect][1])

**Diapositiva 2**
Problema: GPS falla indoors; BLE RSSI sirve, pero sufre ruido, atenuación y multipath. 

**Diapositiva 3**
Concepto de fingerprinting: fase offline y fase online. 

**Diapositiva 4**
Metodología general: captura/filtrado + localización. Usa el diagrama del paper como guía conceptual. 

**Diapositiva 5**
Dataset y setup experimental: sala, 12 sensores, beacon, verdad-terreno por visión, 9×9 offline y trayectorias online.  ([GitHub][2])

**Diapositiva 6**
Parámetros del filtrado:
(Sreads_min = 2), (Svalid_min = 10) o (12), filtro **Max**, (\omega_{min}=0.5) s, (\omega_{max}=2.5) s. 

**Diapositiva 7**
Arquitecturas M1–M8 y diferencia entre regresión y clasificación. 

**Diapositiva 8**
Entrenamiento: batch 256, hasta 1000 épocas, early stopping; MSE para regresión y cross-entropy para clasificación.  

**Diapositiva 9**
Resultados con valores vacíos: destaca M4 y M2 frente a trilateración y estado del arte. 

**Diapositiva 10**
Resultados sin valores vacíos: destaca M2/M5 y la estabilidad de M2.  

**Diapositiva 11**
Discusión: por qué la máscara ayuda cuando faltan lecturas y por qué accuracy no basta como métrica.  

**Diapositiva 12**
Conclusiones, limitaciones y propuesta de tu reproducción experimental.  

## 4) Preguntas críticas para tu análisis en NotebookLM

Puedes llevar estas ya preparadas:

1. ¿Qué tanto dependen los resultados del dataset específico usado?
2. ¿Qué pasa si el entorno cambia respecto al entrenamiento?
3. ¿Por qué el paper dice “No data was used” si sí usa un dataset público?
4. ¿Cuánto impacta usar 10 vs 12 sensores válidos?
5. ¿La mejora viene más del filtrado o del modelo neuronal?
6. ¿Qué tan sensible es M2 a semillas aleatorias y al split 80/20?
7. ¿Los resultados son reproducibles sin los mismos archivos preprocesados?
8. ¿Accuracy es una mala métrica para clasificación espacial? ¿por qué?
9. ¿M4 realmente compensa su mayor costo computacional?
10. ¿La trilateración quedó mal por el modelo físico RSSI→distancia o por la calidad de la señal?
11. ¿El enfoque serviría igual en museos, aeropuertos o fábricas?
12. ¿Qué falta para desplegarlo en tiempo real con beacons reales?
    Estas preguntas salen directamente de las limitaciones y discusión del paper.  

## 5) Lo que ya tienes disponible para la **Parte II**

Tienes tres piezas públicas clave:

**El paper abierto** en ScienceDirect. ([ScienceDirect][1])

**El repo de modelos** `models_fingerprint_positioning`, que contiene los modelos **M1–M8**, clases de entrenamiento y un ejemplo de uso para entrenar modelos como M2, guardando modelo y `score.json`. El README deja claro que asume que el dataset ya está preparado en rutas locales. ([GitHub][3])

**El repo de captura/filtrado** `rssi_capturing_filtering_library`, que implementa la ventana temporal, filtros como mean/median/max/min/TSS y generación de fingerprints. ([GitHub][4])

Además, el dataset público existe en GitHub/Kaggle como **Position-Annotated-BLE-RSSI-Dataset**. ([GitHub][2])

## 6) La mejor estrategia para reproducirlo

Para tu laboratorio, la ruta más sólida es esta:

### Alcance mínimo viable

Reproducir **M2** sobre:

* dataset filtrado **con valores vacíos**,
* dataset filtrado **sin valores vacíos**,
  y comparar con los resultados del paper.
  Esto es lo más sensato porque **M2 es el más estable** entre escenarios y el propio README del repo muestra un ejemplo de entrenamiento con **M2**.   ([GitHub][3])

### Alcance ideal para sacar mejor nota

Además de M2, reproducir **M4** en el caso con valores vacíos, porque es el mejor modelo en ese escenario. Así tendrás una comparación más rica y más cercana a la discusión del paper.  

## 7) Reproducción experimental: pipeline exacto

### Paso 1. Dataset

Descarga el **Position-Annotated-BLE-RSSI-Dataset**. Usa:

* la malla **9×9 offline** para entrenamiento,
* las **trayectorias online** para prueba,
* y divide entrenamiento/validación en **80/20**.  ([GitHub][2])

### Paso 2. Generación de fingerprints

Usa el repo `rssi_capturing_filtering_library` para procesar las lecturas RSSI en ventanas temporales y convertirlas en fingerprints. El repo implementa justo esa lógica y ofrece ejemplo de uso con `SignalCaptureWindow`. ([GitHub][4])

### Paso 3. Parámetros que debes respetar

Usa estos parámetros del paper:

* `Sreads_min = 2`
* `Svalid_min = 10` para dataset **con vacíos**
* `Svalid_min = 12` para dataset **sin vacíos**
* filtro = **Max**
* `omega_min = 0.5 s`
* `omega_max = 2.5 s`
* valor inválido = **100** 

### Paso 4. Preprocesamiento

* Normaliza RSSI con **estandarización** ((x-\mu)/\sigma).
* Para regresión, reescala coordenadas (x,y) con min-max usando:

  * (x \in [0, 20.66])
  * (y \in [0, 17.64])  

### Paso 5. Entrenamiento

Para reproducir **M2**:

* modelo de **regresión**
* pérdida: **MSE**
* salida: activación lineal
* batch size: **256**
* hasta **1000 épocas**
* early stopping con (\delta = 0.0001) y paciencia de **10** épocas
* optimizador/lr:

  * con vacíos: **Adam, 0.0001**
  * sin vacíos: **Adam, 0.001**  

Para **M4**:

* también es de regresión
* optimizador/lr: **Adam, 0.001** en ambos escenarios. 

### Paso 6. Evaluación

Evalúa en las trayectorias online usando **distancia euclidiana** entre posición real y predicha. Reporta mínimo, máximo, media, mediana y cuartiles. Eso es exactamente lo que hace el paper. 

## 8) Qué resultados deberías esperar

Si tu reproducción sale razonablemente bien, deberías acercarte a esto:

### Dataset con vacíos

* Trilateración: media **3.7252 m**
* Estado del arte [15]: media **3.064 m**, mediana **2.223 m**
* **M2**: media **2.0368 m**, mediana **1.8199 m**
* **M4**: media **1.8957 m**, mediana **1.5521 m** 

### Dataset sin vacíos

* Trilateración: media **3.3583 m**
* Estado del arte [15]: media **3.064 m**, mediana **2.223 m**
* **M2**: media **2.0559 m**, mediana **1.7745 m**
* **M4**: media **2.1137 m**, mediana **1.9828 m**
* **M5**: media **2.0766 m**, mediana **2.0344 m** 

Tu análisis comparativo debe enfatizar que:

* con vacíos, **M4** es mejor;
* sin vacíos, **M2/M5** son preferibles;
* y **M2** es el más estable entre escenarios.  

## 9) Lo más importante: la inconsistencia que debes explicar en tu informe

La ficha del artículo en ScienceDirect muestra en “Data availability” la frase **“No data was used for the research described in the article.”** Pero el propio paper describe explícitamente el uso del **Position-Annotated-BLE-RSSI-Dataset**, y además existen el repo del dataset y los repos de los autores. En tu informe conviene decirlo como una **limitación de reproducibilidad documental**. ([ScienceDirect][1])

Puedes redactarlo así:

> “Aunque la ficha editorial del artículo indica que no se usaron datos, el contenido metodológico del paper sí especifica el uso del Position-Annotated-BLE-RSSI-Dataset y los autores publican repositorios asociados. Por ello, la reproducción se realizó a partir del dataset público y del código abierto disponible, asumiendo este conjunto como la referencia experimental efectiva.”

## 10) Qué debes entregar para cumplir la **Parte II**

Tu guía pide: informe técnico, código y evidencia. 

Déjalo así:

### Informe técnico (2–8 páginas)

1. **Introducción**
   Problema de localización indoor con BLE RSSI.
2. **Paper reproducido**
   Cita APA completa, objetivo y aportes.
3. **Metodología reproducida**
   Dataset, filtrado, modelos, preprocesamiento, entrenamiento, evaluación.
4. **Implementación**
   Entorno, librerías, estructura del repo, scripts ejecutados.
5. **Resultados propios**
   Tabla con media, mediana, min, max y cuartiles.
6. **Comparación con el paper**
   Diferencias absolutas y porcentuales.
7. **Discusión**
   Posibles causas de discrepancia.
8. **Conclusiones**
   Qué sí pudiste reproducir y qué no. 

### Código

Sube a GitHub o Colab:

* script de generación de fingerprints,
* script de entrenamiento M2,
* script de entrenamiento M4 si lo haces,
* script de evaluación,
* README con pasos exactos. 

### Evidencia

Adjunta:

* captura de descarga del dataset,
* captura del entorno instalado,
* logs de entrenamiento,
* salida de `score.json`,
* archivo del modelo entrenado,
* tabla/figura de errores,
* boxplot si puedes replicarlo,
* captura del commit final del repo. 

## 11) Verificación metodológica, ya lista para escribir

Para la sección “verificación” de tu guía, puedes poner esto:

* **Sí se replicó** el uso de BLE RSSI + fingerprinting + redes neuronales. 
* **Sí se respetó** el dataset base, la separación offline/online y el split 80/20. 
* **Sí se respetaron** los parámetros óptimos del filtrado: 2, 10/12, Max, 0.5 s y 2.5 s. 
* **Sí se respetó** el tipo de pérdida y esquema de entrenamiento para regresión. 
* **Sí se usó** la métrica de distancia euclidiana para la comparación final. 
* **No puede garantizarse** réplica 1:1, porque el paper y la ficha editorial no dejan completamente cerrada la trazabilidad de los datos ya preprocesados y de todos los artefactos intermedios. ([ScienceDirect][1])

## 12) Recomendación final de trabajo

Para no complicarte y cumplir bien:

**Haz M2 obligatorio**
y, si te da tiempo,
**añade M4 como extensión**.

Con eso tu laboratorio queda fuerte porque:

* M2 está mejor soportado por el repo de entrenamiento,
* M2 es el más estable según el paper,
* M4 te da el mejor caso con vacíos y mejora tu análisis comparativo.   ([GitHub][3])

En el siguiente mensaje te puedo dejar **redactado completo** el contenido de tu **informe técnico** y también el **guion exacto de tus 12 diapositivas**.

[1]: https://www.sciencedirect.com/science/article/pii/S2542660525000782 "Bluetooth low energy indoor positioning: A fingerprinting neural network approach - ScienceDirect"
[2]: https://github.com/philotuxo/Position-Annotated-BLE-RSSI-Dataset "GitHub - philotuxo/Position-Annotated-BLE-RSSI-Dataset: Position Annotated BLE RSSI dataset for indoor localization · GitHub"
[3]: https://github.com/bertoferrero-research/models_fingerprint_positioning "GitHub - bertoferrero-research/models_fingerprint_positioning: Library collection of RSSI fingerprint neural models · GitHub"
[4]: https://github.com/bertoferrero-research/rssi_capturing_filtering_library "GitHub - bertoferrero-research/rssi_capturing_filtering_library: Rssi signal filtering and fingerprint generator library · GitHub"

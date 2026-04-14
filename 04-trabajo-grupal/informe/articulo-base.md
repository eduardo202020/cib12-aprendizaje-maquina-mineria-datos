# Articulo Base

## Titulo tentativo

Modelo de aprendizaje profundo con mecanismos de atencion para mejorar la calidad del servicio de guia virtual con aplicaciones moviles e IoT con senales Wi-Fi/BLE en museos y espacios culturales, 2026

## Resumen

La localizacion indoor basada en senales Wi-Fi/BLE es un componente clave para ofrecer servicios de guia virtual contextualizados en museos y espacios culturales. Sin embargo, factores como la inestabilidad del RSSI, el efecto multipath, la heterogeneidad de dispositivos y las variaciones temporales del entorno reducen la precision de los sistemas convencionales y afectan la activacion oportuna de contenidos para el visitante. En este trabajo se propone evaluar un modelo de aprendizaje profundo con mecanismos de atencion para mejorar la robustez y precision de la localizacion indoor. La investigacion se plantea con enfoque cuantitativo y diseno cuasi experimental, comparando el modelo propuesto con enfoques base sobre datos de fingerprints Wi-Fi/BLE. Se espera que la mejora en precision de localizacion incremente la calidad del servicio de guia virtual en terminos de activacion correcta, pertinencia contextual y continuidad de la experiencia del usuario.

## Palabras clave

localizacion indoor, Wi-Fi fingerprinting, BLE, mecanismos de atencion, aprendizaje profundo, guia virtual, museos inteligentes

## 1. Introduccion

Los museos y espacios culturales buscan incorporar tecnologias digitales que enriquezcan la experiencia del visitante mediante servicios de guia virtual, contenidos contextuales y recorridos personalizados. En este escenario, la localizacion indoor basada en dispositivos moviles y senales inalambricas representa una alternativa viable para identificar la posicion aproximada del usuario y activar informacion relevante segun su ubicacion.

No obstante, el despliegue real de estos sistemas presenta limitaciones importantes. La intensidad de senal recibida puede variar por interferencias, obstaculos fisicos, reflexiones multipath, orientacion del dispositivo y diferencias de hardware entre telefonos. Estas condiciones dificultan la identificacion confiable de la sala, zona u objeto cercano al visitante, lo que reduce la calidad del servicio de guia virtual y afecta la experiencia general del recorrido.

En los ultimos anos, diversos trabajos han explorado el uso de modelos de machine learning y deep learning para mejorar la localizacion indoor. En particular, los mecanismos de atencion han mostrado potencial para manejar dependencias relevantes dentro de las senales observadas y mejorar la robustez frente a heterogeneidad y variaciones temporales. A partir de ello, este trabajo plantea evaluar un modelo de aprendizaje profundo con mecanismos de atencion orientado a mejorar la calidad del servicio de guia virtual en museos y espacios culturales.

## 2. Problema de investigacion

### 2.1 Problema general

¿Como mejorar la calidad del servicio de guia virtual en museos y espacios culturales mediante un modelo de aprendizaje profundo con mecanismos de atencion aplicado a senales Wi-Fi/BLE para localizacion indoor durante 2026?

### 2.2 Problemas especificos

1. ¿De que manera la variabilidad del RSSI, el multipath y la heterogeneidad de dispositivos afectan la precision de localizacion indoor en servicios de guia virtual?
2. ¿En que medida un modelo de aprendizaje profundo con mecanismos de atencion puede mejorar la precision de localizacion indoor frente a enfoques base?
3. ¿Como impacta la mejora de la precision de localizacion indoor en la calidad del servicio de guia virtual para el visitante?

## 3. Objetivos

### 3.1 Objetivo general

Mejorar la calidad del servicio de guia virtual en museos y espacios culturales mediante un modelo de aprendizaje profundo con mecanismos de atencion aplicado a senales Wi-Fi/BLE para localizacion indoor.

### 3.2 Objetivos especificos

1. Analizar el efecto de la variabilidad del RSSI, el multipath y la heterogeneidad de dispositivos sobre la precision de localizacion indoor.
2. Disenar e implementar un modelo de aprendizaje profundo con mecanismos de atencion para estimar la ubicacion indoor a partir de huellas Wi-Fi/BLE.
3. Evaluar el impacto del modelo propuesto sobre indicadores de calidad del servicio de guia virtual.

## 4. Hipotesis

### 4.1 Hipotesis general

La aplicacion de un modelo de aprendizaje profundo con mecanismos de atencion mejora significativamente la calidad del servicio de guia virtual en museos y espacios culturales al incrementar la precision y robustez de la localizacion indoor basada en senales Wi-Fi/BLE.

### 4.2 Hipotesis especificas

1. La variabilidad del RSSI, el multipath y la heterogeneidad de dispositivos reducen significativamente la precision de los sistemas de localizacion indoor basados en Wi-Fi/BLE.
2. Un modelo de aprendizaje profundo con mecanismos de atencion obtiene mejor desempeno que enfoques base al estimar la ubicacion indoor.
3. Una mayor precision de localizacion indoor mejora la activacion contextual y la oportunidad del servicio de guia virtual.

## 5. Antecedentes

Los antecedentes revisados muestran una evolucion desde enfoques clasicos de fingerprinting y aprendizaje supervisado hacia arquitecturas profundas con mayor capacidad de generalizacion. Trabajos como los de Salamah et al. y Zhang et al. evidencian el interes temprano en la aplicacion de machine learning a la localizacion Wi-Fi en interiores. Estudios mas recientes, como Tiku et al., Gufran et al. y Singampalli et al., incorporan mecanismos de atencion, modelos invariantes al dispositivo y enfoques explicables para afrontar variaciones temporales y heterogeneidad de equipos.

Asimismo, investigaciones como las de Xu et al., Tsuchiya et al. y Yaman et al. reflejan una tendencia a integrar senales inalambricas con otras fuentes sensoriales para mejorar robustez y cobertura. En conjunto, estos trabajos sustentan la pertinencia del problema y respaldan la exploracion de modelos profundos con atencion en escenarios donde la calidad del servicio depende de una localizacion indoor confiable.

## 6. Metodologia

La investigacion se desarrollara con enfoque cuantitativo, tipo aplicada y nivel explicativo. Se propone un diseno cuasi experimental en el que se comparara un modelo base de localizacion indoor con un modelo de aprendizaje profundo con mecanismos de atencion. La evaluacion se realizara sobre un conjunto de datos de fingerprints Wi-Fi/BLE, considerando escenarios con variaciones temporales, ruido e heterogeneidad de dispositivos.

Las etapas metodologicas seran:

1. recopilacion y organizacion de datos;
2. preprocesamiento y generacion de fingerprints;
3. definicion del baseline;
4. diseno e implementacion del modelo propuesto;
5. entrenamiento, validacion y prueba;
6. comparacion de metricas;
7. interpretacion del impacto sobre la calidad del servicio de guia virtual.

## 7. Variables

### 7.1 Variable independiente

Modelo de aprendizaje profundo con mecanismos de atencion.

### 7.2 Variable dependiente

Calidad del servicio de guia virtual.

## 8. Resultados esperados

Se espera demostrar que el modelo propuesto mejora la precision de localizacion indoor y reduce errores de identificacion de sala o zona frente a metodos base. Como consecuencia, se espera una activacion mas pertinente y oportuna de contenidos de guia virtual, contribuyendo a una mejor experiencia del visitante.

## 9. Estructura pendiente para completar

- marco teorico ampliado;
- descripcion detallada del dataset;
- definicion del baseline;
- arquitectura del modelo;
- resultados cuantitativos;
- discusion;
- conclusiones;
- trabajos futuros;
- referencias en formato de revista.

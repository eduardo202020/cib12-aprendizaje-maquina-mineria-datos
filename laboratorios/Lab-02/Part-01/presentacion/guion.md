# Guion de Sustentacion

## Objetivo del guion

Este guion esta pensado para ayudarte a exponer aunque no estes familiarizado con el tema.  
La idea es que no memorices palabra por palabra, sino que entiendas que significa cada termino y como explicarlo de forma simple.

## Recomendacion general para exponer

- Habla con calma y explica primero la idea simple, luego el termino tecnico.
- Cuando menciones una sigla, primero di su nombre y luego una explicacion corta.
- Si te preguntan algo tecnico, vuelve siempre a esta idea: el paper busca mejorar la localizacion en interiores usando mejor procesamiento de la senal y redes neuronales.

## Diapositiva 1. Portada

### Que decir

“Buenos dias. En esta exposicion presentare la Parte I de mi laboratorio, centrada en el paper titulado `Bluetooth low energy indoor positioning: A fingerprinting neural network approach`.

Este trabajo estudia como mejorar la localizacion de personas u objetos dentro de espacios cerrados usando senales Bluetooth y modelos de aprendizaje automatico.

Elegí este paper porque relaciona telecomunicaciones con inteligencia artificial, compara varios modelos y ademas publica codigo y repositorios, lo cual tambien ayuda para la siguiente parte del laboratorio, que es la reproduccion experimental.”

### Si te piden aclarar

- `Indoor positioning`: localizacion en interiores.
- `Aprendizaje automatico`: tecnicas que permiten a un sistema aprender patrones a partir de datos.

## Diapositiva 2. Referencia del paper

### Que decir

“El paper fue escrito por Alberto Ferrero-Lopez, Antonio Javier Gallego y Miguel Angel Lozano, y fue publicado en 2025 en la revista `Internet of Things`.

El tema principal es el posicionamiento indoor usando BLE, RSSI, fingerprinting y redes neuronales.

En palabras simples, el articulo intenta responder esta pregunta: como podemos estimar la ubicacion de un dispositivo dentro de un edificio usando senales inalambricas y modelos de inteligencia artificial.”

### Terminos clave

- `BLE` o `Bluetooth Low Energy`: una version de Bluetooth pensada para consumir poca energia. Se usa mucho en sensores, beacons y dispositivos pequenos.
- `RSSI`: significa `Received Signal Strength Indicator`. Es una medida de que tan fuerte llega una senal.
- `Red neuronal`: modelo de aprendizaje automatico inspirado de forma general en como procesamos informacion. Aprende relaciones entre entradas y salidas.

### Forma simple de explicarlo

“Si una senal llega muy fuerte, normalmente el dispositivo esta mas cerca. Si llega debil, probablemente esta mas lejos. Pero esto no es exacto porque en interiores hay paredes, rebotes e interferencias.”

## Diapositiva 3. Introduccion

### Que decir

“El problema principal es que el GPS funciona bien en exteriores, pero pierde precision dentro de edificios.

Esto ocurre porque la senal del GPS se debilita cuando atraviesa paredes, techos y otros obstaculos. Ademas, en ambientes cerrados la senal puede rebotar y distorsionarse.

Por eso se buscan alternativas para localizacion indoor, y una de ellas es usar BLE con mediciones RSSI.”

### Terminos clave

- `Atenuacion`: perdida de fuerza de la senal al atravesar objetos o distancia.
- `Obstaculos`: paredes, muebles, personas u otros elementos que afectan la senal.
- `Multitrayectoria` o `multipath`: cuando la senal rebota en superficies y llega por varios caminos distintos.

### Forma corta de decirlo

“El GPS no es confiable dentro de edificios, asi que este paper propone usar Bluetooth y aprendizaje automatico para mejorar la ubicacion.”

## Diapositiva 4. Antecedentes

### Que decir

“Los autores revisan tres enfoques principales usados antes de su propuesta.

El primero es el fingerprinting probabilistico, que compara patrones de senal usando modelos matematicos y probabilidades.

El segundo es el fingerprinting con redes neuronales, donde una red aprende a asociar patrones RSSI con posiciones.

El tercero es la trilateracion, que intenta calcular la posicion a partir de distancias estimadas desde varios sensores.

Los autores critican que muchos trabajos anteriores no explican bien como capturan la senal, como la filtran o como la evalúan en situaciones reales.”

### Terminos clave

- `Fingerprinting`: tecnica que usa una “huella” de senales del entorno.
- `Huella` o `fingerprint`: vector de valores RSSI observados en una posicion concreta.
- `Trilateracion`: metodo geometrico que estima una posicion usando distancias desde varios puntos conocidos.
- `Probabilistico`: enfoque basado en probabilidad y estimacion matematica.

### Analogía sencilla

“El fingerprinting funciona como reconocer un lugar por su patron de senales, igual que una huella digital reconoce a una persona.”

## Diapositiva 5. Objetivo e hipotesis inferida

### Que decir

“El objetivo del paper es analizar una metodologia completa para posicionamiento indoor usando BLE y fingerprinting.

No solo quieren probar una red neuronal, sino todo el proceso: como capturar la senal, como filtrarla, como representar los datos y que modelo predice mejor la posicion.

La hipotesis que se puede inferir del trabajo es que si se prepara bien la senal RSSI y se usa una red neuronal adecuada, se puede superar tanto a la trilateracion clasica como a metodos previos del estado del arte.”

### Terminos clave

- `Hipotesis inferida`: idea principal que se deduce del paper aunque no este escrita literalmente en una sola frase.
- `Estado del arte`: los mejores metodos publicados antes de este trabajo.

### Frase facil de recordar

“La idea central es que una buena preparacion de la senal mas una buena red neuronal puede dar mejores resultados que los metodos tradicionales.”

## Diapositiva 6. Metodos: pipeline propuesto

### Que decir

“La metodologia del paper tiene dos fases principales.

La primera fase es la captura y filtrado de senales BLE. Un beacon emite la senal, varios sensores la reciben y guardan sus lecturas RSSI dentro de una ventana temporal.

Una ventana temporal es simplemente un pequeno bloque de tiempo en el que se juntan varias mediciones recientes.

Despues esas lecturas se filtran, es decir, se procesan para reducir ruido e inconsistencias.

Con esas lecturas procesadas se construye un fingerprint, que es un vector con un valor por cada sensor.

La segunda fase es la prediccion de la ubicacion. Ese fingerprint se entrega a un modelo, que puede ser una red de regresion, una red de clasificacion o el metodo de trilateracion.”

### Terminos clave

- `Beacon`: dispositivo que emite la senal BLE.
- `Sensor`: dispositivo que recibe la senal.
- `Ventana temporal`: intervalo de tiempo donde se acumulan lecturas.
- `Filtrado`: proceso para suavizar o limpiar datos ruidosos.
- `Vector`: conjunto ordenado de valores numericos.

### Explicacion del valor 100

“Si un sensor no tiene suficientes lecturas, el paper coloca el valor 100 para indicar que ese dato esta vacio. No significa una senal fuerte; es solo una marca para decir ‘aqui falta informacion’.”

## Diapositiva 7. Metodos: datos y configuracion experimental

### Que decir

“Para entrenar y probar los modelos, los autores usan un dataset publico llamado `Position-Annotated-BLE-RSSI-Dataset`.

El entorno experimental es una sala de 20.66 por 17.64 metros, con 12 sensores BLE y un beacon.

La posicion real del beacon, lo que se llama `ground truth`, se obtiene mediante vision por computador y marcadores ArUco.

Eso significa que la ubicacion verdadera fue medida con un sistema externo mas preciso, para luego compararla con la prediccion del modelo.

El dataset tiene dos partes. La parte `offline` sirve para construir las huellas conocidas y entrenar. La parte `online` contiene trayectorias reales, y se usa para evaluar que tan bien funciona el modelo en situaciones mas cercanas a la realidad.”

### Terminos clave

- `Dataset`: conjunto de datos usado para entrenar y evaluar.
- `Ground truth`: valor real o referencia correcta.
- `Offline`: etapa previa de preparacion y entrenamiento.
- `Online`: etapa de uso real o prueba sobre datos nuevos.
- `Trayectoria`: recorrido real seguido por el dispositivo.

### Aclaracion sencilla

“Offline es cuando el sistema aprende. Online es cuando el sistema intenta ubicar algo que no vio antes.”

## Diapositiva 8. Metodos: modelos y parametros

### Que decir

“Los autores comparan varios modelos.

M1 es el modelo base.
M2 es una red densa mas profunda.
M3 y M4 agregan una mascara para manejar valores vacios.
M5 usa una CNN de una dimension.
M6, M7 y M8 son modelos de clasificacion por grillas.
Ademas, comparan todo esto con trilateracion.

Tambien analizan parametros importantes en la etapa de captura y filtrado, como el numero minimo de lecturas por sensor, el numero minimo de sensores validos y el tamano de la ventana temporal.”

### Terminos clave

- `Red densa`: red neuronal donde las neuronas de una capa se conectan con todas las de la siguiente.
- `Mascara`: informacion adicional que indica que entradas estan vacias o faltantes.
- `CNN 1D`: red convolucional de una dimension, util para detectar patrones locales en secuencias o vectores.
- `Clasificacion`: el modelo predice una categoria, por ejemplo una celda de una grilla.
- `Regresion`: el modelo predice un valor numerico continuo, por ejemplo coordenadas x e y.

### Diferencia facil entre regresion y clasificacion

“Si el modelo dice ‘estas en la celda 4’, eso es clasificacion.  
Si el modelo dice ‘estas en x igual a 8.2 y y igual a 3.5’, eso es regresion.”

## Diapositiva 9. Resultados principales

### Que decir

“En los resultados, los modelos de regresion fueron mejores que los de clasificacion.

Cuando el dataset permitia valores vacios, el mejor modelo fue M4 con un error medio de 1.8957 metros. Luego aparecio M2 con 2.0368 metros.

Cuando el dataset no tenia valores vacios, los mejores fueron M2 y M5, con errores medios cercanos a 2.06 metros.

En ambos casos, los modelos propuestos superaron claramente a la trilateracion, que tuvo errores mayores a 3.3 metros, y tambien mejoraron el estado del arte previo, que estaba alrededor de 3.064 metros.”

### Terminos clave

- `Error medio`: distancia promedio entre la posicion real y la predicha.
- `Metro de error`: cuanto se equivoca el sistema al estimar la ubicacion.

### Forma simple de explicarlo

“Mientras mas pequeno es el error medio, mejor ubica el sistema.”

## Diapositiva 10. Discusion

### Que decir

“En la discusion, los autores explican por que algunos modelos funcionan mejor que otros.

M2 mejora al modelo base M1 porque tiene una arquitectura mas profunda, es decir, puede aprender relaciones mas complejas dentro de la senal.

M3 y M4 funcionan mejor cuando hay datos faltantes porque usan una mascara que le indica al modelo donde falta informacion.

Otra conclusion importante es que las metricas de entrenamiento, como `loss` o `accuracy`, no siempre reflejan el rendimiento real del sistema.

Por eso los autores insisten en que no basta con entrenar bien el modelo; hay que evaluarlo en trayectorias reales.”

### Terminos clave

- `Loss`: medida del error interno del modelo durante el entrenamiento.
- `Accuracy`: porcentaje de aciertos, usado mucho en clasificacion.
- `Rendimiento real`: comportamiento del modelo sobre datos nuevos o situaciones practicas.

### Explicacion importante

“En localizacion, una clasificacion puede marcarse como incorrecta aunque haya fallado por poco. Por eso `accuracy` no siempre es una buena medida; la distancia euclidiana suele ser mas util.”

### Que es distancia euclidiana

“Es la distancia en linea recta entre la posicion real y la posicion predicha.”

## Diapositiva 11. Conclusiones

### Que decir

“Como conclusiones, el paper demuestra que combinar BLE, fingerprinting y redes neuronales puede mejorar de forma importante la localizacion indoor.

M4 fue el mejor modelo cuando existen valores vacios, mientras que M2 fue el mas estable entre distintos escenarios.

El trabajo tambien deja claro que el preprocesamiento de la senal es muy importante. Es decir, no solo importa el modelo, sino tambien como se capturan y limpian los datos.

Finalmente, para la Parte II del laboratorio, M2 parece ser el mejor candidato para reproducir, porque es estable y tiene buen soporte en el repositorio de codigo.”

### Frase de cierre util

“En resumen, el paper no solo propone una red neuronal, sino una metodologia completa para mejorar la localizacion en interiores.”

## Diapositiva 12. Repositorios y fuentes

### Que decir

“Finalmente, el paper esta respaldado por un DOI, un dataset publico y repositorios de codigo para los modelos y para la etapa de captura y filtrado.

Esto es importante porque facilita la trazabilidad del trabajo y permite avanzar hacia la reproduccion experimental.”

### Si te preguntan por que esto importa

“Porque un paper es mas valioso cuando sus resultados pueden revisarse, entenderse y reproducirse.”

## Mini glosario rapido para recordar antes de exponer

- `BLE`: Bluetooth de bajo consumo.
- `RSSI`: intensidad de la senal recibida.
- `Indoor positioning`: localizacion dentro de edificios.
- `Fingerprinting`: usar una huella de senales para reconocer una posicion.
- `Trilateracion`: calcular una ubicacion estimando distancias.
- `Dataset`: conjunto de datos.
- `Ground truth`: posicion real usada como referencia.
- `Regresion`: prediccion de valores numericos continuos.
- `Clasificacion`: prediccion de categorias o clases.
- `Loss`: error del modelo durante entrenamiento.
- `Accuracy`: porcentaje de aciertos.
- `Distancia euclidiana`: distancia recta entre dos puntos.

## Cierre final sugerido

“Para cerrar, considero que este paper es una buena eleccion para el laboratorio porque presenta un problema real de telecomunicaciones, propone una solucion basada en aprendizaje automatico y ademas ofrece resultados cuantitativos y recursos abiertos para su reproduccion.”

## Posibles preguntas y respuestas cortas

### 1. Por que no usar GPS?

“Porque en interiores el GPS pierde precision debido a paredes, techos y rebotes de la senal.”

### 2. Por que BLE?

“Porque consume poca energia, es economico y puede implementarse con infraestructura relativamente simple.”

### 3. Que aporta la inteligencia artificial aqui?

“Permite aprender patrones complejos entre las lecturas RSSI y la posicion, algo dificil de modelar solo con formulas geometricas.”

### 4. Cual fue el mejor modelo?

“M4 cuando habia valores vacios, y M2 como el modelo mas estable en general.”

### 5. Que aprendiste de este paper?

“Que en localizacion indoor no basta con entrenar una red neuronal; tambien es crucial capturar, filtrar y evaluar bien la senal.”

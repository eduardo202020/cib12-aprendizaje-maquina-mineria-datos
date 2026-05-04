# Laboratorio Semana 07

## Tema

Procesamiento de flujos de datos en tiempo real a gran escala aplicado a la detección de fraude con tarjetas.

## Propósito del laboratorio

Este laboratorio fue construido para ejemplificar, de forma práctica y demostrable, los conceptos centrales del capítulo 4 de `huawei-2022.pdf`, de la investigación realizada y de la monografía final.

La idea no es solo “simular transacciones”, sino mostrar cómo funciona un pipeline de `stream processing` cuando los datos:

- llegan continuamente;
- no siempre llegan en el mismo orden en que ocurrieron;
- pueden repetirse;
- deben evaluarse con reglas de negocio en tiempo real;
- y producen una decisión operativa inmediata.

En otras palabras, este laboratorio aterriza la idea principal del capítulo: el valor del dato depende del tiempo, por lo que la plataforma debe reaccionar antes de que la oportunidad de actuar se pierda.

## Conceptos del capítulo que sí demuestra

Este laboratorio está alineado con las secciones más importantes de la monografía:

- `Procesamiento en Tiempo Real en Big Data`
- `Marco Conceptual`
- `Arquitectura de Referencia`
- `Tecnologías Principales del Capítulo`
- `Casos de Uso: Fraude con tarjetas`

En particular, demuestra:

- flujo continuo de eventos;
- diferencia entre `event time` y `processing time`;
- uso de ventanas temporales;
- mantenimiento de estado por tarjeta;
- `watermarks`;
- eventos tardíos;
- deduplicación para comportamiento idempotente;
- checkpoints;
- decisiones en tiempo real.

## Caso de uso elegido

Se eligió el caso de `fraude con tarjetas` porque es el ejemplo más representativo del capítulo y permite ilustrar casi todos los conceptos del tema en una sola demo.

Cada evento representa una transacción bancaria con información como:

- identificador del evento;
- tarjeta;
- comercio;
- monto;
- país;
- `event_time`;
- `arrival_time`.

El motor de streaming revisa el comportamiento reciente por tarjeta y emite una decisión:

- `APROBAR`
- `REVISAR`
- `BLOQUEAR`
- `AUDITAR_TARDE`
- `IGNORAR_DUPLICADO`

## Arquitectura conceptual del laboratorio

El laboratorio reproduce una arquitectura simplificada inspirada en el capítulo:

`fuente -> broker -> procesador -> sink`

### 1. Fuente

La fuente es un conjunto de eventos de ejemplo almacenados en:

- [transacciones.jsonl](/C:/Users/pc/Documents/trabajos/cib12-aprendizaje-maquina-mineria-datos/01-exposiciones-grupales/semana-07/laboratorio/data/transacciones.jsonl)

Estos eventos simulan transacciones reales y contienen casos diseñados para demostrar:

- operaciones normales;
- montos altos;
- cambios de país;
- ráfagas de transacciones en poco tiempo;
- eventos tardíos;
- duplicados.

### 2. Broker simulado

No se levanta un Kafka real en esta versión, pero se conserva su lógica conceptual:

- desacoplar la producción y el consumo;
- mostrar una cola intermedia;
- procesar por orden de llegada (`arrival_time`).

En la versión web esto se ve claramente como una etapa separada.

### 3. Procesador de streaming

El procesador aplica reglas sobre el flujo usando:

- `event_time` para el análisis;
- `arrival_time` para el orden de llegada;
- una ventana temporal configurable;
- un `watermark`;
- estado por tarjeta;
- deduplicación por `event_id`.

### 4. Sink de decisiones

La salida final es una decisión operativa inmediata. En un sistema real, esta salida podría terminar en:

- una API de bloqueo;
- un sistema de alertas;
- una base de datos;
- un dashboard;
- o un motor de reglas.

Aquí la salida se muestra en:

- consola;
- dashboard web;
- y checkpoints del estado.

## Estructura de archivos

- `data/transacciones.jsonl`: dataset de eventos del laboratorio.
- `src/streaming_core.py`: núcleo del motor de streaming.
- `src/lab_fraude_streaming.py`: versión ejecutable por consola.
- `src/lab_fraude_dashboard.py`: servidor local con dashboard visual.
- `web/index.html`: interfaz principal del dashboard.
- `web/app.js`: lógica de actualización en navegador.
- `web/styles.css`: estilos de la interfaz visual.
- `checkpoints/`: snapshots del estado del procesamiento.

## Requisitos

Para esta versión del laboratorio solo necesitas:

- `Python 3.11` o superior.

No necesitas instalar:

- Java;
- Spark;
- Kafka;
- Docker.

Eso fue una decisión práctica para que la demo sea estable, portable y fácil de ejecutar durante la exposición.

## Ejecución desde cero

## Paso 1. Abre una terminal en la raíz del repositorio

La raíz del repositorio es:

```text
C:\Users\pc\Documents\trabajos\cib12-aprendizaje-maquina-mineria-datos
```

Puedes abrir PowerShell en esa carpeta.

## Paso 2. Verifica Python

Ejecuta:

```powershell
python --version
```

Deberías ver algo como:

```text
Python 3.11.x
```

## Paso 3. Ejecuta la versión de consola

Desde la raíz del repositorio:

```powershell
python 01-exposiciones-grupales/semana-07/laboratorio/src/lab_fraude_streaming.py
```

### Qué hace esta ejecución

- carga los eventos desde el archivo `.jsonl`;
- los ordena por `arrival_time`;
- procesa cada transacción con reglas de fraude;
- muestra decisiones en consola;
- genera checkpoints en la carpeta `checkpoints/`.

### Qué deberías ver

Una tabla parecida a esta:

```text
ARRIVAL             EVENT               CARD          MONTO DECISION           DETALLE
--------------------------------------------------------------------------------------------------------------
09:00:03            09:00:00            CARD-100     120.00 APROBAR            ...
09:00:28            09:00:25            CARD-100     980.00 REVISAR            ...
09:01:02            09:01:00            CARD-100     430.00 BLOQUEAR           ...
...
```

Al final verás un resumen:

- cuántas fueron aprobadas;
- cuántas revisadas;
- cuántas bloqueadas;
- cuántas tardías;
- cuántas duplicadas.

## Paso 4. Revisa los checkpoints

Después de ejecutar la versión de consola, se generan archivos en:

- [checkpoints](/C:/Users/pc/Documents/trabajos/cib12-aprendizaje-maquina-mineria-datos/01-exposiciones-grupales/semana-07/laboratorio/checkpoints)

Ejemplos:

- `checkpoint-004.json`
- `checkpoint-008.json`
- `checkpoint-012.json`
- `checkpoint-final.json`

Estos archivos permiten explicar el concepto de:

- estado;
- tolerancia a fallos;
- recuperación a partir de snapshots.

## Paso 5. Ejecuta la versión visual en navegador

Desde la raíz del repositorio:

```powershell
python 01-exposiciones-grupales/semana-07/laboratorio/src/lab_fraude_dashboard.py
```

Deberías ver algo como:

```text
Dashboard disponible en http://127.0.0.1:8765
Abre esa URL en el navegador y pulsa 'Iniciar simulacion'.
```

## Paso 6. Abre el dashboard

Abre esta URL en tu navegador:

```text
http://127.0.0.1:8765
```

Luego pulsa:

- `Iniciar simulacion`

## Qué muestra el dashboard

La interfaz web te permite explicar visualmente todo el flujo:

### Fuente

Muestra el evento actual:

- `event_id`
- `card_id`
- monto
- país
- `event_time`
- `arrival_time`

### Broker

Muestra:

- profundidad actual de la cola;
- eventos recientes enviados al broker;
- diferencia entre producir y procesar.

### Procesador

Muestra:

- `watermark`;
- cantidad de revisadas;
- cantidad de tardías;
- cantidad de duplicados.

### Sink

Muestra:

- última decisión emitida;
- razones de esa decisión;
- tabla de decisiones recientes.

## Reglas del laboratorio

Estas son las reglas implementadas:

- `REVISAR`: monto individual alto.
- `REVISAR`: cambio de país en menos de 2 minutos.
- `BLOQUEAR`: alta frecuencia de transacciones con monto acumulado alto en la ventana.
- `AUDITAR_TARDE`: evento que llega demasiado tarde respecto al `watermark`.
- `IGNORAR_DUPLICADO`: evento cuyo `event_id` ya fue procesado.
- `APROBAR`: evento sin patrón sospechoso.

## Cómo se conectan estas reglas con la teoría

## 1. Event time vs processing time

Los eventos se reciben por `arrival_time`, pero las reglas se calculan usando `event_time`.

Eso permite explicar por qué:

- el orden de llegada no siempre coincide con el orden real del negocio;
- y por qué `event_time` representa mejor el momento real del suceso.

## 2. Watermarks

El motor mantiene un `watermark` que avanza a partir del máximo `event_time` observado.

Si un evento llega demasiado atrás respecto a ese watermark, entonces:

- no se procesa normalmente;
- se marca como `AUDITAR_TARDE`.

Esto ilustra muy bien el tratamiento de eventos tardíos del capítulo.

## 3. Ventanas

El laboratorio usa una ventana temporal para revisar el comportamiento reciente por tarjeta.

Gracias a esto puede detectar:

- demasiadas transacciones en poco tiempo;
- montos acumulados sospechosos;
- cambios de comportamiento recientes.

## 4. Estado

Se mantiene estado por tarjeta con el historial reciente necesario para evaluar:

- frecuencia;
- monto acumulado;
- país anterior;
- secuencia reciente.

Esto aterriza la idea de `stateful stream processing`.

## 5. Deduplicación

Si llega el mismo `event_id` dos veces:

- el segundo evento no se vuelve a procesar;
- se marca como `IGNORAR_DUPLICADO`.

Esto permite explicar el concepto de comportamiento idempotente y su relación con semánticas de entrega.

## 6. Checkpoints

Cada cierto número de eventos el motor guarda un snapshot del estado.

Eso ilustra:

- recuperación tras fallos;
- consistencia del estado;
- continuidad del procesamiento.

## Parámetros configurables

La versión de consola acepta parámetros:

```powershell
python 01-exposiciones-grupales/semana-07/laboratorio/src/lab_fraude_streaming.py `
  --window-seconds 120 `
  --allowed-lateness 45 `
  --checkpoint-every 4
```

### Significado

- `--window-seconds`: tamaño de la ventana temporal.
- `--allowed-lateness`: tolerancia para eventos tardíos.
- `--checkpoint-every`: cada cuántos eventos se genera un checkpoint.

## Flujo recomendado para la exposición

Si vas a presentarlo en clase, este orden funciona muy bien:

1. Mostrar brevemente el archivo [transacciones.jsonl](/C:/Users/pc/Documents/trabajos/cib12-aprendizaje-maquina-mineria-datos/01-exposiciones-grupales/semana-07/laboratorio/data/transacciones.jsonl).
2. Explicar que cada fila representa una transacción con `event_time` y `arrival_time`.
3. Ejecutar primero la versión visual en navegador.
4. Pulsar `Iniciar simulacion`.
5. Señalar cómo cambia el evento actual, el broker y el sink.
6. Resaltar el `watermark`.
7. Señalar el caso de `IGNORAR_DUPLICADO`.
8. Señalar el caso de `AUDITAR_TARDE`.
9. Mostrar el caso de `BLOQUEAR`.
10. Abrir un checkpoint y explicar el estado guardado.

## Problemas comunes

## El navegador no abre la página

Verifica que el servidor siga ejecutándose y abre manualmente:

```text
http://127.0.0.1:8765
```

## El puerto 8765 ya está ocupado

Puedes ejecutar el dashboard en otro puerto modificando el comando:

```powershell
python 01-exposiciones-grupales/semana-07/laboratorio/src/lab_fraude_dashboard.py --port 8780
```

Y luego abres:

```text
http://127.0.0.1:8780
```

## No aparecen checkpoints

Ejecuta primero la versión de consola o inicia la simulación en la versión web. Los checkpoints se generan durante el procesamiento.

## Relación con el stack real del capítulo

Esta implementación no levanta Kafka, Flink ni Redis reales, pero conserva su lógica conceptual:

- fuente de eventos;
- broker intermedio;
- procesamiento con ventanas y estado;
- salida operativa.

La razón es práctica: en este entorno no estaban listos `Java`, `PySpark` ni un daemon activo de Docker, así que se priorizó una versión:

- estable;
- ejecutable;
- explicable;
- y útil para la exposición.

## Posible extensión futura

Este mismo laboratorio puede evolucionar a una versión más cercana al stack del capítulo:

- productor Python;
- Kafka real;
- procesamiento con PySpark Structured Streaming o PyFlink;
- salida a Redis;
- dashboard conectado al resultado real del procesamiento.

## Resumen final

Este laboratorio no es solo una simulación visual. Es una forma compacta de demostrar, con un caso de negocio claro, los fundamentos del procesamiento de flujos en tiempo real:

- los datos llegan continuamente;
- el tiempo importa;
- el sistema mantiene estado;
- los eventos pueden llegar tarde o repetidos;
- y la plataforma debe decidir rápido.

Eso lo convierte en una buena pieza de apoyo para:

- la monografía;
- la presentación;
- y la explicación oral del capítulo 4.

# Prompt para NotebookLM - Semana 03

## Objetivo de esta semana

Construir los antecedentes bibliograficos.

## Archivos que debes cargar en NotebookLM

- todos los papers relevantes del tema
- `04-trabajo-grupal/docs/avances/investigacion-IA.pdf`
- si ya existe, la presentacion o resumen de la semana 02 dentro de `04-trabajo-grupal/entregables/semana-02-sistematizacion/entrega/`

## Prompt sugerido

Actua como asistente academico para un trabajo grupal universitario. Quiero construir el entregable de la semana 03: antecedentes bibliograficos del tema.

Tema del grupo:
"Modelo de aprendizaje profundo con mecanismos de atencion para mejorar la calidad del servicio de guia virtual con aplicaciones moviles e IoT con senales Wi-Fi/BLE en museos y espacios culturales, 2026".

Usa los papers cargados y el avance de la semana 02 como contexto acumulado. Necesito que selecciones los antecedentes mas relevantes y los organizes de forma academica, no solo como una lista de referencias.

Genera lo siguiente:

1. Una seleccion priorizada de antecedentes realmente utiles para el problema.
2. Para cada antecedente: autores, anio, problema abordado, metodo, datos o escenario, hallazgo principal, y relacion con mi tema.
3. Una sintesis comparativa que muestre vacios o limitaciones de la literatura.
4. Una justificacion de por que mi tema sigue siendo pertinente.

Ademas:

- separa antecedentes directamente relacionados con indoor localization;
- separa antecedentes relacionados con atencion, heterogeneidad de dispositivos, RSSI, multipath y guia virtual;
- propone una narrativa para explicar los antecedentes en una presentacion corta.

Quiero la salida en este formato:

- bloque 1: tabla resumida de antecedentes;
- bloque 2: sintesis academica en parrafos;
- bloque 3: esquema de presentacion semanal con 3 a 5 diapositivas;
- bloque 4: lista de frases clave que luego puedan convertirse en contenido para diapositivas en LaTeX.

## Uso posterior

Con esa salida se puede generar una presentacion semanal en `.tex` y tambien alimentar el marco teorico.

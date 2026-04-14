# Informe del Laboratorio

## Datos generales

- Curso: `CIB12 - Aprendizaje de Maquina y Mineria de Datos`
- Codigo: `CIB12`
- Departamento academico: `Telecomunicaciones`
- Laboratorio: `Lab-01`
- Titulo: `Ingenieria de Prompts y Verificacion`
- Semana: pendiente de completar
- Fecha: pendiente de completar
- Docente: pendiente de completar
- Integrantes: pendiente de completar
- Tema: `Ingenieria de Prompts y Verificacion`

## 1. Resumen ejecutivo

Este laboratorio analiza como el diseño de prompts influye en la precision de las respuestas generadas por modelos de lenguaje extensos. El enunciado propone comparar un prompt generico con un prompt optimizado en al menos 10 LLM, identificar y clasificar alucinaciones, y verificar afirmaciones en bases de datos indexadas. A partir del documento de investigacion preliminar, se plantea un mini estudio comparativo con enfoque academico, donde las respuestas son auditadas mediante claims atomicos y evidencia bibliografica. La hipotesis central sostiene que un prompt optimizado, con contexto, restricciones y verificacion explicita, reduce la tasa de alucinaciones y mejora la confiabilidad de las respuestas.

## 2. Objetivo del laboratorio

### Objetivo general

Analizar como la ingenieria de prompts afecta la precision de distintos LLM y desarrollar criterios para identificar, clasificar y reducir alucinaciones mediante verificacion en bases de datos indexadas.

### Objetivos especificos

- comparar respuestas de al menos 10 LLM usando un prompt generico y un prompt optimizado;
- clasificar las alucinaciones detectadas en categorias factuales, logicas, de contexto, de referencia y estilisticas;
- verificar afirmaciones seleccionadas en BDI para estimar la confiabilidad academica de cada modelo.

## 3. Planteamiento del problema

### Contexto

Los modelos de lenguaje son herramientas cada vez mas usadas para apoyar tareas de redaccion, consulta y sintesis de informacion. Sin embargo, pueden producir respuestas plausibles pero incorrectas, especialmente cuando se les pide contenido academico con autores, fechas, articulos o DOI.

### Problema

Un prompt mal formulado puede inducir alucinaciones y afectar la validez del trabajo academico. Esto representa un riesgo cuando se usan LLM para buscar antecedentes, resumir literatura o construir argumentos tecnicos.

### Pregunta de trabajo

Que estrategias de ingenieria de prompts reducen alucinaciones y mejoran la verificabilidad academica de las respuestas generadas por distintos LLM.

## 5. Datos

- fuente de datos: respuestas producidas por al menos 10 LLM ante un prompt generico y uno optimizado;
- numero de registros: pendiente de completar con la ejecucion real;
- variables principales: nombre del LLM, tipo de prompt, respuesta, fragmento observado, tipo de alucinacion, claim atomico, BDI consultada, evidencia y veredicto;
- criterio de seleccion: se deben elegir 2 a 3 afirmaciones verificables por cada LLM;
- problemas detectados: riesgo de citas inventadas, autores inexistentes, relaciones causales incorrectas y respuestas fuera de contexto;
- consideraciones eticas o de calidad: no asumir como verdaderas las respuestas del modelo sin verificacion externa.

## 4. Metodologia

### 6.1 Preprocesamiento

Se propone registrar todas las respuestas de los LLM de forma completa, luego subrayar fragmentos sospechosos y separar afirmaciones complejas en claims atomicos para facilitar la verificacion bibliografica.

### 6.2 Tecnicas o modelos aplicados

El laboratorio compara dos configuraciones de entrada:

- prompt generico, amplio y sin restricciones;
- prompt optimizado, con rol, contexto, especificidad, formato esperado y solicitud de verificacion explicita.

Los errores deben clasificarse en categorias definidas por el laboratorio: alucinaciones factuales, logicas, de contexto, de referencia y linguisticas o estilisticas.

### 6.3 Metricas de evaluacion

Las metricas propuestas en el documento de investigacion son:

- numero de claims verificados por modelo y por tipo de prompt;
- numero de claims clasificados como alucinacion;
- tasa de alucinacion por LLM;
- precision verificable;
- reduccion absoluta y relativa de alucinaciones entre el prompt generico y el optimizado.

## 5. Desarrollo y experimentos

El procedimiento del laboratorio se organiza en cuatro etapas:

1. generar un prompt inicial y ejecutarlo en al menos 10 LLM;
2. registrar respuestas y clasificar posibles alucinaciones;
3. rediseñar el prompt aplicando estrategias de ingenieria de prompts;
4. verificar en una BDI las afirmaciones seleccionadas y comparar resultados.

Como apoyo metodologico, el documento `lab_01.pdf` recomienda mantener tres tablas minimas:

- tabla de ejecucion con modelo, tipo de prompt y respuesta completa;
- tabla de clasificacion de alucinaciones por fragmento;
- tabla de verificacion en BDI con evidencia bibliografica y veredicto.

## 6. Resultados

### Resultados cuantitativos

Los resultados cuantitativos finales aun deben completarse con los datos reales de ejecucion. En esta etapa, el informe puede reportar como minimo:

- numero total de LLM evaluados;
- numero de respuestas registradas;
- numero de claims verificados;
- tasa de alucinacion por modelo;
- diferencia entre prompt generico y prompt optimizado.

### Resultados cualitativos

De acuerdo con el marco del laboratorio, se espera observar que los prompts genericos generen mas errores de referencia, citas imprecisas y respuestas mas ambiguas. En contraste, los prompts optimizados deberian producir salidas mejor estructuradas, mas faciles de verificar y con menor frecuencia de afirmaciones no sustentadas.

## 7. Discusion

El valor principal del laboratorio no esta solo en detectar errores, sino en mostrar que la calidad de la salida depende en buena medida del diseño del prompt. La discusion debe comparar que modelos generan mas alucinaciones, en que categoria se concentran y que estrategias de ingenieria de prompts ayudaron a reducirlas. Tambien debe resaltarse que la confiabilidad academica de un LLM no puede asumirse automaticamente: necesita contraste con fuentes indexadas.

## 8. Conclusiones

- la ingenieria de prompts es un factor determinante para mejorar la utilidad academica de los LLM;
- la verificacion en BDI es necesaria para distinguir contenido plausible de informacion realmente sustentada;
- las alucinaciones no solo son factuales, tambien pueden ser logicas, contextuales o de referencia;
- la utilidad academica de un LLM depende tanto de la calidad del prompt como del proceso de verificacion posterior.

## 9. Trabajo futuro

El siguiente paso natural es completar el experimento con las respuestas reales de los 10 LLM, consolidar la tabla de verificacion y calcular metricas comparativas. Luego, este esquema puede ampliarse hacia un trabajo mas formal sobre confiabilidad de IA generativa en contextos academicos o tecnicos.

## 10. Referencias

1. Ji, Z., Lee, N., Frieske, R., Yu, T., Su, D., Xu, Y., et al. (2023). Survey of hallucination in natural language generation. *ACM Computing Surveys*, 55(12), 1-38. https://doi.org/10.1145/3571730
2. Liu, P., Yuan, W., Fu, J., Jiang, Z., Hayashi, H., and Neubig, G. (2023). Pre-train, prompt, and predict: A systematic survey of prompting methods in natural language processing. *ACM Computing Surveys*, 55(9), 1-35. https://doi.org/10.1145/3560815
3. Crossref. Metadata search. https://search.crossref.org/

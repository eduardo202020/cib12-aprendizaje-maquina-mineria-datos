# Ficha del Laboratorio

Esta ficha ya fue prellenada con la informacion disponible en:

- `01.1 Laboratorio de Ingenieria de Prompts.pdf` como enunciado;
- `lab_01.pdf` como desarrollo metodologico preliminar.

## 1. Identificacion

- Curso: `CIB12 - Aprendizaje de Maquina y Mineria de Datos`
- Codigo: `CIB12`
- Departamento academico: `Telecomunicaciones`
- Docente: pendiente de completar
- Ciclo / semestre: pendiente de completar
- Semana: pendiente de completar
- Laboratorio: `Lab-01`
- Titulo del laboratorio: `Ingenieria de Prompts y Verificacion`
- Fecha de entrega: pendiente de completar
- Modalidad: por confirmar
- Integrantes: pendiente de completar

## 2. Tema del laboratorio

- Tema principal: `ingenieria de prompts y verificacion academica`
- Tipo de trabajo: `laboratorio`

## 3. Problema y alcance

- Problema que se busca resolver: determinar como el diseno de prompts afecta la precision de las respuestas de multiples LLM.
- Pregunta de investigacion o pregunta tecnica: que estrategias de ingenieria de prompts reducen alucinaciones y mejoran la verificabilidad academica de las respuestas.
- Hipotesis o idea central: un prompt optimizado con contexto, restricciones, formato y solicitud de verificacion explicita reduce la tasa de alucinaciones frente a un prompt generico.
- Alcance del laboratorio: comparacion de al menos 10 LLM, clasificacion de alucinaciones y verificacion de 2 a 3 afirmaciones por modelo en bases de datos indexadas.
- Limitaciones conocidas: falta registrar todavia los resultados reales de ejecucion, la verificacion completa en BDI y las metricas finales por modelo.

## 4. Datos y recursos

- Dataset o fuente de datos: respuestas textuales generadas por al menos 10 LLM a partir de un prompt generico y uno optimizado.
- Tipo de datos: texto, citas, afirmaciones verificables y metadatos bibliograficos.
- Numero de registros: pendiente; idealmente 20 respuestas base o mas, segun cantidad de LLM y tipo de prompt.
- Variables principales: modelo, tipo de prompt, respuesta, fragmento analizado, tipo de alucinacion, claim atomico, BDI consultada, evidencia y veredicto.
- Herramientas: LLM web o app, documento de registro, BDI como Scopus, Web of Science, SciELO, Redalyc o IEEE Xplore.
- Entorno usado: pendiente de completar

## 5. Metodologia prevista

- Preprocesamiento: separar respuestas por modelo, identificar fragmentos relevantes y convertir afirmaciones complejas en claims atomicos.
- Algoritmos o tecnicas: comparacion antes y despues del rediseño del prompt; clasificacion manual asistida de alucinaciones.
- Metricas: tasa de alucinacion por modelo y por tipo de prompt; precision verificable; reduccion absoluta y relativa de alucinaciones.
- Baseline o punto de comparacion: prompt generico amplio sin restricciones.
- Evidencia esperada: tablas comparativas, tabla de verificacion en BDI, analisis critico y conclusiones sobre confiabilidad academica.

## 6. Entregables

- Notebook: opcional
- Codigo fuente: opcional para automatizar tablas y metricas
- Informe PDF: `02-laboratorios/Lab-01/informe/informe.tex` o `informe.md`
- Presentacion PDF: pendiente de exportar
- Presentacion web: pendiente
- Demo: opcional

## 7. Criterios de revision antes de entregar

- el informe ya tiene objetivo, metodologia, resultados esperados y conclusiones provisionales;
- faltan completar las evidencias experimentales reales;
- las referencias base ya estan identificadas;
- la exposicion debe resumir comparacion entre prompt generico y optimizado;
- cada integrante debe saber que parte sustentara;
- antes de entregar conviene exportar informe y diapositivas a PDF.

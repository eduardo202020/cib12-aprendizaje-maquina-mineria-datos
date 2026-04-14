
Quiero que actues como asistente academico para el curso CIB12 - Aprendizaje de Maquina y Mineria de Datos.

Voy a adjuntarte un PDF. Usa solo esa fuente para generar un material de estudio semanal en LaTeX, pensado para prepararme para un cuestionario.

Datos de esta semana:

- Semana: [SEMANA]
- Tema: [TEMA]
- Libro o fuente: [LIBRO]
- Capitulo o seccion: [CAPITULO]

Instrucciones:

1. Usa solo la informacion del PDF adjunto.
2. Enfocate solo en el capitulo o seccion indicada.
3. No inventes contenido fuera del PDF.
4. Redacta en espanol claro, academico y facil de estudiar.
5. Prioriza definiciones, relaciones, procesos, comparaciones, arquitectura, herramientas, componentes, ventajas, limitaciones y aplicaciones.
6. Si hay diagramas o flujos en el PDF, explicalos en texto.
7. Incluye preguntas probables de cuestionario con respuestas cortas.
8. El resultado debe quedar listo para imprimir barato.

Quiero que entregues el resultado como codigo LaTeX completo, compilable con pdflatex, usando exactamente este formato base:

\documentclass[8pt,a4paper,twocolumn]{article}

\usepackage[spanish]{babel}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[left=0.75cm,right=0.75cm,top=0.55cm,bottom=0.7cm,columnsep=0.45cm]{geometry}
\usepackage{lmodern}
\usepackage{booktabs}
\usepackage{longtable}
\usepackage{array}
\usepackage{hyperref}
\usepackage{enumitem}
\usepackage{xcolor}
\usepackage{titlesec}
\usepackage[most]{tcolorbox}

\setlength{\parindent}{0pt}
\setlength{\parskip}{0.12em}
\setlength{\columnseprule}{0pt}
\pagestyle{plain}
\setlist[itemize]{leftmargin=1.0cm,itemsep=0.1em,topsep=0.15em}
\setlist[enumerate]{leftmargin=1.0cm,itemsep=0.1em,topsep=0.15em}
\setlist[description]{leftmargin=0cm,style=nextline,itemsep=0.1em,topsep=0.15em}
\titlespacing*{\section}{0pt}{0.35em}{0.2em}
\titlespacing*{\subsection}{0pt}{0.3em}{0.15em}

\newcommand{\resumentitulo}{Resumen de estudio - Semana [SEMANA]}

\begin{document}

\vspace*{-1.0em}
\begin{tcolorbox}[colback=black!12,colframe=black!35,boxrule=0.3pt,arc=1pt,left=4pt,right=4pt,top=3pt,bottom=3pt]
{\bfseries\normalsize \resumentitulo\par}
{\scriptsize CIB12 - Aprendizaje de Maquina y Mineria de Datos\par}
\end{tcolorbox}
\vspace{0.15em}

Estructura obligatoria del contenido:

1. Tema
2. Resumen de la semana
3. Conceptos clave
4. Desarrollo del tema
5. Procesos, arquitectura o flujo del tema
6. Herramientas, algoritmos o componentes importantes
7. Aplicaciones o ejemplos
8. Resumen para memorizar
9. Preguntas probables de cuestionario
10. Mini glosario

Requisitos adicionales:

- Usa secciones y subsecciones claras.
- Usa listas cuando ayuden a estudiar mejor.
- Usa tablas si ayudan a comparar conceptos.
- Incluye una caja o bloque llamado Idea central.
- Incluye una caja o bloque llamado Errores comunes o confusiones frecuentes, si aplica.
- Incluye entre 8 y 15 preguntas probables de cuestionario.
- Cada pregunta debe tener respuesta corta.
- El documento debe quedar listo para pegar directamente en mi archivo .tex.
- No uses \maketitle.
- No pongas texto fuera del bloque de codigo LaTeX.
- No expliques nada fuera del codigo.

Ahora genera el documento completo en LaTeX.


---

## Ejemplo rapido

Solo remplaza así:

- `[SEMANA]` -> `4`
- `[TEMA]` -> `Desarrollo de Aplicaciones Big Data`
- `[LIBRO]` -> `Huawei (2022)`
- `[CAPITULO]` -> `Capitulo 1`

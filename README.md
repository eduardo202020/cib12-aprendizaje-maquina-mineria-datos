# CIB12 - Aprendizaje de Maquina y Mineria de Datos

Repositorio base para organizar laboratorios, informes, presentaciones y evidencia del curso.

## Objetivo

Tener un flujo simple para:

- desarrollar cada laboratorio con orden;
- guardar el informe final en PDF;
- preparar una exposicion visible desde GitHub Pages;
- usar GitHub como respaldo, historial y vitrina del curso.

## Estructura

```text
cib12-aprendizaje-maquina-mineria-datos/
├── README.md
├── .gitignore
├── docs/                      # GitHub Pages
│   ├── index.html
│   ├── styles.css
│   ├── .nojekyll
│   └── presentaciones/
│       └── lab00.html
├── laboratorios/
│   └── lab00-plantilla/
│       ├── README.md
│       ├── datos/
│       ├── notebooks/
│       ├── src/
│       ├── resultados/
│       ├── informe/
│       │   └── informe.md
│       └── presentacion/
│           ├── diapositivas.md
│           └── guion.md
├── informes/                  # PDFs finales exportados
├── presentaciones/            # PDFs de exposicion exportados
└── proyecto-final/
```

## Flujo recomendado

1. Duplica `laboratorios/lab00-plantilla/` y renombralo a `lab01`, `lab02`, etc.
2. Trabaja el analisis en `notebooks/` o `src/`.
3. Guarda tablas, graficos y metricas en `resultados/`.
4. Redacta el informe en `informe/informe.md`.
5. Prepara la exposicion en `presentacion/diapositivas.md`.
6. Exporta a PDF y guarda:
   - informes en `informes/`
   - diapositivas en `presentaciones/`
7. Actualiza `docs/index.html` para enlazar el nuevo laboratorio en GitHub Pages.

## Como usar GitHub Pages

1. Sube este repositorio a GitHub.
2. Ve a `Settings > Pages`.
3. En `Build and deployment`, selecciona:
   - `Source`: `Deploy from a branch`
   - `Branch`: `main`
   - `Folder`: `/docs`
4. Guarda y espera la URL publica.

La pagina principal quedara en algo como:

`https://TU-USUARIO.github.io/cib12-aprendizaje-maquina-mineria-datos/`

## Entrega y exposicion

- Para entregar: comparte el enlace del repositorio y, si te lo piden, el PDF del informe.
- Para exponer: abre GitHub Pages o el PDF local.
- Para preguntas tecnicas: abre el notebook, codigo o resultados desde el repo.

## Siguiente paso sugerido

Cuando salga el primer laboratorio:

1. copia `laboratorios/lab00-plantilla` a `laboratorios/lab01`;
2. cambia los titulos;
3. agrega enlaces a `docs/index.html`;
4. exporta el informe y las diapositivas a PDF.

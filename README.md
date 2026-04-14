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
├── 02-laboratorios/
│   ├── Lab-01/
│   ├── Lab-02/
│   ├── Lab-03/
│   ├── Lab-04/
│   ├── Lab-05/
│   └── Lab-06/
├── informes/                  # PDFs finales exportados
├── presentaciones/            # PDFs de exposicion exportados
└── proyecto-final/
```

## Flujo recomendado

1. Usa `02-laboratorios/` como ubicacion principal de los laboratorios.
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

Cuando trabajes un nuevo laboratorio:

1. crea o completa su carpeta dentro de `02-laboratorios/`;
2. organiza el material en `docs`, `src`, `datos`, `resultados` y `notebooks` si aplica;
3. agrega enlaces a `docs/index.html` o a la landing correspondiente;
4. exporta el informe y las diapositivas a PDF.

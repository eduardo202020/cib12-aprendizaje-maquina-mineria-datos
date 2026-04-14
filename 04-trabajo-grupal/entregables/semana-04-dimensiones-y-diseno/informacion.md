Como asesor académico, he procesado los requerimientos para el entregable de la **semana 04**, integrando los hallazgos técnicos de los artículos de vanguardia (STELLAR, ANVIL, xKAN) con la estructura de gestión de proyectos definida en los lineamientos del curso.

A continuación, presento la propuesta de dimensiones y diseño preliminar para su investigación aplicada.

---

### BLOQUE 1: Tabla de variables, dimensiones e indicadores

Esta tabla operacionaliza el tema, permitiendo que conceptos abstractos como "atención" o "calidad" se conviertan en métricas medibles en el entorno del museo.

| Variable | Dimensión | Indicadores sugeridos | Respaldo (Fuente) |
| :--- | :--- | :--- | :--- |
| **Independiente (VI):** Modelo de aprendizaje profundo con mecanismos de atención | **Arquitectura de Invarianza** | • Número de capas de aumento de huellas (FASt layers).<br>• Tasa de pérdida contrastiva (Triplet Loss). | |
| | **Mecanismo de Atención** | • Número de cabezas de atención (Multi-head).<br>• Puntuación de importancia de señal (Global Influence Score). | |
| | **Eficiencia en el Borde (Edge AI)** | • Tiempo de inferencia en smartphone (ms).<br>• Cantidad de parámetros entrenables (K-parameters). | |
| **Dependiente (VD):** Calidad del servicio de guía virtual | **Desempeño Técnico** | • Error promedio de localización (metros).<br>• Error en el 95-percentil (m).<br>• F1-score de clasificación por sala. | |
| | **Oportunidad y Pertinencia** | • Porcentaje de activaciones correctas de guía por zona.<br>• Tiempo de respuesta desde la entrada a zona (ms). | |
| | **Resiliencia Temporal** | • Degradación de precisión tras 6-12 meses sin recalibrar.<br>• Varianza del error entre dispositivos heterogéneos. | |

---

### BLOQUE 2: Descripción del diseño preliminar

**Tipo y Diseño de Estudio:**
Se propone un diseño **cuasi-experimental de nivel explicativo**. El estudio comparará el rendimiento de un modelo base (*baseline*) como k-NN o MLP tradicional frente al modelo propuesto basado en mecanismos de atención y redes siamesas en condiciones de heterogeneidad de hardware (uso de diferentes marcas de smartphones).

**Procedimiento Experimental:**
1.  **Fase Offline (Entrenamiento):** Recolección de *fingerprints* Wi-Fi/BLE en las salas del museo usando un dispositivo maestro. Construcción del radio-mapa y entrenamiento de la red siamesa para aprender características invariantes.
2.  **Fase Online (Prueba):** Despliegue del modelo en la aplicación móvil de guía virtual. Usuarios con diversos smartphones recorrerán el museo.
3.  **Evaluación de QoS:** Se medirá si la guía de audio o información contextual se activa correctamente al entrar en el radio de una obra u objeto cultural, correlacionando la precisión técnica con la satisfacción del servicio.

**Justificación de Coherencia:**
Este diseño es coherente porque aborda directamente el problema identificado en la literatura: la **inestabilidad del RSSI** y la **heterogeneidad de dispositivos**. Al usar un enfoque experimental, podemos validar estadísticamente si la "atención" realmente mejora la "calidad del servicio" frente a métodos que no la usan.

---

### BLOQUE 3: Esquema para presentación semanal (Semana 04)

*   **Diapositiva 1: Operacionalización de Variables.** Presentación de la VI (Modelo con Atención) y VD (Calidad del Servicio) con sus dimensiones técnicas y de usuario.
*   **Diapositiva 2: Desempeño Técnico vs. Calidad de Servicio.** Explicación de que el error en metros (técnico) es el medio, pero la activación correcta de la guía (QoS) es el fin.
*   **Diapositiva 3: Diseño Cuasi-experimental.** Diagrama del flujo de trabajo: Radio-mapa $\rightarrow$ Entrenamiento Siames $\rightarrow$ Pruebas con smartphones diversos en el museo.
*   **Diapositiva 4: Indicadores y Métricas.** Resumen de los KPI del proyecto (Error < 2m, Invarianza de dispositivo > 30% mejora).
*   **Diapositiva 5: Conexión con la Matriz de Consistencia.** Cómo estas dimensiones aseguran que el objetivo general sea medible y alcanzable en 2026.

---

### BLOQUE 4: Bullets para diapositivas (Contenido técnico)

*   **Diferenciación Crítica:** El **desempeño técnico** se mide en el laboratorio (error métrico), mientras que la **calidad del servicio** se mide en la experiencia del visitante (continuidad y pertinencia de la guía).
*   **Mejora de Indicador:** Se descarta el indicador ambiguo "Satisfacción del usuario" por el indicador objetivo **"Tasa de activaciones contextuales correctas"**, que es directamente dependiente de la precisión de localización.
*   **Robusto ante el Tiempo:** Se integra la dimensión de **"Invarianza Temporal"** para medir cuánto tiempo el sistema del museo puede operar sin mantenimiento manual (recalibración-free).
*   **Trazabilidad Académica:** Cada dimensión conecta con la **Matriz de Consistencia**, garantizando que si la Hipótesis General es correcta, los indicadores deben mostrar una mejora significativa en la precisión y estabilidad.
*   **Uso de XAI:** Se incluye la dimensión de **"Diagnóstico de Error"** mediante xKAN para explicar por qué el sistema podría fallar en salas con alta interferencia de metal o muros densos.
Como asistente académico para tu grupo de **Machine Learning y Big Data**, he seleccionado y organizado los antecedentes bibliográficos más relevantes para tu proyecto sobre servicios de guía virtual en museos. Esta selección prioriza soluciones que abordan directamente la **heterogeneidad de dispositivos**, la **invarianza temporal** y el uso de **mecanismos de atención**, elementos clave identificados en tu sistematización previa.

### BLOQUE 1: Tabla resumida de antecedentes

| N° | Autores / Año | Problema abordado | Método utilizado | Escenario / Datos | Hallazgo principal | Relación con el tema |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | Gufran et al. (2023) | Variaciones temporales y heterogeneidad de hardware. | Marco **STELLAR**: Redes siamesas con atención multicabezal. | Entornos interiores diversos durante 2 años. | Mejora de precisión del 18% al 165% en periodos largos sin recalibrar. | Base para el modelo robusto y "libre de recalibración" propuesto. |
| 2 | Singampalli et al. (2024) | Naturaleza de "caja negra" de los modelos de IA en localización. | Marco **xKAN**: IA Explicable (XAI) post-hoc model-agnostic. | Dos edificios con alta densidad de APs (hasta 194). | Logra una interpretabilidad funcional del impacto del RSSI de cada AP. | Permite diagnosticar errores en la guía virtual del museo. |
| 3 | Tiku et al. (2022) | Degradación de precisión por cambio de smartphone del usuario. | Marco **ANVIL**: Atención multicabezal y aumento de datos FASt. | Cinco planos de planta universitarios (oficinas, aulas). | Mejora del 35% en precisión frente a métodos tradicionales de DL. | Clave para manejar la diversidad de móviles de los visitantes. |
| 4 | Jianhua et al. (2026) | Inestabilidad en navegación multiescena y alto costo de infraestructura. | Marco **MMVP**: Fusión de sensores, MLA y visión artificial ligera. | Oficina típica con trayectorias en múltiples pisos. | Error promedio de 0.55m usando hardware comercial existente. | Aporta la capa de fusión sensorial (IMU/BLE) para museos. |
| 5 | Salamah et al. (2016) | Alta redundancia de señales y costo computacional en móviles. | Reducción de dimensionalidad mediante **PCA** y clasificadores ML. | Hall de un departamento con interferencia de movimiento. | Reducción del 70% en tiempo de procesamiento manteniendo la precisión. | Optimiza la aplicación del museo para ejecutarse en tiempo real. |

---

### BLOQUE 2: Síntesis académica en párrafos

**Tendencias en Localización Indoor y Heterogeneidad**
La literatura reciente destaca que el uso de huellas digitales (*fingerprinting*) de Wi-Fi y BLE es la técnica más viable para servicios basados en ubicación (LBS) en entornos complejos como museos. Sin embargo, se reporta un vacío crítico: la **heterogeneidad de dispositivos**, donde diferentes chipsets reportan patrones de RSSI distintos para un mismo punto, degrada severamente la precisión. Para mitigar esto, investigadores han evolucionado de métodos determinísticos (k-NN) a arquitecturas de **Deep Learning** que incorporan mecanismos de atención multicabezal, permitiendo que el modelo se enfoque selectivamente en las señales más estables y relevantes del entorno.

**Varianza Temporal y el Desafío de la Recalibración**
Otro problema recurrente identificado es la inestabilidad de la señal RSSI a lo largo del tiempo debido a cambios en la infraestructura o el mobiliario. Los antecedentes muestran que los métodos tradicionales requieren recalibraciones manuales costosas y disruptivas. Propuestas innovadoras como el marco **STELLAR** introducen el aprendizaje contrastivo y redes siamesas para lograr sistemas "libres de recalibración", capaces de mantener la precisión durante años. Además, la integración de IA explicable (**xKAN**) surge como una solución para transparentar las decisiones del modelo, permitiendo entender por qué un sistema de guía virtual podría fallar en una sala específica del museo.

**Fusión Sensorial y Viabilidad del Proyecto**
Finalmente, los antecedentes validan que la precisión submétrica necesaria para guías virtuales se alcanza mediante la **fusión multisensorial** (BLE, Wi-Fi, IMU y visión). El uso de modelos ligeros optimizados, como EfficientNet-Lite o la aplicación de PCA, garantiza que estos algoritmos de aprendizaje profundo sean ejecutables directamente en los smartphones de los visitantes sin agotar la batería. Esto justifica la pertinencia de un modelo que una la robustez de la atención multicabezal con la eficiencia de IoT para mejorar la experiencia museográfica en 2026.

---

### BLOQUE 3: Esquema de presentación semanal

**Diapositiva 1: Criterios de Selección de Antecedentes**
*   **Enfoque:** Papers originales de alto impacto (IEEE, ACM) 2016-2026.
*   **Filtros aplicados:**
    *   Sistemas basados en Wi-Fi/BLE RSSI.
    *   Uso de Mecanismos de Atención y Deep Learning.
    *   Soluciones a la heterogeneidad de hardware.

**Diapositiva 2: El Estado del Arte en Atención e Invarianza**
*   **STELLAR (2023):** Uso de redes siamesas para evitar recalibraciones manuales ante cambios en el tiempo.
*   **ANVIL (2022):** Capas FASt de aumento de datos para que la app funcione en cualquier marca de móvil.
*   **Hallazgo clave:** La atención multicabezal mejora la precisión hasta un 165% en condiciones variables.

**Diapositiva 3: Transparencia y Fusión Multimodal**
*   **xKAN (2025):** IA Explicable para entender cómo las señales de la sala influyen en la ubicación.
*   **MMVP (2026):** Fusión de BLE con visión artificial ligera para precisión de 0.55m.
*   **PCA (2016):** Reducción del 70% del costo computacional en smartphones.

**Diapositiva 4: Vacíos Detectados y Justificación**
*   **Vacío 1:** La mayoría de modelos DL son "cajas negras" difíciles de depurar en museos.
*   **Vacío 2:** Alta dependencia de datasets etiquetados manualmente y estáticos.
*   **Nuestra Pertinencia:** El proyecto integra atención, resiliencia temporal y XAI para un servicio de guía virtual confiable y escalable en 2026.

---

### BLOQUE 4: Frases clave para LaTeX

```latex
% Frases para bullets en diapositivas LaTeX
\item La heterogeneidad de dispositivos causa discrepancias críticas en los patrones de RSSI \cite{Gufran2023}.
\item Los mecanismos de atención multicabezal permiten mitigar el ruido y el efecto multipath \cite{Tiku2022}.
\item El marco STELLAR propone sistemas libres de recalibración mediante aprendizaje contrastivo \cite{Gufran2023}.
\item La IA Explicable (xKAN) revela las dependencias estructurales AP-RP en planos complejos \cite{Singampalli2024}.
\item La fusión de señales BLE con visión artificial ligera logra precisiones submétricas de 0.55m \cite{Jianhua2026}.
\item La optimización mediante PCA reduce el costo computacional en dispositivos móviles un 70\% \cite{Salamah2016}.
\item Existe una necesidad urgente de modelos robustos ante variaciones temporales en entornos dinámicos \cite{Gufran2023}.
```
Como asistente académico para tu grupo de **Machine Learning y Big Data**, he estructurado la sistematización de tu tema de investigación basándome en los lineamientos del curso y en los antecedentes científicos proporcionados. 

Esta propuesta integra los conceptos de **heterogeneidad de dispositivos** y **variaciones temporales** hallados en los artículos de vanguardia (como el marco STELLAR y ANVIL) para asegurar que el trabajo tenga el rigor necesario para un artículo científico publicable.

---

### BLOQUE 1: Versión académica final del contenido

**1. LÍNEA DE INVESTIGACIÓN:**  
Inteligencia Artificial y Comunicación Inalámbrica.

**2. TEMA GENERAL:**  
Sistemas de radiolocalización en interiores basados en aprendizaje profundo para servicios basados en la ubicación (LBS).

**3. TEMAS PARTICULARES:**  
1. Arquitecturas de redes neuronales con mecanismos de atención para el procesamiento de señales de radio.  
2. Mitigación de la heterogeneidad de hardware y variaciones temporales en entornos inalámbricos dinámicos.  
3. Integración de dispositivos móviles e infraestructura IoT para la mejora de la experiencia del usuario (UX) en espacios cerrados.

**4. TEMAS ESPECÍFICOS:**  
1. Implementación de redes neuronales siamesas para la extracción de características robustas (invarianza) en señales RSSI de Wi-Fi/BLE.  
2. Aplicación de mecanismos de atención multicabezal para filtrar el ruido y el desvanecimiento por trayectorias múltiples en museos.  
3. Desarrollo de modelos ligeros de aprendizaje profundo para inferencia en tiempo real directamente en dispositivos móviles (Edge AI).

**5. PROBLEMA DE ESTUDIO:**  
Los servicios de guía virtual en museos y espacios culturales dependen críticamente de la precisión de la localización en interiores. Sin embargo, las señales Wi-Fi y BLE sufren de una **inestabilidad inherente** debido a la interferencia humana dinámica, el efecto *multipath* y, principalmente, la **heterogeneidad de los dispositivos** (diferentes smartphones captan diferentes intensidades de señal en un mismo punto). Esto provoca que los modelos convencionales de aprendizaje automático pierdan precisión con el tiempo y requieran recalibraciones manuales costosas, afectando la continuidad y calidad del servicio de guía virtual.

**6. TÍTULO PRELIMINAR DE LA INVESTIGACIÓN:**  
Análisis de la precisión y resiliencia de modelos de aprendizaje profundo ante la heterogeneidad de señales inalámbricas en entornos culturales.

**7. TÍTULO TENTATIVO DE LA INVESTIGACIÓN:**  
Modelo de aprendizaje profundo basado en redes siamesas y mecanismos de atención para una localización indoor robusta y libre de recalibración en servicios de guía virtual para museos, 2026.

**8. VARIABLE INDEPENDIENTE:**  
Arquitectura de red neuronal profunda con mecanismos de atención multicabezal y aprendizaje contrastivo (redes siamesas).

**9. VARIABLE DEPENDIENTE:**  
Calidad del servicio de localización, medida a través de la precisión métrica (error promedio en metros) y la robustez ante el cambio de dispositivo (invarianza).

**10. OBJETO DE ESTUDIO:**  
Sistema de radiolocalización basado en huellas digitales (*fingerprinting*) de señales Wi-Fi/BLE en entornos interiores de alta concurrencia.

**11. ALCANCE ESPACIAL:**  
Espacios culturales y museos (o simulaciones en edificios universitarios con alta densidad de puntos de acceso y visitantes).

**12. ALCANCE TEMPORAL:**  
Periodo académico 2026.

---

### BLOQUE 2: Observaciones y mejoras

*   **Explicación de coherencia:**  
    *   **Línea y Tema:** Son coherentes porque utilizas IA (Deep Learning/Atención) para resolver un problema de telecomunicaciones (Localización con señales Wi-Fi/BLE).  
    *   **Variables:** La arquitectura de atención es el "motor" (independiente) que genera el resultado de precisión y robustez (dependiente) necesario para un museo, donde no puedes obligar a todos los visitantes a usar el mismo modelo de teléfono.
*   **Detección de inconsistencias:**  
    *   El título original mencionaba "Calidad del servicio". En términos técnicos de Machine Learning, esto es muy ambiguo. Se ha mejorado vinculándolo a la **precisión métrica** y la **resiliencia temporal**, que son las métricas reales evaluadas en los artículos científicos.
    *   Se añadió el concepto de **redes siamesas**. Los papers sugieren que la "atención" por sí sola no resuelve la variación a largo plazo; se requiere aprendizaje contrastivo para que el sistema sea "libre de recalibración".
*   **Mejoras de redacción:**  
    *   Se sustituyó "mejorar la calidad" por "mitigar la heterogeneidad y variaciones temporales", ya que es un término más académico y específico del área de radiolocalización.

---

### BLOQUE 3: Estructura para presentación semanal (Semana 02)

**Diapositiva 1: Título y Contexto**
*   **Título del Proyecto:** Modelo de Localización Indoor con Atención para Guías Virtuales en Museos.
*   **Línea de investigación:** IA y Comunicación Inalámbrica.
*   **Contexto:** El crecimiento del mercado de servicios basados en ubicación (LBS) y su necesidad en el turismo cultural 2026.

**Diapositiva 2: El Problema (The Pain Point)**
*   **Inestabilidad de señal:** El RSSI varía por obstáculos y movimiento de personas.
*   **Heterogeneidad:** Los modelos entrenados con un smartphone "X" no funcionan bien en un smartphone "Y" de un visitante.
*   **Costo de mantenimiento:** La necesidad constante de recalibrar los mapas de señales en los museos.

**Diapositiva 3: Propuesta Tecnológica Innovadora**
*   **Mecanismos de atención:** Permiten al modelo enfocarse en los puntos de acceso (APs) más estables y relevantes.
*   **Aprendizaje contrastivo:** Uso de redes siamesas para que el sistema aprenda a reconocer la ubicación a pesar de que la intensidad de señal cambie.
*   **Edge AI:** Procesamiento eficiente para que la aplicación del museo responda al instante en el móvil.

**Diapositiva 4: Metodología y Variables**
*   **Variable Independiente:** Modelo de Deep Learning con Atención y FASt Layers (Fingerprint Augmentation).
*   **Variable Dependiente:** Reducción del error de localización y aumento de la resiliencia temporal.
*   **Objetivo final:** Lograr un sistema de guía virtual preciso sin necesidad de mantenimiento manual del radio-mapa.

**Diapositiva 5: Referencias Clave (Basado en el estado del arte)**
*   Uso de marcos de trabajo validados como **STELLAR** (2023) y **ANVIL** (2022) para el diseño del modelo.
*   Cumplimiento con los lineamientos de investigación académica del curso.
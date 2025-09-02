## Resumen del informe

### 1. Introducción
Las BCI permiten que personas, incluso completamente paralizadas, se comuniquen con el entorno mediante señales cerebrales registradas por EEG. Se basan en la detección de intenciones a través de potenciales relacionados con eventos.

---

## 2. Modelo Funcional de un BCI Genérico

Propuesto por Mason & Birch, incluye los siguientes bloques:

- **Usuario**: genera señales cerebrales.
- **Extractor de características**: detecta variaciones neurológicas.
- **Clasificador**: asigna estados cerebrales a comandos.
- **Retroalimentación**: permite al usuario ajustar su control.

---

## 3. Paradigmas de BCI No Invasivas

### Cuadro comparativo de paradigmas

| Paradigma                                   | Señal EEG                          | Ventajas                                                                 | Desventajas                                                                 |
|--------------------------------------------|------------------------------------|--------------------------------------------------------------------------|------------------------------------------------------------------------------|
| **VEP (Visual Evoked Potentials)**         | Estímulos visuales                 | Control de cursor por mirada                                             | Requiere vías nerviosas intactas                                            |
| **SSVEP (Steady-State VEP)**               | Estímulos visuales periódicos >6Hz| Poco entrenamiento, pocos canales                                        | Requiere atención visual sostenida                                          |
| **SCP (Slow Cortical Potentials)**         | EEG de baja frecuencia (0.1–2 Hz) | Aplicación clínica probada                                               | Entrenamiento largo, baja tasa de éxito                                     |
| **MT (Mental Tasks)**                      | EEG espontáneo                    | No requiere estímulos externos                                           | Control poco natural                                                        |
| **ERD/ERS (Event-Related Desync/Sync)**    | Ritmos mu (8–12 Hz) y beta (16–26 Hz) | Relacionado con intención motora                                     | Requiere entrenamiento                                                      |
| **ERP (Event-Related Potentials, P300)**   | Potenciales endógenos (>100 ms)   | No requiere entrenamiento, natural en selección de objetivos             | Requiere atención visual; alternativa táctil/auditiva disponible            |

---

## 4. Detección de Gestos Oculares Voluntarios mediante EEG

### 4.1 Análisis comparativo de bases de datos EEG

Se revisaron dos referencias principales:

- *Multimodal Sensor Fusion for EEG-Based BCI Typing Systems (2025)*
- *Assessing the effects of voluntary and involuntary eyeblinks in EEG (2016)*

###  Cuadro comparativo de características

| Característica                  | Base de datos 2025                                  | Base de datos 2016                                  |
|--------------------------------|-----------------------------------------------------|-----------------------------------------------------|
| Calidad de señal               | Alta, multicanal                                    | Moderada, centrada en ICs                          |
| Etiquetado de parpadeos       | Preciso, incluye voluntarios e involuntarios        | Parcial, requiere preprocesamiento                 |
| Compatibilidad con ICA/wavelets| Alta, validado en estudios recientes                | Compatible, pero con menor resolución temporal     |
| Frecuencia de muestreo        | 512 Hz                                              | 256 Hz                                              |
| Número de canales             | 32                                                  | 19                                                  |
| Formato                       | BIDS + anotaciones sincronizadas                    | EDF con etiquetas manuales                         |

---

## 5. Metodología Experimental

### Diseño de ensayos

- **Protocolos**: Parpadeo voluntario e involuntario.
- **Segmentación**: Épocas de 4 segundos.
- **Procesamiento**: ICA mejorado por wavelets + filtrado espacial.
- **Objetivo**: Caracterizar artefactos y diferenciar componentes independientes (ICs) en EEG.

### Comparación metodológica

| Aspecto                         | Ensayo Voluntario                          | Ensayo Involuntario                        |
|---------------------------------|--------------------------------------------|--------------------------------------------|
| Duración de época               | 4 segundos                                 | 4 segundos (excluyendo artefacto marcado)  |
| Aplicación de ICA               | Todo el periodo temporal                   | Todo el periodo temporal                   |
| Exclusión de artefactos        | No aplica                                  | Se excluye segmento marcado con estrella   |
| Tipo de parpadeo               | Controlado por el sujeto                   | Espontáneo o inducido                      |
| Objetivo del análisis          | Separación de ICs y caracterización espectral | Comparación de efectos en ICs              |

---

## 6. Referencias

- Wolpaw et al. (2002) – *Brain-computer interfaces for communication and control*
- Hild et al. (2011) – *ERP-based BCI for text entry*
- Cincotti et al. (2006) – *BCI meeting: hardware and software*
- Gentiletti (2007) – *Estado del arte y desarrollo en Argentina*
- Birbaumer et al. (2003) – *Thought-translation device: mecanismos y resultados clínicos*
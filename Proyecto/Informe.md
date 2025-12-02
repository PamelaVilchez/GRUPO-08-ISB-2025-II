# Sistema BCI P300 Speller con OpenBCI para Asistencia a la Tetraplejia
## 1. Contexto, Justificación y Alcance del Proyecto
### 1.1. Problemática a Abordar
Las Interfaces Cerebro-Computadora (BCI) son esenciales para establecer vías de comunicación y control en personas con limitaciones motoras severas, como la tetraplejia [1]. En Perú, el Consejo Nacional para la Integración de la Persona con Discapacidad (CONADIS) registra 55 534 personas con discapacidad, de las cuales casi el 60% enfrenta una discapacidad severa [4]. Esta población a menudo depende de terceros para tareas básicas, limitando su autonomía e inclusión tecnológica.

### 1.2. Propuesta de Solución: BCI P300 Speller
Se propone desarrollar un sistema BCI no invasivo basado en el potencial P300 utilizando hardware abierto y accesible (Ultracortex Mark IV / OpenBCI). Este sistema permitirá a personas con tetraplejia operar un teclado inalámbrico.

| Característica | Detalle |
|----------------|---------|
| **Hardware**   | Ultracortex Mark IV y OpenBCI: Adquisición portátil de señales EEG/EOG. |
| **Paradigma**  | P300 Speller (Oddball): Matriz 6x6 que parpadea secuencialmente. La atención focalizada en el carácter objetivo genera un P300. |
| **Electrodos** | Centrados en regiones Parietales (Pz) y Centrales (Cz) (zonas responsables de la generación del P300). |
| **Traducción** | La detección y clasificación del P300 traduce la intención mental en un comando de selección de carácter. |

### 1.3. Objetivos a Alcanzar
1. Desarrollar un sistema BCI no invasivo que utilice un EEG portátil (OpenBCI) para registrar la actividad cerebral y los artefactos oculares (EOG).

2. Proponer una solución orientada a mejorar la autonomía de personas con discapacidad motora severa.

## 2. Metodología y Estado del Arte (BCI P300)
### 2.1. Fundamento Neurofisiológico y P300
El P300 es un Potencial Evocado Relacionado con Eventos (ERPs) que se manifiesta como una deflexión positiva en el EEG entre $300 \text{ ms}$ y $600 \text{ ms}$ post-estímulo. Se genera cuando el estímulo es relevante o infrecuente (oddball), sirviendo como un marcador ideal de la intención mental del usuario en un BCI Speller [2].

### 2.2. Manejo de Artefactos y EOG
Las BCI basadas en EEG son susceptibles a artefactos oculares (EOG).

- EOG como Ruido: Tradicionalmente descartado, su detección requiere métodos como la varianza y curtosis en el dominio de la frecuencia [3].

- EOG como Comando: En el contexto de la tetraplejia, los movimientos oculares voluntarios pueden ser una fuente valiosa de control. Herramientas como BLINKER [2] automatizan la extracción de índices oculares (frecuencia, duración, amplitud de parpadeos) a partir de canales EEG/EOG, lo que permite considerarlos para comandos asistivos complementarios.

## 3. Análisis de Señales EEG del P300 (Prueba Piloto)
Se validó la metodología P300 utilizando datos del BIG-P3 BCI Dataset de PhysioNet, enfocándose en la decodificación de caracteres.

### 3.1. Preparación de Datos y Segmentación
El proceso se realizó con mne y pyedflib. Los datos crudos (62 canales) se filtraron para usar solo los 16 canales EEG (identificados como EEG_*).- Detección de Eventos: Se utilizó el canal StimulusCode para identificar las transiciones de $0 \rightarrow \text{valor } (1-12)$, marcando el inicio de cada parpadeo.Eventos detectados: 116 (Test02) y 109 (Test01).
- Epoching: Se segmentó la señal en ventanas de $[-0.1 \text{ s}, 0.8 \text{ s}]$, aplicando corrección de línea base.

### 3.2. Análisis de Amplitud y Decodificación
La cuantificación de la P300 se centró en el canal EEG_Pz (Parietal) en la ventana crítica de $0.3 \text{ s}$ a $0.6 \text{ s}$. El carácter seleccionado es la intersección de la fila y columna con la máxima amplitud P300 promedio.

| Archivo Analizado            | Máxima Amplitud (Fila)     | Máxima Amplitud (Columna)   | Fila y Columna Seleccionadas | Carácter Decodificado |
|------------------------------|----------------------------|-----------------------------|------------------------------|-----------------------|
| J_01_SE001_RC_Test02.edf     | row_5 (5.56×10⁻⁶ V)        | col_4 (1.55×10⁻⁶ V)         | "row_5, col_4"               | 2                     |
| J_01_SE001_RC_Test01.edf     | row_2 (2.27×10⁻⁶ V)        | col_5 (2.92×10⁻⁶ V)         | "row_2, col_5"               | K                     |

### 3.3. Visualización de Potenciales Evocados (EEG_Cz)
El análisis de las respuestas evocadas promedio confirmó la presencia de deflexiones positivas en la ventana del P300, validando la metodología de selección de caracteres por máxima amplitud.

## 4. Conclusiones y Próximos Pasos
### 4.1. Conclusión
La metodología BCI P300 Speller, validada mediante el análisis piloto, demostró ser efectiva en la decodificación de la intención mental del usuario para seleccionar caracteres ('2' y 'K'). La integración de esta metodología con hardware accesible (OpenBCI) tiene el potencial de mejorar significativamente la autonomía y la inclusión de las personas con tetraplejia.

### 4.2. Próximos Pasos Técnicos
Para avanzar hacia la implementación con OpenBCI, las siguientes acciones son prioritarias:
- Preprocesamiento: Implementar filtros de banda (e.g., $0.1 \text{ Hz}$ a $30 \text{ Hz}$) y corrección de artefactos o referenciamiento a la media (CAR) para optimizar la relación señal-ruido.
- Clasificación: Desarrollar un clasificador robusto (e.g., LDA o SVM) para la decodificación en tiempo real de los epochs, esencial para el uso práctico del sistema.
- Traducción de Comandos: Conectar el resultado del clasificador a un Microcontrolador para ejecutar el comando detectado y operar el teclado inalámbrico.

## 5. Referencias Bibliográficas
[1] T. C. A. R. Gentiletti G., “Interfaz Cerebro-Computadora: Estado del arte y desarrollo en Argentina,” Revista Argentina de Bioingeniería, vol. 13, nº 1, pp. 21–29, 2007.
[2] P. F. Camillo S., “P300-based Brain-computer Interface: clinical applications and new possible directions,” en Proceedings of SIMPAR 2010 Workshops. Intl. Conf. on Simulation, Modeling and Programming for Autonomous Robots, Germany, 2010.
[3] Naciones Unidas, "Día Internacional de las Personas con Discapacidad", Naciones Unidas, 2025. Disponible en: $\text{[https://www.un.org/es/observances/day-of-persons-with-disabilities](https://www.un.org/es/observances/day-of-persons-with-disabilities)}$
[4] Observatorio Nacional de la Discapacidad, Consejo Nacional para la Integración de la Persona con Discapacidad (CONADIS), “Discapacidad en cifras”, disponible en: $\text{[https://observatorio.conadisperu.gob.pe/](https://observatorio.conadisperu.gob.pe/)}$

Estado del Arte Adicional:
- MILimbEEG: A dataset of EEG signals related to upper and lower limb execution of motor and motor imagery tasks.
- BLINKER: Automated extraction of ocular indices from eeg enabling large scale analysis (Toolbox disponible en $\text{[https://github.com/VisLab/EEG-Blinks](https://github.com/VisLab/EEG-Blinks)}$).
- Algoritmo con Interfaz Gráfica para la Detección Automática de Artefactos Oculares y Musculares en Señales EEG.
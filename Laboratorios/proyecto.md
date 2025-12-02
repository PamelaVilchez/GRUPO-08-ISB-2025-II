# Sistema BCI con Ultracortex para operar un teclado inalámbrico en personas con tetraplejia

## ⚠️ Problemática a abordar
Las Interfaces Cerebro-Computadora (BCI) son sistemas que permiten establecer una conexión directa entre la actividad cerebral y el entorno, sin necesidad de recurrir a vías nerviosas o musculares convencionales. Estas tecnologías han surgido como alternativas de comunicación y control especialmente dirigidas a personas con limitaciones motoras severas, al traducir señales neurofisiológicas en comandos capaces de interactuar con dispositivos externos [1].

En el caso de las BCI basadas en electroencefalografía (EEG), las señales suelen verse contaminadas por artefactos generados por movimientos oculares y parpadeos [2]. En entornos clínicos este fenómeno se descarta por considerarse “ruido”; sin embargo, puede convertirse en una fuente valiosa de control para aplicaciones asistivas. Esto es posible porque el ojo se comporta como un dipolo eléctrico: la córnea presenta carga positiva y la retina negativa. Al mover los ojos en diferentes direcciones, varía la orientación del dipolo, lo que produce cambios de voltaje detectables en electrodos ubicados alrededor de la zona ocular, fenómeno conocido como electrooculografía (EOG).

Para personas con tetraplejia, que conservan la capacidad de comunicarse verbalmente pero enfrentan limitaciones físicas severas, acciones cotidianas como encender el televisor, cambiar de canal o ajustar el volumen suelen requerir asistencia externa o tecnologías especializadas que no siempre están disponibles o adaptadas a sus necesidades. Esto limita su autonomía y dificulta la interacción directa con el entorno.

### 💡 Propuesta de solución
Sistema BCI no invasivo basado en el potencial P300, utilizando el Ultracortex Mark IV y OpenBCI para adquirir señales EEG que permiten a personas con tetraplejia operar un teclado inalámbrico sin movimiento corporal.
El sistema presenta una matriz de números que se iluminan de forma secuencial (paradigma oddball). Cuando el usuario fija su atención en un número, el estímulo objetivo genera un P300, el cual se detecta en regiones parietales y se traduce en un comando. 

Para la implementación, se utilizará:

- Hardware abierto-accesible: El Ultracortex Mark IV y la plataforma OpenBCI para la adquisición de señales EEG. La configuración de los electrodos se centrará estratégicamente en las regiones parietales y centrales (principalmente Pz, Cz), ya que estas áreas cerebrales son las responsables de la generación del P300, asegurando la captación óptima de la señal de interés.
- **Paradigma Oddball**: El sistema presenta una matriz visual 6x6 que se iluminan en 2 fases secuencialmente (1. Iluminación secuencial de las 6 filas y 2. Iluminación secuencial de las 6 columnas). La atención focalizada del usuario en el carácter objetivo provoca una respuesta cerebral P300 de alta amplitud exclusivamente en el momento en que su fila y su columna son iluminadas (estímulo objetivo).
- Traducción de comandos: La detección y clasificación de este potencial permite traducir la intención mental del usuario en un comando para la selección de un caracter.

Al integrar hardware accesible (Ultracortex/OpenBCI) con una metodología robusta (P300 speller), esta solución no solo proporciona una vía de comunicación esencial sino que también sienta las bases para un sistema de control asistido integral. El objetivo es mejorar significativamente la autonomía, la dignidad y la inclusión tecnológica de las personas con movilidad reducida, convirtiendo la actividad cerebral intencional en una forma práctica y eficiente de interactuar con el mundo.

## 📊 Estadísticas

En la actualidad, más de **1 000 millones de personas** en el mundo enfrenta algún tipo de discapacidad, lo que equivale a 1 de cada 7 personas. De esta población, el 80% reside en países en desarrollo [3]. Nuestro país no es ajeno a esta problemática. Según el Consejo Nacional para la Integración de la Persona con Discapacidad (CONADIS), hasta el 31 de julio de 2025 se registran **55 534 personas con discapacidad en Perú** [4].


<p align="center">
  <img src="../Repositorio-Imágenes/CONADIS_2025.png" alt="CONADIS-2025" width="400"> 
</p>

La gráfica evidencia que casi el **60%** de esta población enfrenta una discapacidad severa, condición que suele involucrar limitaciones motoras graves que obliga a muchas personas a depender de terceros para realizar incluso tareas básicas de comunicación o interacción con dispositivos.


## 🎯 Objetivos a alcanzar

- Desarrollar un sistema BCI no invasivo que utilice un EEG portátil (OpenBCI) para registrar tanto la actividad cerebral como los artefactos oculares (EOG) generados por parpadeos y movimientos oculares voluntarios.
- Proponer una solución orientada a mejorar la autonomía de personas con discapacidad motora severa.

## 🛠️ Herramientas a utilizar

- **Hardware**
  - Open BCI (EEG portátil): adquisición de señales EEG/EOG de manera no invasiva
  - Microcontrolador: módulo encargado de ejecutar los comandos detectados y controlar dispositivos externos.

- **Software**
  - Python


## 📚 Estado del Arte
### 1. MILimbEEG: A dataset of EEG signals related to upper and lower limb execution of motor and motor imagery tasks
La detección precisa y automática de la actividad neuronal de las extremidades superiores e inferiores mediante EEG puede ser útil en la rehabilitación de personas que sufren limitaciones de movilidad o discapacidades.

Este artículo presenta un conjunto de datos que contiene 7440 archivos CSV de 60 sujetos de prueba durante tareas motoras y de imaginería motora.

Las tareas motoras y de imaginería motora realizadas por los sujetos de prueba fueron: cerrar la mano izquierda, cerrar la mano derecha, flexión dorsal del pie izquierdo, flexión plantar del pie izquierdo, flexión dorsal del pie derecho, flexión plantar del pie derecho y descanso entre tareas.

<p align="center">
  <img src="https://github.com/PamelaVilchez/GRUPO-08-ISB-2025-II/blob/f81ee407676b9f5076f90d9550f21e4771a53d5c/Repositorio-Im%C3%A1genes/MILimb_2a.png?raw=true" 
       alt="MILimb_2a" width="400">
</p>

Para garantizar la estandarización al registrar señales de EEG en las diferentes regiones de la corteza cerebral, la Sociedad Americana de Electroencefalografía (AES) definió el sistema internacional 10/10 - 64 electrodos, en el cual los electrodos se colocan en el cuero cabelludo con una separación del 10% entre ellos con respecto a las curvas sagital central y coronal central.

<p align="center">
  <img src="https://github.com/PamelaVilchez/GRUPO-08-ISB-2025-II/blob/f81ee407676b9f5076f90d9550f21e4771a53d5c/Repositorio-Im%C3%A1genes/MILimb_1.png?raw=true" 
       alt="MILimb_1" width="400">
</p>

### 2. BLINKER: Automated extraction of ocular indices from eeg enabling large scale analysis
Proponen un proceso automatizado (BLINKER) para extraer índices oculares como la frecuencia de parpadeo, la duración del parpadeo y las relaciones entre la velocidad y la amplitud del parpadeo a partir de canales EEG, canales EOG
y/o componentes independientes (IC).

También investigan la dependencia de los índices oculares en función de la tarea en un estudio de tiradores. Además, implementaron el algoritmo en un toolbox de MATLAB de libre acceso llamado BLINKER. Este toolbox se puede aplicar a colecciones de datos sin intervención del usuario y permite descubrir cuáles canales o circuitos integrados capturan los parpadeos.

<p align="center">
  <img src="https://github.com/PamelaVilchez/GRUPO-08-ISB-2025-II/blob/e05ba2b68a20814ed54fbd8f4a484695f9b1603f/Repositorio-Im%C3%A1genes/Blinker_1.png?raw=true" 
       alt="Blinker_1" width="400">
</p>

Los índices oculares que se pueden extraer fácilmente del EEG son la frecuencia de parpadeo, la duración del parpadeo, la relación de desviación de la amplitud del parpadeo, la relación de velocidad de amplitud positiva, la relación de velocidad de amplitud negativa, el porcentaje de tiempo con los ojos cerrados, así como las desviaciones estándar, las tasas de cambio y las relaciones de estas medidas.

BLINKER utiliza un umbral para la eliminación de valores atípicos y la selección de la mejor señal para identificar parpadeos. Las señales de los parpadeos tienen forma de carpa y una alta amplitud en relación con la señal de fondo.

<p align="center">
  <img src="https://github.com/PamelaVilchez/GRUPO-08-ISB-2025-II/blob/f81ee407676b9f5076f90d9550f21e4771a53d5c/Repositorio-Im%C3%A1genes/Blinker_2.png?raw=true" 
       alt="Blinker_2" width="400">
</p>

El toolbox está disponible en https://github.com/VisLab/EEG-Blinks.
La documentación para el usuario y los ejemplos se encuentran en http://vislab.github.io/EEG-Blinks/.


### 3. Algoritmo con Interfaz Gráfica para la Detección Automática de Artefactos Oculares y Musculares en Señales EEG
Durante el registro de señales de un electroencefalograma se pueden presentar artefactos oculares y musculares, los cuales llegan a esconder la señal cerebral que se desea analizar; es por ello que proponen un algoritmo con interfaz gráfica, implementada en MATLAB, para la detección automática de dichos artefactos para minimizar el tiempo de procesamiento de señales EEG.

La detección se realiza a través del cálculo de la varianza y la curtosis en el dominio de la frecuencia, para el caso de artefactos oculares, y de la varianza en el dominio del tiempo, para el caso de artefactos musculares. Una vez detectados los artefactos, su eliminación se facilitará y permitirá al usuario agilizar el procesamiento de los datos EEG y realizar con éstos un análisis posterior. 

<p align="center">
  <img src="https://github.com/PamelaVilchez/GRUPO-08-ISB-2025-II/blob/f81ee407676b9f5076f90d9550f21e4771a53d5c/Repositorio-Im%C3%A1genes/algortimo-GUI_1.png?raw=true" 
       alt="algoritmo-GUI_1" width="400">
</p>

Además, se robustecerá el algoritmo de detección de ambos tipos de artefactos en el dominio del tiempo y frecuencia mediante pruebas con series de datos EEG de pacientes con Epilepsia focalizada y generalizada. 

## Referencias
- [1] T. C. A. R. Gentiletti G., “Interfaz Cerebro-Computadora: Estado del arte y desarrollo en Argentina,” Revista Argentina de Bioingeniería, vol. 13, nº 1, pp. 21–29, 2007.
- [2] P. F. Camillo S., “P300-based Brain-computer Interface: clinical applications and new possible directions,” en Proceedings of SIMPAR 2010 Workshops. Intl. Conf. on Simulation, Modeling and Programming for Autonomous Robots, Germany, 2010.
- [3] Naciones Unidas, "Día Internacional de las Personas con Discapacidad", Naciones Unidas, 2025. Disponible en: https://www.un.org/es/observances/day-of-persons-with-disabilities

- [4] Observatorio Nacional de la Discapacidad, Consejo Nacional para la Integración de la Persona con Discapacidad (CONADIS), “Discapacidad en cifras”, disponible en: https://observatorio.conadisperu.gob.pe/















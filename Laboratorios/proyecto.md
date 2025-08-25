# Detección en Tiempo Real de Parpadeos Oculares para Control de Dispositivos mediante EEG



## Problemática a abordar

Las Interfaces Cerebro-Computadora (BCI) son sistemas que permiten establecer una conexión directa entre la actividad cerebral y el entorno, sin necesidad de recurrir a vías nerviosas o musculares convencionales. Estas tecnologías han surgido como alternativas de comunicación y control especialmente dirigidas a personas con limitaciones motoras severas, al traducir señales neurofisiológicas en comandos capaces de interactuar con dispositivos externos [1]. 

En el caso de las BCI basadas en electroencefalografía (EEG), las señales suelen verse contaminadas por artefactos generados por movimientos oculares y parpadeos [2]. En entornos clínicos este fenómeno se descarta por considerarse “ruido”; sin embargo, puede convertirse en una fuente valiosa de control para aplicaciones asistivas. Esto es posible porque el ojo se comporta como un dipolo eléctrico: la córnea presenta carga positiva y la retina negativa. Al mover los ojos en diferentes direcciones, varía la orientación del dipolo, lo que produce cambios de voltaje detectables en electrodos ubicados alrededor de la zona ocular, fenómeno conocido como electrooculografía (EOG). 

De esta manera, un sistema EEG portátil también puede registrar señales EOG, permitiendo identificar en tiempo real parpadeos o movimientos oculares y traducirlos en comandos simples brindando autonomía a personas con limitaciones motoras graves sin necesidad de complejos paradigmas cognitivos o costosos sistemas invasivos.




### 📊 Estadísticas

En la actualidad, más de **1 000 millones de personas** en el mundo enfrenta algún tipo de discapacidad, lo que equivale a 1 de cada 7 personas. De esta población, el 80% reside en países en desarrollo [3]. Nuestro país no es ajeno a esta problemática. Según el Consejo Nacional para la Integración de la Persona con Discapacidad (CONADIS), hasta el 31 de julio de 2025 se registran **55 534 personas con discapacidad en Perú** [4].


<p align="center">
  <img src="../Repositorio-Imágenes/CONADIS_2025.png" alt="CONADIS-2025" width="400"> 
</p>

La gráfica evidencia que casi el **60%** de esta población enfrenta una discapacidad severa, condición que suele involucrar limitaciones motoras graves que obliga a muchas personas a depender de terceros para realizar incluso tareas básicas de comunicación o interacción con dispositivos.


## Objetivos a alcanzar
- Detectar parpadeos oculares en tiempo real mediante señales EEG.
- Traducir estos eventos en comandos para controlar dispositivos electrónicos.
- Evaluar la precisión, latencia y robustez del sistema en condiciones reales.
- Proponer una solución accesible, portátil y replicable para usuarios con discapacidad motora.

## Herramientas a utilizar
- Sensor EEG (OpenBCI o similar): dispositivo de adquisición de señales cerebrales, que actúa como el sensor principal para detectar actividad eléctrica relacionada con parpadeos.
- Python: lenguaje principal para el procesamiento de señales, desarrollo de algoritmos de detección y control.

## Referencias
- [1] T. C. A. R. Gentiletti G., “Interfaz Cerebro-Computadora: Estado del arte y desarrollo en Argentina,” Revista Argentina de Bioingeniería, vol. 13, nº 1, pp. 21–29, 2007.
- [2] P. F. Camillo S., “P300-based Brain-computer Interface: clinical applications and new possible directions,” en Proceedings of SIMPAR 2010 Workshops. Intl. Conf. on Simulation, Modeling and Programming for Autonomous Robots, Germany, 2010.
- [3] Naciones Unidas, "Día Internacional de las Personas con Discapacidad", Naciones Unidas, 2025. Disponible en: https://www.un.org/es/observances/day-of-persons-with-disabilities

- [4] Observatorio Nacional de la Discapacidad, Consejo Nacional para la Integración de la Persona con Discapacidad (CONADIS), “Discapacidad en cifras”, disponible en: https://observatorio.conadisperu.gob.pe/

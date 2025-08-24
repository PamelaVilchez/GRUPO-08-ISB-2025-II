# Detección en Tiempo Real de Parpadeos Oculares para Control de Dispositivos mediante EEG



## Problemática a abordar
Las Interfaces Cerebro-Computadora (BCI) son sistemas computacionales que permiten establecer una conexión directa entre la actividad cerebral de un individuo y su entorno, sin necesidad de utilizar vías nerviosas o musculares convencionales. Estas interfaces surgen como respuesta a la necesidad de crear nuevos canales de comunicación para personas con limitaciones motoras severas, facilitando su interacción con dispositivos mediante señales neurofisiológicas [1].
Las BCI se fundamentan en la adquisición y procesamiento de señales cerebrales asociadas a procesos cognitivos, utilizando tecnologías como EEG (electroencefalografía), MEG (magnetoencefalografía) o fMRI (imagen por resonancia magnética funcional). Gracias a estos métodos, es posible interpretar intenciones del usuario y traducirlas en comandos que permiten controlar actuadores o sistemas externos, abriendo nuevas posibilidades en el ámbito clínico y de asistencia tecnológica [2].



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
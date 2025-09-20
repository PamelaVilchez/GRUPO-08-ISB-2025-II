- [1. Introducción](#1-introducción)
- [2. Objetivos del laboratorio](#2-objetivos-del-laboratorio)

- [7. Referencias](#7-referencias)

# 1. Introducción 
El electroencefalograma (EEG) es una técnica neurofisiológica no invasiva que permite registrar la actividad eléctrica de las neuronas 
corticales mediante electrodos ubicados en el cuero cabelludo. Esta actividad se manifiesta en forma de ondas cerebrales, caracterizadas 
por su frecuencia y amplitud, parámetros que reflejan los distintos estados funcionales del cerebro [1].

Las principales bandas de frecuencia del EEG son: delta (δ), theta (θ), alfa (α) y beta (β), cada una asociada a condiciones específicas 
como el sueño profundo, la relajación, el reposo vigilante o la actividad cognitiva intensa. Aunque el EEG no permite evaluar directamente 
la actividad de estructuras profundas como el tronco encefálico o el cerebelo, constituye una herramienta esencial para el estudio de la 
dinámica cortical, tanto en condiciones de reposo como durante la ejecución de tareas [1].

Además de su valor en la investigación neurocientífica, el EEG tiene una amplia aplicación clínica, ya que permite detectar alteraciones 
en la actividad cerebral que pueden contribuir al diagnóstico de epilepsia, trastornos convulsivos, encefalopatías y otras disfunciones 
neurológicas [2].



# 2. Objetivos del laboratorio 
- Configurar adecuadamente el dispositivo BITalino (r)evolution Board Kit BLE/BT para la adquisición de señales EEG, garantizando la correcta colocación de los electrodos y la calidad de la señal registrada.
- Registrar señales EEG en diferentes condiciones experimentales: reposo, fijación visual, ojos cerrados, ejecución de una tarea cognitiva y durante una actividad libre.
- Preprocesar las señales EEG mediante la aplicación de un filtro pasa banda entre 0.8–48 Hz, con el fin de eliminar artefactos y aislar la actividad cerebral de interés.
- Identificar y analizar las principales bandas de frecuencia de la señal EEG (δ, θ, α y β), asociando cada una de ellas con los estados y actividades registradas.
- Implementar el análisis de señales EEG utilizando Python y el software OpenSignals, desarrollando un flujo de trabajo reproducible para la visualización e interpretación de los resultados.

# 3. Materiales 
| Equipo / material     | Cantidad |
|:-----------:|:--------:|
| BITalino Board BLE/BT |    1     |
| Laptop con Bluetooth 4.0+|    1     |
| Software OpenSignals |    -     |
| Electrodos Ag/AgCl (gel) |    3     |
| Ultracortex Mark IV (dry headset) |    1     |

### Seguridad y buenas prácticas
- Operar solo con batería (no mientras carga).
- Evitar piel lesionada y pacientes con implantes.
- Desinfección previa y retiro de objetos metálicos.
- Registrar artefactos (parpadeo, masticación) en cuaderno o video.
- Impedancia < 20 kΩ recomendada.


# 4. Metodología
## 4.1.1. Conexión de los electrodos
Antes del inicio del registro EEG, se procedió a la colocación de los electrodos siguiendo el sistema internacional 10–20, adaptado para configuración frontal [3]. Se utilizaron electrodos de tipo Ag/AgCl con gel conductor, asegurando una buena adherencia y baja impedancia de contacto.
El montaje se realizó de la siguiente manera:
- Electrodo activo: ubicado en la región Fp1, correspondiente al lóbulo frontal izquierdo. Esta posición permite captar actividad cortical relacionada con atención, parpadeo y procesamiento cognitivo.
- Electrodo de referencia: colocado en la mastoide derecha, zona ósea detrás de la oreja, utilizada para estabilizar la señal y reducir interferencias.
- Electrodo de tierra (GND): ubicado en Fp2, región frontal derecha, con el fin de cerrar el circuito de adquisición y minimizar el ruido eléctrico.
Previo a la colocación, se realizó limpieza de la piel con alcohol isopropílico y se verificó que el participante no tuviera objetos metálicos ni lesiones en las zonas de contacto. La impedancia fue medida y ajustada para mantenerse por debajo de los 20 kΩ, garantizando una señal estable y libre de artefactos por contacto deficiente.
Este montaje permitió obtener registros confiables en condiciones de reposo, estimulación visual, actividad cognitiva y presencia de artefactos inducidos, facilitando el análisis comparativo entre diferentes estados fisiológicos.

<p align="center">
  <img src="../../Repositorio-Imágenes/Lab5_electrodos.jpeg" alt="Colocación de electrodos según el sistema internacional 10-20" width="400" height="400"/>
</p>
 
## 4.1.2. Prueba 1 – Bloque repetido (reposo, fijación visual y ojos cerrados)
Se registró la señal EEG del participante en tres ciclos consecutivos, cada uno compuesto por una fase de reposo con ojos cerrados y con aislamiento visual (30 segundos), una fase de fijación visual hacia un objeto (2 minutos) y una fase de descanso con ojos cerrados (30 segundos). Este bloque repetido tuvo como objetivo establecer una línea de base estable y observar la modulación de ritmos cerebrales, especialmente en la banda alfa, bajo condiciones de estimulación visual controlada y relajación. La repetición del ciclo permitió obtener datos consistentes y comparables entre estados de activación y reposo.

## 4.1.3. Prueba 2 – Tarea cognitiva (resta de 100–7)
El participante realizó una tarea de cálculo mental que consistió en restar secuencialmente el número 7 desde 100, de forma mental, evitando gestos lo cual implica un movimiento muscular y por ende un artefacto para el experimento. Esta actividad se llevó a cabo 1 vez, con el propósito de inducir una mayor exigencia y evaluar el incremento de potencia en bandas rápidas, particularmente beta, la encargada de la actividad cognitiva. Se registró el número final alcanzado por el participante como referencia para trazabilidad cognitiva.

## 4.1.4. Prueba 3 – Artefactos inducidos (parpadeo + masticación)
Durante esta prueba, el participante realizó parpadeos voluntarios cada 2 segundos mientras masticaba de forma continua, sin alimento, durante tres bloques de 1 minuto cada uno. Esta combinación de movimientos oculares y musculares permitió generar artefactos complejos en la señal EEG, útiles para validar la sensibilidad del sistema y entrenar algoritmos de detección y limpieza. Se documentó la frecuencia de parpadeo y se verificó la presencia de interferencias en el canal frontal

## 4.1.5. Prueba 4 – Estimulación libre con música
En esta etapa, se expuso al participante a dos condiciones auditivas contrastantes: primero, una canción de heavy metal con alta carga sensorial; luego, una pieza musical seleccionada por el propio participante según sus preferencias personales. Cada estímulo tuvo una duración aproximada de 2 a 4 minutos, dependiendo de la duración de la canción. El objetivo fue observar la modulación emocional y su impacto en bandas beta y gamma. Se registraron el tipo de música, el volumen y un auto-reporte emocional para complementar el análisis.


# 5. Señales ploteadas en Python



##### - Archivos EEG:


# 6. Discusión de resultados


# 7. Referencias
- [1] “Electroencefalograma | ¿Qué es un electroencefalograma”, Portal CLÍNIC, Hospital Clínic de Barcelona, 27 abril 2022; actualizado el 20 marzo 2025. Disponible en: https://www.clinicbarcelona.org/asistencia/pruebas-y-procedimientos/electroencefalograma.
- [2] “Electroencefalografía (EEG) – Mayo Clinic,” Mayo Clinic, 18-sep-2024. Disponible en: https://www.mayoclinic.org/es/tests-procedures/eeg/about/pac-20393875. 
 - [3] M. Proença and K. Mrotzeck, BITalino Home Guide #3 – Electroencephalography (EEG): Exploring Brain Signals, PLUX – Wireless Biosignals, S.A., Lisbon, Portugal, Feb. 2021.






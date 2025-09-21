 # Índice
- [1. Introducción](#1-introducción)
- [2. Objetivos del laboratorio](#2-objetivos-del-laboratorio)

- [5. Señales ploteadas en Python](#5-señales-ploteadas-en-python)
  - [Señales EEG obtenidas del BITalino](#señales-eeg-obtenidas-del-bitalino)
    - [Señal EEG basal (Reposo)](#señal-eeg-basal-reposo)
    - [Señal EEG con ojos abiertos](#señal-eeg-con-ojos-abiertos)
    - [Señal EEG con ojos cerrados](#señal-eeg-con-ojos-cerrados)
    - [Señal EEG restando 7 desde 100](#señal-eeg-restando-7-desde-100)
    - [Señal EEG con artefactos](#señal-eeg-con-artefactos)
    - [Señal EEG escuchando música](#señal-eeg-escuchando-música)
      - [Género Rock](#rock)
      - [Género Pop](#pop)
  - [Gráficas de OpenBCI](#gráficas-de-openbci)
    - [Gráfica de las señales de los 8 canales](#gráfica-de-las-señales-de-los-8-canales)
    - [Frecuencias de los 8 canales](#frecuencias-de-los-8-canales)
    - [Frecuencias de los 8 canales superpuestas](#frecuencias-de-los-8-canales-superpuestas)
- [6. Discusión de resultados](#6-discusion-de-resultados)
  - [6.1 Discusión de resultados OpenBCI - BITalino](#61-discusion-de-resultados-openbci---bitalino)
  - [6.2 Discusión de resultados OpenBCI - Ultracortex](#62-discusion-de-resultados-openbci---ultracortex)
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

<p align="center">
  <img src="../../Repositorio-Imágenes/Lab3_kit_BITalino.jpeg" alt="Kit BITalino" width="400" height="400"/>
</p>

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

<figure style="text-align: center;">
  <img src="../../Repositorio-Imágenes/Lab5_electrodos.jpg" alt="Reposo 1" width="500" height="500"/>
  <figcaption>Imagen 1. Posicionamiento de los electrodos según sistema 10-20</figcaption>
</figure>
 
## 4.1.2. Prueba 1 – Bloque repetido (reposo, fijación visual y ojos cerrados)
Se registró la señal EEG del participante en tres ciclos consecutivos, cada uno compuesto por una fase de reposo con ojos cerrados y con aislamiento visual (30 segundos), una fase de fijación visual hacia un objeto (2 minutos) y una fase de descanso con ojos cerrados (30 segundos). Este bloque repetido tuvo como objetivo establecer una línea de base estable y observar la modulación de ritmos cerebrales, especialmente en la banda alfa, bajo condiciones de estimulación visual controlada y relajación. La repetición del ciclo permitió obtener datos consistentes y comparables entre estados de activación y reposo.

<figure style="text-align: center;">
  <img src="../../Repositorio-Imágenes/Lab5_reposo1.gif" alt="Reposo 1" width="500" height="500"/>
  <figcaption>GIF 1. Estado de reposo inicial</figcaption>
</figure>

<figure style="text-align: center;">
  <img src="../../Repositorio-Imágenes/Lab5_fijar.gif" alt="Fijación" width="500" height="500"/>
  <figcaption>GIF 2. Fijación del Objeto</figcaption>
</figure>

<figure style="text-align: center;">
  <img src="../../Repositorio-Imágenes/Lab5_reposo2.gif" alt="Reposo 1" width="500" height="500"/>
  <figcaption>GIF 3. Estado de reposo final</figcaption>
</figure>
 
## 4.1.3. Prueba 2 – Tarea cognitiva (resta de 100–7)
El participante realizó una tarea de cálculo mental que consistió en restar secuencialmente el número 7 desde 100, de forma mental, evitando gestos lo cual implica un movimiento muscular y por ende un artefacto para el experimento. Esta actividad se llevó a cabo 1 vez, con el propósito de inducir una mayor exigencia y evaluar el incremento de potencia en bandas rápidas, particularmente beta, la encargada de la actividad cognitiva. Se registró el número final alcanzado por el participante como referencia para trazabilidad cognitiva.

<figure style="text-align: center;">
  <img src="../../Repositorio-Imágenes/Lab5_resta.gif" alt="Reposo 1" width="500" height="500"/>
  <figcaption>GIF 4. Resta de 100 - 7 consecutivade manera mental</figcaption>
</figure>

## 4.1.4. Prueba 3 – Artefactos inducidos (parpadeo + masticación)
Durante esta prueba, el participante realizó parpadeos voluntarios cada 2 segundos mientras masticaba de forma continua, sin alimento, durante tres bloques de 1 minuto cada uno. Esta combinación de movimientos oculares y musculares permitió generar artefactos complejos en la señal EEG, útiles para validar la sensibilidad del sistema y entrenar algoritmos de detección y limpieza. Se documentó la frecuencia de parpadeo y se verificó la presencia de interferencias en el canal frontal.

<figure style="text-align: center;">
  <img src="../../Repositorio-Imágenes/Lab5_masticar.gif" alt="Reposo 1" width="500" height="500"/>
  <figcaption>GIF 5. Ejercicio de parpadeo y masticación a la misma vez</figcaption>
</figure>

## 4.1.5. Prueba 4 – Estimulación libre con música
En esta etapa, se expuso al participante a dos condiciones auditivas contrastantes: primero, una canción de heavy metal con alta carga sensorial; luego, una pieza musical seleccionada por el propio participante según sus preferencias personales. Cada estímulo tuvo una duración aproximada de 2 a 4 minutos, dependiendo de la duración de la canción. El objetivo fue observar la modulación emocional y su impacto en bandas beta y gamma. Se registraron el tipo de música, el volumen y un auto-reporte emocional para complementar el análisis.

<figure style="text-align: center;">
  <img src="../../Repositorio-Imágenes/Lab5_musica.gif" alt="Reposo 1" width="500" height="500"/>
  <figcaption>GIF 6. Ejercicio de estimulación según el tipo de música</figcaption>
</figure>


# 5. Señales ploteadas en Python
## Señales EEG obtenidas del BITalino
#### Señal EEG basal (Reposo)
Se cubrió al usario con una manta y se le cubrieron los oídos para evitar interferencias, como consecuencias de los potenciales generados, en la señal basal. 

<p align="center">
  <img src="https://github.com/PamelaVilchez/GRUPO-08-ISB-2025-II/blob/4d90058c1213571f1e10639ba62aceb412aabfc6/Repositorio-Im%C3%A1genes/reposo1.jpg?raw=true" 
       alt="b_reposo" height="300" width="500">
</p>
<p align="center">
  <img src="https://github.com/PamelaVilchez/GRUPO-08-ISB-2025-II/blob/4d90058c1213571f1e10639ba62aceb412aabfc6/Repositorio-Im%C3%A1genes/reposo2.jpg?raw=true" 
       alt="b_reposo" height="300" width="500">
</p>
<p align="center">
  <img src="https://github.com/PamelaVilchez/GRUPO-08-ISB-2025-II/blob/4d90058c1213571f1e10639ba62aceb412aabfc6/Repositorio-Im%C3%A1genes/reposo3.jpg?raw=true" 
       alt="b_reposo" height="300" width="500">
</p>

#### Señal EEG con ojos abiertos
El usuario permaneció mirando fijamente la pared, aunque ya no llevaba los oídos cubiertos.

<p align="center">
  <img src="https://github.com/PamelaVilchez/GRUPO-08-ISB-2025-II/blob/4d90058c1213571f1e10639ba62aceb412aabfc6/Repositorio-Im%C3%A1genes/abierto1.jpg?raw=true" 
       alt="b_reposo" height="300" width="500">
</p>
<p align="center">
  <img src="https://github.com/PamelaVilchez/GRUPO-08-ISB-2025-II/blob/4d90058c1213571f1e10639ba62aceb412aabfc6/Repositorio-Im%C3%A1genes/abierto2.jpg?raw=true" 
       alt="b_reposo" height="300" width="500">
</p>
<p align="center">
  <img src="https://github.com/PamelaVilchez/GRUPO-08-ISB-2025-II/blob/4d90058c1213571f1e10639ba62aceb412aabfc6/Repositorio-Im%C3%A1genes/abierto3.jpg?raw=true" 
       alt="b_reposo" height="300" width="500">
</p>con 

#### Señal EEG con ojos cerrados
El usuario permaneció con los ojos cerrados, aunque ya no llevaba los oídos ni los ojos cubiertos.

<p align="center">
  <img src="https://github.com/PamelaVilchez/GRUPO-08-ISB-2025-II/blob/4d90058c1213571f1e10639ba62aceb412aabfc6/Repositorio-Im%C3%A1genes/cerrado1.jpg?raw=true" 
       alt="b_reposo" height="300" width="500">
</p>
<p align="center">
  <img src="https://github.com/PamelaVilchez/GRUPO-08-ISB-2025-II/blob/4d90058c1213571f1e10639ba62aceb412aabfc6/Repositorio-Im%C3%A1genes/cerrado2.jpg?raw=true" 
       alt="b_reposo" height="300" width="500">
</p>
<p align="center">
  <img src="https://github.com/PamelaVilchez/GRUPO-08-ISB-2025-II/blob/4d90058c1213571f1e10639ba62aceb412aabfc6/Repositorio-Im%C3%A1genes/cerrado3.jpg?raw=true" 
       alt="b_reposo" height="300" width="500">
</p>

#### Señal EEG restando 7 desde 100 
Se le solicitó al usuario restar mentalmente 7 desde el número 100. No se permitió que utilizará sus manos para contar ni que pudiera hablar.

<p align="center">
  <img src="https://github.com/PamelaVilchez/GRUPO-08-ISB-2025-II/blob/4d90058c1213571f1e10639ba62aceb412aabfc6/Repositorio-Im%C3%A1genes/restar100.jpg?raw=true" 
       alt="b_reposo" height="300" width="500">
</p>

#### Señal EEG con artefactos
Se le solicitó al usuario masticar constantemente y pestañear cada 2 segundos aproximadamente, para observar la señal generada por dichos artefactos.
<p align="center">
  <img src="https://github.com/PamelaVilchez/GRUPO-08-ISB-2025-II/blob/4d90058c1213571f1e10639ba62aceb412aabfc6/Repositorio-Im%C3%A1genes/pYm1.jpg?raw=true" 
       alt="b_reposo" height="300" width="500">
</p>
<p align="center">
  <img src="https://github.com/PamelaVilchez/GRUPO-08-ISB-2025-II/blob/4d90058c1213571f1e10639ba62aceb412aabfc6/Repositorio-Im%C3%A1genes/pYm2.jpg?raw=true" 
       alt="b_reposo" height="300" width="500">
</p>
<p align="center">
  <img src="https://github.com/PamelaVilchez/GRUPO-08-ISB-2025-II/blob/4d90058c1213571f1e10639ba62aceb412aabfc6/Repositorio-Im%C3%A1genes/pYm3.jpg?raw=true" 
       alt="b_reposo" height="300" width="500">
</p>

#### Señal EEG escuchando música 
El usuario permaneció sentado con los ojos abiertos y utilizando audífonos, los  cuales reproducieron una canción de rock estruendosa y su canción favorita que pertenecía al género musical de pop.

###### Género Rock
<p align="center">
  <img src="https://github.com/PamelaVilchez/GRUPO-08-ISB-2025-II/blob/873b99537a91122debbc6cf6e3359c13b741b7e5/Repositorio-Im%C3%A1genes/mRock.jpg?raw=true" 
       alt="b_reposo" height="300" width="500">
</p>

###### Género Pop
<p align="center">
  <img src="https://github.com/PamelaVilchez/GRUPO-08-ISB-2025-II/blob/4d90058c1213571f1e10639ba62aceb412aabfc6/Repositorio-Im%C3%A1genes/mFav.jpg?raw=true" 
       alt="b_reposo" height="300" width="500">
</p>

## Gráficas de OpenBCI
### Gráfica de las señales de los 8 canales
Señales en uV leídas en los 8 canales del Ultracortex.
<p align="center">
  <img src="https://github.com/PamelaVilchez/GRUPO-08-ISB-2025-II/blob/30dc3ec60751fa2ed8001b767dbbae8b83a732a7/Repositorio-Im%C3%A1genes/se%C3%B1alesBCI.jpg?raw=true" 
       alt="MILimb_2a" >
</p>

### Frecuencias de los 8 canales
Frecuencias de cada canal en Hz versus magnitud en dB.
<p align="center">
  <img src="https://github.com/PamelaVilchez/GRUPO-08-ISB-2025-II/blob/7599216c21ee284c7f949140bd29338d69a1b80b/Repositorio-Im%C3%A1genes/frecuencias_openBCI.jpg?raw=true" 
       alt="MILimb_2a" >
</p>

#### Frecuencias de los 8 canales superpuestas
Frecuencias de cada canal en Hz versus magnitud en dB superpuestas.
<p align="center">
  <img src="https://github.com/PamelaVilchez/GRUPO-08-ISB-2025-II/blob/7599216c21ee284c7f949140bd29338d69a1b80b/Repositorio-Im%C3%A1genes/f_superpuestas_openBCI.jpg?raw=true" 
       alt="MILimb_2a" width="500">
</p>

##### - Archivos EEG:
[Archivos-Eeg](https://github.com/PamelaVilchez/GRUPO-08-ISB-2025-II/tree/dea9ccd5c8fe10b70f42ff90bb250261a728159b/Repositorio-Im%C3%A1genes/Archivos_EEG)

# 6. Discusión de resultados

La interpretación de las señales de electroencefalografía (EEG) se basa en la identificación de las ondas cerebrales dentro del espectro de frecuencias. La clasificación en diferentes bandas como se resume en la Tabla 1, representan diversos estados de conciencia y actividad cognitiva. Mediante la Transformada Rápida de Fourier (FFT) es posible descomponer la señal y analizar la presencia de cada componente frecuencial, lo que resulta fundamental para relacionar la actividad cerebral registrada con los estados reportados en la literatura [4]

<p align="center">

| Ondas cerebrales |  Frecuencia | Descripción |
|:-------------:|:-------------:|-------------|
| Onda δ | 1-4 Hz | Etapa de sueño profundo |
| Onda θ | 4-8 Hz | Etapa de somnolencia, relajación profunda |
| Onda α | 8-12 Hz | Etapa de reposo |
| Onda β | 12-30 Hz | Etapa de concentración (actividad mental intensa), resolución de problemas |
| Onda γ | >30 Hz | Etapa de extrema concentración o momentos altamente estresantes |

 *Tabla 1*
</p>

De esta manera, además de identificar las bandas cerebrales en el espectro de frecuencia, es importante considerar la localización de los electrodos, ya que distintas regiones corticales muestran patrones característicos. Por ejemplo, en FP1/FP2 la presencia de actividad en la banda beta puede asociarse con estrés o concentración; en C3/C4 la activación suele vincularse con tareas motoras, siendo relevante en neurorehabilitación. En la región temporal (T5/T6), los picos en la banda theta se relacionan con procesos de memoria o relajación profunda, mientras que en O1/O2 es común observar picos en la banda alpha (~10 Hz), característicos de un estado de reposo visual con los ojos cerrados [5].

| Localización de los electrodos | Importancia |
| ----- | ----- |
| <img src="../../Repositorio-Imágenes/Lab5_electrodos.png" alt="EEG 19 electrodos" height="400" width="400"/> | <img src="../../Repositorio-Imágenes/electrodos_ultracortex.png" alt="Electrodos ultracortex" height="400" width="400"/> |
| *Figura 1. Diagrama que muestra la colocación de los 19 electrodos en el cuero cabelludo usados para los registros EEG [6].* | *Figura 2. Ubicación de los electrodos. Extraído de Manual básico para enfermeros en electroencefalografía [7]* |


## 6.1 Discusión de resultados OpenBCI - BITalino

- **Señal EEG en reposo**: En el gráfico n° 3 se observan la presencia de picos alrededor de 3 Hz (ondas δ) y 9 Hz (ondas α). Es así, que el pico en 9 Hz es característico de un estado de relajación con los ojos cerrados. Sin embargo, el pico de 3 Hz es más probable que sea debido a un artefacto (movimiento corporal o interferencia externa) ya que esta última suele ser dominante en el sueño profundo. 
- **Señal EEG con mirada fija y ojos abiertos**: En el gráfico n.° 3 se observa actividad predominante en el rango de 15–30 Hz (ondas β). Este patrón refleja un estado de alerta y atención sostenida, ya que al mantener la mirada fija el cerebro activa redes corticales vinculadas al procesamiento de la información visual. No obstante, la señal presenta cierta contaminación por artefactos, probablemente originados por movimientos oculares (parpadeo) o por la actividad muscular facial. Estos factores son comunes en registros EEG cuando se trabaja con tareas que requieren control ocular.
- **Señal EEG con los ojos cerrados**: En el gráfico n.° 2 se aprecia un patrón oscilatorio en el rango de 8–12 Hz (ondas α), tal como se espera en condiciones de reposo y relajación. Además, la señal muestra oscilaciones abruptas, repetidas de alta amplitud probablemente originadas por artefactos en los músculos extraoculares.
- **Señal EEG restando 7 desde 100**: En el gráfico, la señal EEG evidencia la complejidad de la actividad cerebral durante una tarea cognitiva demandante. La señal sin filtrar resulta prácticamente ilegible debido al alto nivel de ruido y artefactos, lo cual puede atribuirse a la tensión muscular facial, micro-movimientos de labios o incluso a la postura corporal mantenida bajo esfuerzo mental. Tras aplicar el filtrado, se distinguen variaciones en el dominio del tiempo que sugieren un incremento en la actividad de alta frecuencia (ondas β y γ). Estas oscilaciones están asociadas a procesos de atención, concentración y razonamiento lógico, lo cual respalda la hipótesis de que la tarea de cálculo activa circuitos corticales de mayor demanda.
- **Señal EEG de música rock vs pop**: El registro muestra diferencias claras entre las condiciones musicales. Durante la escucha de música rock, la señal aparece más estable y menos contaminada por artefactos, lo que sugiere una menor participación de la musculatura facial y corporal, posiblemente porque el sujeto no experimentó una respuesta emocional significativa. En contraste, la señal registrada al escuchar música pop presenta picos de mayor amplitud distribuidos a lo largo del tiempo, lo que puede reflejar tanto una respuesta emocional intensa como la aparición de artefactos de movimiento (cabeceo, tarareo, gesticulación o activación muscular involuntaria). Este patrón sugiere que la experiencia subjetiva frente a distintos géneros musicales influye directamente en el nivel de ruido electromiográfico registrado por el EEG.





## 6.2 Discusión de resultados OpenBCI - Ultracortex

### Análisis en el dominio del tiempo
- **Canales frontales (FP1/FP2)**: Las señales presentan una deriva ascendente de la línea base un fenómeno de baja frecuencia que genera que la señal se desplace hacia arriba o abajo gradualmente. Esto suele ser producto de una mala conexión de los electrodos frontales debido a movimientos oculares como parpadeos o movimientos oculares laterales [8].
- **Canales centrales (C3/C4)**: El canal C3 exhibe picos de alta frecuencia y amplitud debido a artefactos de actividad muscular por lo que, se visualizan como fluctuaciones rápidas e irregulares. En contraste, el canal C4 exhibe una señal más estable, lo que sugiere una menor interferencia muscular [8].
- **Canales temporales (T5/T6)**: El canal T5 exibe picos similares a los del canal C3 lo que podría indicar presencia de artefactos de actividad muscular o incluso artefactos oculares de movimientos laterales de los ojos. El canal T6, exhibe una señal relativamente estable facilitando el análisis cerebral del lóbulo temporal.
- **Canales occipitales (O1/O2)**: El canal O1 exhibe picos similares al de los canales C3 y T5 sugiriendo que podrían ser eventos de origen común como un movimiento brusco de la cabeza o un parpadeo. La señal del canal O2 es de baja amplitud sugiriéndonos que se pudo dar por una mala conexión del electrodos.

### Análisis en el dominio de la frecuencia
- **Canales occipitales (O1/O2)**: Estos canales son los más relevantes para analizar la actividad cerebral de las ondas α cuando una persona se encuentra en estado de reposo con los ojos cerrados por lo que se esperaría un pico de potencia significativo en el rango de 8-12 Hz. En este caso, no se visualiza un pico prominente, lo que podría significar que el sujeto tenía los ojos abiertos al momento de registrar la señal.



# 7. Referencias
- [1] de Riquer AI, Ventura CG. ¿Qué es un electroencefalograma [Internet]. Clínic Barcelona. [citado el 20 de septiembre de 2025]. Disponible en: https://www.clinicbarcelona.org/asistencia/pruebas-y-procedimientos/electroencefalograma.
- [2] Electroencefalografía (EEG) [Internet]. Mayoclinic.org. [citado el 20 de septiembre de 2025]. Disponible en: https://www.mayoclinic.org/es/tests-procedures/eeg/about/pac-20393875  
 - [3] M. Proença and K. Mrotzeck, BITalino Home Guide #3 – Electroencephalography (EEG): Exploring Brain Signals, PLUX – Wireless Biosignals, S.A., Lisbon, Portugal, Feb. 2021.
 - [4] Neuroscenter. Ondas Cerebrales: Tipos de Ondas, Desequilibrios y Tratamientos [Internet]. Barcelona/Girona: Neuroscenter; [citado 20 de septiembre de 2025]. Disponible en: https://neuroscenter.com/neurofeedback/ondas-cerebrales/
 - [5] Teresa Talamillo García. Manual básico para enfermeros en electroencefalografía [Internet]. Enfermera Docente. 2011;94:29-33. Disponible en: https://es.scribd.com/document/354810519/ED-094-07-pdf
 - [6] Babiloni C, Triggiani AI, Lizio R, Cordone S, Tattoli G, Bevilacqua V, et al. Classification of single normal and Alzheimer’s disease individuals from cortical sources of resting state EEG rhythms. Front Neurosci [Internet]. 2016;10:47. Disponible en: http://dx.doi.org/10.3389/fnins.2016.00047
 - [7] Ed 094 07 PDF [Internet]. Scribd. [citado el 21 de septiembre de 2025]. Disponible en: https://www.scribd.com/document/354810519/ED-094-07-pdf
 - [8] Jiang, X., Bian, G. B., & Tian, Z. (2019). Removal of Artifacts from EEG Signals: A Review. Sensors (Basel, Switzerland), 19(5), 987. https://doi.org/10.3390/s19050987
 - 









































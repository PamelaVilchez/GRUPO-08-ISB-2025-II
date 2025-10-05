
## Índice
1. [Introducción](#1-introducción)  
2. [Objetivos Específicos](#2-objetivos-específicos)  
3. [Elección de la familia de Wavelet](#3-elección-de-la-familia-de-wavelet)  
   - [EMG](#31-emg)  
   - [ECG](#32-ecg)  
   - [EEG](#33-eeg)  
4. [Resultados](#4-resultados)  
   - [Parámetros del Filtro](#41-parámetros-del-filtro)  
5. [Discusión](#5-discusión)  
   - [Señal ECG](#51-discusión-de-la-señal-ecg)  
   - [Señal EEG](#52-discusión-de-la-señal-eeg)  
   - [Señal EMG](#53-discusión-de-la-señal-emg)  
6. [Bibliografía](#6-bibliografía)

---

## 1. Introducción
La gran mayoría de señales biológicas, antes de ser evaluadas, requieren procesamiento por la introducción de ruido en la obtención de la señal de interés. La transformada wavelet se basa en la investigación de Daubechies y presenta un enfoque de tiempo-frecuencia que permite el procesamiento de señales biológicas, como EMG, EEG y ECG. 

Sin embargo, la elección de la familia adecuada de *wavelet* depende de la naturaleza de la señal. La función *wavelet madre* es la base de las transformadas wavelet que permitirían la identificación de coeficientes correlacionados entre múltiples señales, cuanto más similar sea la función wavelet madre a los coeficientes wavelet entre señales, más precisa será la identificación y el aislamiento de la señal de interés [1].

Las señales EMG de superficie permiten obtener información sobre el tiempo o intensidd de la activación de un músculo superficial. No obstante,  cada vez que se registra una señal EMG del músculo, diversos tipos de ruidos, tanto físicos como eléctricos, la contaminan. Algunas de las principales fuentes de ruido son los movimientos de grupos musculares cercanos, pues estos producen su popio potencial; señales electromgnéticas externas o del propio cuerpo; inlcuso los propios electrodos, pues a menor tamaño del electrodo se genera más impedancia lo cual reduce la calidad de la señal y proporciona una baja relación señal-ruido. [2]  

<p align="center">
  <img src="https://github.com/PamelaVilchez/GRUPO-08-ISB-2025-II/blob/aeb6c85187b04c949bdc5f4e52af25c82c41332e/Repositorio-Im%C3%A1genes/intro_emg.png?raw=true" 
       alt="MILimb_2a" width="300">
</p>

Asimismo, las señales ECG son sumamente importantes para el diagnóstico y tratamiento de pacientes, es por ello que su procesamiento es frecuentemente estudiado. La información importante que se debe mantener post-procesamiento son los picos y valles P , Q, R, S y T, los cuales son llamados onda P , T y U y los complejos o segmentos PQ, QRS y ST [3]. 

<p align="center">
  <img src="https://github.com/PamelaVilchez/GRUPO-08-ISB-2025-II/blob/aeb6c85187b04c949bdc5f4e52af25c82c41332e/Repositorio-Im%C3%A1genes/intro_ecg.png?raw=true" 
       alt="MILimb_2a" width="300">
</p>

Las señales EEG constituyen un registro gráfico de las variaciones de voltaje generadas por la actividad eléctrica cerebral, producto de flujos de corriente iónica. Estas señales se captan mediante electrodos colocados sobre el cuero cabelludo. Sin embargo, varios ruidos artificiales pueden interferir con la señal EEG original durante su tiempo de registro, como el parpadeo, los movimientos oculares, la actividad muscular y la interferencia de las señales de los dispositivos electrónicos [4]. 

<p align="center">
  <img src="https://github.com/PamelaVilchez/GRUPO-08-ISB-2025-II/blob/aeb6c85187b04c949bdc5f4e52af25c82c41332e/Repositorio-Im%C3%A1genes/intro_eeg.png?raw=true" 
       alt="MILimb_2a" width="300">
</p>

En función a lo mencionado anteriormente, las señales biológicas serán sometidas a un proceso de reducción de ruido mediante técnicas específicas. La selección del método de procesamiento se fundamenta en literatura y se adapta a las características particulares de cada tipo de señal.

---

## 2. Objetivos Específicos
-  Seleccionar la familia de wavelet y parámetros del filtro más adecuada para cada tipo de señal biológica y justificar con literatura científica la elección del método.
- Aplicar la transformada wavelet para descomponer las señales en distintos niveles de frecuencia y detalle.
- Visualizar y analizar los resultados de la descomposición wavelet para validar la eliminación de ruido sin pérdida de información crítica.

---

## 3. Elección de la familia de Wavelet
### 3.1. EMG
Se elegió la transformación wavelet Daubechies-4 (db-4), pues para el análisis de señales sEMG este ofrece mejores resultados al utilizar la función ddb4 en el nivel de descomposición 4. Aunque tambien menciona que se puede emplear db-2, db-6, db-44 y db-45. [2]

Sin embargo, otro estudio ha demostrado que el db-4 presenta un mejor rendimiento para realizar una máxima reducción de ruido, eliminando alrededor del 93 % de sus coeficientes de energía pequeña descartada, a comparación de db-8, db-16 y db-32. La reducción de ruido fue medida mediante *mean squared error* (MSE). [5]

<p align="center">
  <img src="https://github.com/PamelaVilchez/GRUPO-08-ISB-2025-II/blob/fecf5c738e6446e579990446f9d68489ac41a15c/Repositorio-Im%C3%A1genes/emg-d4.png?raw=true" 
       alt="MILimb_2a" width="400" height ="220">
</p>

### 3.2. ECG 
Se eligió emplear un wavelet Daubechies-8 (db-8) en el nivel de descomposición 3 [6], porque el dominio wavelet contiene pocos coeficientes significativos, al reconstruir la señal se preservan al máximo los componentes de la señal primaria ECG mientras se elimina eficientemente el ruido. Además, se demostró que presenta una mejor propiedad de localización de los coeficientes wavelet con db-8 en comparación con db-4, db-6, db-10, db-12, db-14, db-16, Symlet 3, Symlet 4, Symlet 5, Symlet 6, Symlet 7, Symlet 8, Coiflet 1, Coiflet 2, Coiflet 3, Battle-Lemarié 1 y Battle-Lemarié 3 [7]. Ello refuerza la elección de utilizar el filtro wavelet de Daubechies de orden 8 como
óptimo para el procesamiento de señales ECG. 

Asimismo, en este mismo estudio se demuestra que el db-8 fue capaz de reconstruir la señal casi idénticamente a la original incluso después de eliminar el ruido.

<p align="center">
  <img src="https://github.com/PamelaVilchez/GRUPO-08-ISB-2025-II/blob/00df93aece265b3f144966c485774d571a380d64/Repositorio-Im%C3%A1genes/ecg_db-8.png?raw=true" 
       alt="MILimb_2a" width="400">
</p>

### 3.3. EEG
Se eligió un wavelet de Debauchies (DB4) y un nivel de descomposición de 5, pues a partir de esta se puede establecer una relación entre la señal descompuesta con las subbandas de EEG tales como delta, theta, alfa, beta y gamma [8]. Cabe resaltar que en dicho estudio emplearon un EEG de 14 canales (AF3, AF4, F3, F4, F7, F8, FC5, FC6, P7, P8, T7, T8, O1, O2) denominado «EMOTIVE EPOC». A diferencia de la señal que nosotros obtuvimos a partir del Ultracortex que consta de 8 canales (FP1, FP2, C3, C4, T5, T6, O1, O2).  

<div style="display: flex; justify-content: center; gap: 20px;">
  <img src="https://github.com/PamelaVilchez/GRUPO-08-ISB-2025-II/blob/721ceb98650ec76784b690648eea85dd3430d56b/Repositorio-Im%C3%A1genes/eeg_d4.png?raw=true" 
       alt="MILimb_2a" width="400">
  <img src="https://github.com/PamelaVilchez/GRUPO-08-ISB-2025-II/blob/2e2002a99b936d818712289928bb403889a90209/Repositorio-Im%C3%A1genes/eeg_d4_2.png?raw=true" 
       alt="MILimb_2a" width="400">
</div>
---

## 4. Resultados

### 4.1 Parámetros del Filtro
- **Tipo de wavelet:** Daubechies  
- **Nivel de descomposición:**   
- **Umbral aplicado:**   
- **Frecuencia de muestreo:**   Hz  
- **Duración de la señal:**  segundos  

Se obtuvieron ..

---

## 5. Discusión
### 5.1. Discusión de la señal ECG:
El procesamiento de la señal ECG mediante la transformada wavelet Daubechies-8 permitió reducir eficazmente el ruido sin alterar la morfología crítica de la señal. Se aplicaron dos enfoques: una reconstrucción basada en la conservación de coeficientes de aproximación, útil para compresión y análisis de tendencia; y un filtrado por umbral suave, tanto fijo como adaptativo, que logró atenuar el ruido de alta frecuencia preservando los complejos QRS y las ondas P y T. La superposición entre la señal original y la reconstruida evidenció una alta fidelidad temporal, sin desplazamientos ni pérdida significativa de amplitud.
El análisis espectral mostró componentes dominantes en torno a 60 Hz, atribuibles a interferencia electromagnética, mientras que el espectrograma STFT reveló un aumento de energía en bandas altas hacia los 35 segundos, posiblemente por artefactos de movimiento post-ejercicio. El scalograma confirmó que las escalas entre 20 y 40 concentraban la mayor energía, correspondientes a frecuencias entre 10 y 30 Hz, lo que valida la elección de la familia Daubechies para representar transitorios rápidos como los del ECG.
La detección de picos en la señal reconstruida mantuvo una concordancia elevada respecto a la señal original, con sensibilidad y precisión adecuadas para aplicaciones clínicas. La frecuencia cardíaca estimada se mantuvo estable antes y después del procesamiento, lo que indica que el filtrado no alteró la periodicidad fisiológica. Además, el filtrado permitió reducir el número de coeficientes significativos sin comprometer la calidad de la reconstrucción, lo que sugiere su utilidad en contextos de compresión y transmisión eficiente de datos biomédicos.
La metodología empleada es reproducible y compatible con entornos de adquisición en campo. El uso de PyWavelets y Matplotlib permitió documentar cada paso del procesamiento, asegurando trazabilidad. Si bien la señal fue adquirida post-ejercicio, lo que introduce artefactos musculares, el enfoque aplicado demostró ser robusto frente a estas condiciones. Se recomienda complementar el procesamiento con técnicas de corrección de línea base y validar con métodos alternativos como EMD o wavelet scattering para escenarios clínicos más exigentes.
En conclusión, el uso de Daubechies-8 con umbral adaptativo ofrece una solución eficaz para el procesamiento de señales ECG, combinando reducción de ruido, preservación morfológica y eficiencia computacional. Esta estrategia puede ser replicada en otros tipos de señales biológicas, adaptando los parámetros según las características espectrales de cada caso.

### 5.1. Discusión de la señal EEG:
La señal EEG registrada durante una tarea cognitiva fue procesada mediante transformadas wavelet y análisis espectral para evaluar su estructura, reducir ruido y extraer componentes fisiológicos relevantes. La señal original mostró oscilaciones de baja amplitud con presencia de artefactos, lo que justifica la necesidad de filtrado multibanda y descomposición temporal.
El espectro de frecuencias reveló componentes distribuidos hasta ±100 Hz, con predominancia en bandas bajas, mientras que el espectrograma STFT permitió visualizar la evolución temporal de la energía, destacando zonas de mayor actividad entre los 10 y 25 segundos. La transformada wavelet continua (CWT) con Morlet mostró concentraciones de energía en escalas medias, lo que sugiere actividad cerebral sostenida en rangos Theta y Alpha.
La descomposición discreta (DWT) con Daubechies-4 permitió segmentar la señal en niveles de detalle y aproximación. Al conservar únicamente los coeficientes de aproximación, se logró una reconstrucción suave de la señal, útil para compresión y análisis de tendencia. El filtrado por umbral suave (0.4) permitió atenuar el ruido sin eliminar componentes relevantes, como se evidenció en la superposición entre señal original y reconstruida.
La señal denoised mostró una mejora en la claridad de los patrones oscilatorios, especialmente en el rango de 10 a 25 segundos, donde se observó una reducción de artefactos. La compresión por conservación de coeficientes de aproximación permitió reducir la dimensionalidad de la señal manteniendo su forma general, lo que es útil para almacenamiento eficiente.
Finalmente, se aplicaron filtros pasa banda para extraer las bandas cerebrales clásicas (Delta, Theta, Alpha, Beta, Gamma bajo y alto). La distribución de energía mostró predominancia en Theta y Beta, coherente con la realización de una tarea cognitiva de concentración moderada. Aunque se reportaron advertencias de overflow en el cálculo de energía, esto puede corregirse normalizando la señal o ajustando el rango dinámico antes de aplicar operaciones cuadráticas.
En conjunto, el procesamiento aplicado permitió caracterizar la señal EEG en tiempo, frecuencia y escala, con resultados coherentes con la literatura sobre actividad cognitiva. La metodología es reproducible y adaptable a otros sujetos o tareas, y puede integrarse en pipelines de análisis EEG para investigación o aplicaciones clínicas.

### 5.1. Discusión de la señal EMG:
La señal EMG registrada durante la activación del tríceps fue procesada mediante transformadas wavelet y análisis espectral con el objetivo de reducir ruido, identificar patrones musculares y evaluar la eficiencia de compresión. La señal original mostró oscilaciones de alta frecuencia y variabilidad, propias de la actividad muscular voluntaria, pero también evidenció componentes espurios que justifican la aplicación de técnicas de filtrado multiescala.
El espectro de frecuencias reveló una distribución energética amplia, con componentes significativos por encima de los 50 Hz, lo que sugiere presencia de ruido electromagnético y actividad muscular secundaria. El espectrograma STFT permitió visualizar la evolución temporal de la energía, destacando zonas de mayor intensidad entre los 7 y 14 segundos, coincidentes con la contracción sostenida del músculo.
La transformada wavelet continua (CWT) con Morlet mostró concentraciones de energía en escalas bajas y medias, lo que indica la presencia de transitorios rápidos y actividad muscular localizada. La descomposición discreta (DWT) con Daubechies-4 permitió segmentar la señal en niveles de detalle y aproximación. Al conservar únicamente los coeficientes de aproximación, se logró una reconstrucción suave de la señal, útil para compresión y análisis de tendencia.
El filtrado por umbral suave (0.4) permitió atenuar el ruido sin eliminar componentes relevantes, como se evidenció en la superposición entre señal original y reconstruida. La señal denoised mostró una mejora en la claridad de los patrones oscilatorios, especialmente en el rango de 6 a 10 segundos, donde se observó una reducción de artefactos. La compresión por conservación de coeficientes de aproximación permitió reducir la dimensionalidad de la señal manteniendo su forma general, lo que es útil para almacenamiento eficiente o transmisión remota.
En conjunto, el procesamiento aplicado permitió caracterizar la señal EMG en tiempo, frecuencia y escala, con resultados coherentes con la literatura sobre actividad muscular. La metodología es reproducible, adaptable a otros músculos o tareas, y puede integrarse en pipelines de análisis EMG para investigación, rehabilitación o control de prótesis.

---

## 6. Bibliografía
1. Rafiee, M. A. Rafiee, N. Prause, and M. P. Schoen, “Wavelet basis functions in biomedical signal processing,” Expert Systems with Applications, vol. 38, no. 5, pp. 6190–6201, May 2011, doi: 10.1016/j.eswa.2010.11.050.
2. Chowdhury et al., “Surface electromyography signal processing and classification techniques,” Sensors, vol. 13, no. 9, pp. 12431–12466, Sep. 2013, doi: 10.3390/s130912431.
3. McSharry, G. D. Clifford, L. Tarassenko, and L. A. Smith, “A dynamical model for generating synthetic electrocardiogram signals,” IEEE Transactions on Biomedical Engineering, vol. 50, no. 3, pp. 289–294, Mar. 2003, doi: 10.1109/TBME.2003.808805.
4. Alyasseri, A. T. Khader, M. A. Al-Betar, S. N. Makhadmeh, and others, “EEG signals denoising using optimal wavelet transform hybridized with efficient metaheuristic methods,” IEEE Access, vol. 7, pp. 1–1, Dec. 2019, doi: 10.1109/ACCESS.2019.2962658.
5. Berger, J. C. Carmo, F. A. D. O. Nascimento, and A. Rocha, “Algorithm for compression of EMG signals,” in Proc. 25th Annual Int. Conf. IEEE Engineering in Medicine and Biology Society (EMBS), Cancun, Mexico, Oct. 2003, pp. 1332–1335. https://doi.org/10.3390/s130912431
6. Poornachandra, “Wavelet-based denoising using subband dependent threshold for ECG signals,” Digital Signal Processing, vol. 17, no. 3, pp. 572–588, 2007, doi: 10.1016/j.dsp.2007.09.006.
7. Singh and A. K. Tiwari, “Optimal selection of wavelet basis function applied to ECG signal denoising,” Digital Signal Processing, vol. 16, pp. 275–287, 2006, doi: 10.1016/j.dsp.2005.12.003.
8. Kumari and A. Vaish, “Brainwave’s based user authentication system: A pilot study in robotic environment,” Robotics and Autonomous Systems, 2014, doi: 10.1016/j.robot.2014.11.015.


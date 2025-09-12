- [1. Introducción](#1-introducción)
- [2. Objetivos del laboratorio](#2-objetivos-del-laboratorio)
- [3. Materiales y equipo](#3-materiales-y-equipo)
- [4. Metodología](#4-metodología)
- [5. Señales ECG ploteadas en Python](#5-señales-ecg-ploteadas-en-python)
- [6. Conclusiones](#6-conclusiones)
- [7. Referencias](#referencias)

# 1. Introducción 
Un electrocardiograma (ECG) es un procedimiento sencillo, no invasivo y de rápida ejecución que registra la actividad eléctrica del corazón. Cada vez que el corazón late, una señal eléctrica recorre el músculo cardíaco, estimulando sus cámaras para que se contraigan y bombeen sangre al cuerpo. El ECG es una herramienta clave para revisar el estado del corazón cuando se sospecha algún problema. Permite detectar alteraciones como arritmias, enfermedades del músculo cardíaco o problemas en las arterias. Su funcionamiento se basa en captar la actividad eléctrica del corazón a través de electrodos colocados en la piel. Además, el electrocardiograma ayuda a que distintos profesionales de salud trabajen juntos para brindar una mejor atención al paciente [1].
# 2. Objetivos del laboratorio 
- Registrar señales ECG en reposo, respiración y ejercicio.
- Evaluar calidad de señal según acoplamiento electrodo-piel.
- Usar Python y OpenSignals para análisis de la señal obtenida.

# 3. Materiales y equipo
# 4. Metodología

# 5. Señales ECG ploteadas en Python
Se graficó en Python la señal obtenida por el dispositivo **BITalino**, lo que permitió un análisis detallado del **ECG**.  
Este paso es fundamental, ya que posibilita identificar con mayor precisión los **complejos QRS**, necesarios para el cálculo de los **latidos por minuto (lpm)**.

Para determinar la frecuencia cardíaca, se midieron los **intervalos R-R**, es decir, la distancia temporal entre picos R consecutivos de la señal.

Dado que se trata de un ECG con **ritmo regular**, el cálculo se simplifica aplicando la siguiente fórmula:

$$
\text{Lpm} = \frac{60}{\text{Intervalo R-R (s)}}
$$

Previo a ello, fue necesario convertir el número de muestras en **segundos**, empleando la frecuencia de muestreo configurada en el BITalino (f = 1000Hz)

Adicionalmente, se realizó un análisis espectral mediante la **Transformada Rápida de Fourier (FFT)**.  
Este procedimiento permitió observar la **distribución de frecuencias** contenidas en la señal ECG, lo cual facilita la identificación de posibles **componentes de ruido**.

El **BITalino** integra un sistema de **acondicionamiento analógico previo**, que incluye filtrado de hardware.  
Dicho sistema atenúa gran parte de las interferencias antes de la digitalización, por lo que no fue necesario aplicar un filtrado digital adicional en el procesamiento de la señal.

---
### 5.1. Señal ECG en reposo
El usuario se encontraba en reposo por lo que este representa su estado basal, además se puede medir el valor del intervalo R-R calculando el tiempo entre los picos en 4.9s y 5.72s, lo cual representa un intervalo R-R de 0.82s. Ello equivale a **73.17 latidos por minuto**, lo cual está dentro del rango normal de palpitaciones cardíacas.

<p align="center">
  <img src="https://github.com/PamelaVilchez/GRUPO-08-ISB-2025-II/blob/3aaab43f2e1c31f8cdd6feb53b37c3380c6df669/Repositorio-Im%C3%A1genes/ecg_signal_reposo.png?raw=true" 
       alt="b_reposo" width="700">
</p>

<p align="center">
  <img src="https://github.com/PamelaVilchez/GRUPO-08-ISB-2025-II/blob/616b588c18c505bbfa2c30f55ab345c76344f817/Repositorio-Im%C3%A1genes/ecg_fft_reposo.png?raw=true" 
       alt="b_reposo" width="700">
</p>

### 5.2. Señal ECG conteniendo el aire
El usuario contuvo la respiración durante 30 segundos, y después descansó durante 1 minuto. 

En la tercera gráfica de esta sección se puede observar el espectro completo, se puede evidenciar como la amplitud de la señal vuelve a aumentar una vez que el usuario finaliza la contención del aire. Ello se puede explicar porque, al contener la respiración, aumenta la presión intratorácica y esto disminuye el retorno venoso hacia el corazón, reduciendo así el volumen sistólico. A la vez, se activa el reflejo vagal, lo que genera un predominio parasimpático que tiende a enlentecer y estabilizar la frecuencia cardiaca. Sin embargo, una vez que se retoma la respiración, la presión intratorácica vuelve a la normalidad, el retorno venoso mejora y el corazón se llena de manera más adecuada, lo que se manifiesta como una recuperación en la amplitud de la señal.

El tiempo entre los picos en 10.98s y 11.82s representa un intervalo R-R de 0.84s. Ello equivale a **71.42 latidos por minuto**.

<p align="center">
  <img src="https://github.com/PamelaVilchez/GRUPO-08-ISB-2025-II/blob/23fa0260db26d6b7cb8aebdf790c29b613f99553/Repositorio-Im%C3%A1genes/ecg_signal_aire.png?raw=true" 
       alt="MILimb_2a" width="700">
</p>

<p align="center">
  <img src="https://github.com/PamelaVilchez/GRUPO-08-ISB-2025-II/blob/23fa0260db26d6b7cb8aebdf790c29b613f99553/Repositorio-Im%C3%A1genes/ecg_fft_aire.png?raw=true" 
       alt="MILimb_2a" width="700">
</p>

<p align="center">
  <img src="https://github.com/PamelaVilchez/GRUPO-08-ISB-2025-II/blob/23fa0260db26d6b7cb8aebdf790c29b613f99553/Repositorio-Im%C3%A1genes/contener_aire_completo.png?raw=true" 
       alt="MILimb_2a" width="700">
</p>

Si evaluáramos los latidos por minuto en su etapa de recuperación tendríamos que el tiempo 34.88s y 35.66s representa un intervalo R-R de 0.78s. Ello equivale a **76.92 latidos por minuto**.

<p align="center">
  <img src="https://github.com/PamelaVilchez/GRUPO-08-ISB-2025-II/blob/5d5acaea9555da12965dc4d168f32e9bd94f345d/Repositorio-Im%C3%A1genes/otro.png?raw=true" 
       alt="MILimb_2a" width="700">
</p>

#### 5.3. Señal ECG después de actividad aeróbica
El usuario fue sometido a actividad física de 11 minutos, inmediatamente después se le realizó la medición.
El tiempo entre los picos en 4.06s y 4.68s representa un intervalo R-R de 0.62s. Ello equivale a **96.77 latidos por minuto**.

<p align="center">
  <img src="https://github.com/PamelaVilchez/GRUPO-08-ISB-2025-II/blob/98d4e2fc6c3d62c4e8e7002e9c6f64ce7a8d5a27/Repositorio-Im%C3%A1genes/ecg_signal_actF.png?raw=true" 
       alt="MILimb_2a" width="700">
</p>

<p align="center">
  <img src="https://github.com/PamelaVilchez/GRUPO-08-ISB-2025-II/blob/98d4e2fc6c3d62c4e8e7002e9c6f64ce7a8d5a27/Repositorio-Im%C3%A1genes/ecg_fft_actF.png?raw=true" 
       alt="MILimb_2a" width="700">
</p>

##### - Archivos EGC:
[Documentos txt Bitalino](https://github.com/PamelaVilchez/GRUPO-08-ISB-2025-II/tree/a3c40e49cffb82b3eea75ac27e97558f57f93680/Repositorio-Im%C3%A1genes/Archivos-ECG)


# 6. Conclusiones

# 7. Referencias
 [1]. Y. Sattar and L. Chhabra, “Electrocardiogram,” StatPearls - NCBI Bookshelf, Jun. 05, 2023. https://www.ncbi.nlm.nih.gov/books/NBK549803/

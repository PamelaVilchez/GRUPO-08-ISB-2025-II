## Señal EMG:

Se empleó la señal EMG de **extensión del tríceps con una fuerza opositora (intento 1)** y de **flexión del bíceps braquial con una fuerza opositora (intento 2)**, en ambos se observa el espectro de frecuencias el cual señala que hay mayor información en frecuencias entre 25 Hz y 120Hz.  

Estudios previos establecen que la mayor concentración de energía en las señales EMGS se encuentra entre los 50 Hz y 150 Hz, aunque su **canal de información va de los 20 Hz a los 500 Hz** [1]. Es por ello que la frecuencia de muestreo utilizada en la práctica fue de **1000 Hz**, pues según el **teorema de Nyquist**, si muestreamos a una frecuencia de **500 Hz**, se pueden registrar componentes de frecuencia hasta los **250 Hz**. Es por ello que no es necesario una mayor frecuencia puesto que la mayor concentración de energía se encuentra entre los **50 y 150 Hz**.  

Considerando que se empleó una frecuencia de sampleo de 1000 Hz, se convirtieron las frecuencias de corte como **fnorm = f/fs**, dichos valores fueron colocados en la configuración de ***Target Specification*** en pyFDA. De esta forma el filtro tiene una banda pasante plana entre 0.02 y 0.45 (normalizado) lo que corresponde a **20 Hz - 450 Hz**, como se deseaba filtrar.

---

### Elección de filtro: FIR o IIR
Los filtros FIR presentan fase lineal en la banda de paso [2], lo que los convierte en una buena opción para preservar la morfología de la señal EMG para la detección precisa de picos. Sin embargo, para lograr transiciones de frecuencia estrechas (entre 10 Hz y 20Hz), necesitan un orden muy alto, lo que implica mayor costo computacional y retardo [3], haciéndolos menos adecuados para el procesamiento en tiempo real de señales EMG. 

Por otro lado, los filtros IIR son mucho más eficientes para el procesamiento en tiempo real, ya que alcanzan la misma atenuación que un FIR pero con muchos menos costo computacional, por lo que son más rápidos y de menor consumo de recursos. Aunque no tienen fase lineal y pueden ser inestables si no se diseñan adecuadamente, para el filtrado de señales EMG es más relevante la energía, potencia y frecuencia que la forma exacta de la onda por lo que los filtros IIR se han elegido para filtrar la señal a continuación.

#### Filtro IIR - Butterworth orden 4
Este fue el filtro elegido para filtrar las señales EMG, asimismo fue comparado con otros 3 filtros. Se detalló las principales características que lo vuelven un buen filtro para este tipo de señal.

##### Respuesta de magnitud
<p align="center">
  <img src="https://github.com/PamelaVilchez/GRUPO-08-ISB-2025-II/blob/e45f1b74272b0034ff20d99f260f6c6286d16e6c/Repositorio-Im%C3%A1genes/filtro_butter_magnitud.jpg?raw=true" width="500">
</p>
En el gráfico de magnitud, la banda de paso tiene una respuesta plana sin ondulaciones lo cual evita distorsiones en amplitud dentro del rango útil establecido (20–450 Hz), preservando así la forma original de la señal muscular. Cabe resaltar que no presenta una caída abrupta a la banda de rechazo.

##### Respuesta de fase
<p align="center">
  <img src="https://github.com/PamelaVilchez/GRUPO-08-ISB-2025-II/blob/e45f1b74272b0034ff20d99f260f6c6286d16e6c/Repositorio-Im%C3%A1genes/filtro_butter_fase.jpg?raw=true" width="500">
</p>
Presenta una transición de fase suave lo cual reduce la distorsión temporal (group delay) cuando se apliquen técnicas de filtrado que eliminen el desfase.

##### Gráfico P/Z
<p align="center">
  <img src="https://github.com/PamelaVilchez/GRUPO-08-ISB-2025-II/blob/e45f1b74272b0034ff20d99f260f6c6286d16e6c/Repositorio-Im%C3%A1genes/filtro_butter_pz.jpg?raw=true" width="500">
</p>
El diagrama de polos y ceros muestra que todos los polos están dentro del círculo unitario, lo cual garantiza la estabilidad.

#### Filtro IIR - Bessel orden 4
##### Respuesta de magnitud
<p align="center">
  <img src="https://github.com/PamelaVilchez/GRUPO-08-ISB-2025-II/blob/e45f1b74272b0034ff20d99f260f6c6286d16e6c/Repositorio-Im%C3%A1genes/filtro_bessel_magnitud.jpg?raw=true" width="500">
</p> 
Se observa en la gráfica de magnitud, en dB, una transición muy suave y lenta entre la banda de paso y la banda de rechazo. Es por ello que a pesar de ser un pasabanda, la caída en las frecuencias de paso, 20 Hz y 450 Hz, son muy graduales e implica que las frecuencias fuera del rango útil no sean atenuadas lo suficiente.
Sin embargo en señales EMG ello representa un problema crítico; por ejemplo, a frecuencias menores a 10 Hz se presenta información de artefactos de movimiento o frecuencias superiores a 500 Hz se puede presentar información de origen electromagnético. Las cuales se superponen a la señal de interés.

##### Respuesta de fase
<p align="center">
  <img src="https://github.com/PamelaVilchez/GRUPO-08-ISB-2025-II/blob/e45f1b74272b0034ff20d99f260f6c6286d16e6c/Repositorio-Im%C3%A1genes/filtro_bessel_fase.jpg?raw=true" width="500">
</p>  
Presenta una transición de fase suave lo cual reduce el group delay.

##### Gráfico P/Z
<p align="center">
  <img src="https://github.com/PamelaVilchez/GRUPO-08-ISB-2025-II/blob/e45f1b74272b0034ff20d99f260f6c6286d16e6c/Repositorio-Im%C3%A1genes/filtro_bessel_pz.jpg?raw=true" width="500">
</p>  
Los polos están dentro del círculo unitario, lo cual garantiza la estabilidad.

#### Filtro IIR - Elliptic orden 4
##### Respuesta de magnitud
<p align="center">
  <img src="https://github.com/PamelaVilchez/GRUPO-08-ISB-2025-II/blob/e45f1b74272b0034ff20d99f260f6c6286d16e6c/Repositorio-Im%C3%A1genes/filtro_elliptic_magnitud.jpg?raw=true" width="500">
</p>  
Se observa que la banda de paso presenta pequeñas oscilaciones las cuales variarán la amplitud de la señal de interés. Ello puede afectar la detección de actividad muscular.
Además, en la banda de rechazo también hay oscilaciones pero con una atenuación alta de 60–80 dB.

##### Respuesta de fase
<p align="center">
  <img src="https://github.com/PamelaVilchez/GRUPO-08-ISB-2025-II/blob/e45f1b74272b0034ff20d99f260f6c6286d16e6c/Repositorio-Im%C3%A1genes/filtro_elliptic_fase.jpg?raw=true" width="500">
</p> 
Se observa que la fase no es lineal sino que hay saltos bruscos. Ello genera que exista una deformación temporal de la señal (group delay) que provoca retardos en diferentes frecuencias.  Consecuentemente, los potenciales de acción musculares se pueden superponer incorrectamente.

##### Gráfico P/Z
<p align="center">
  <img src="https://github.com/PamelaVilchez/GRUPO-08-ISB-2025-II/blob/e45f1b74272b0034ff20d99f260f6c6286d16e6c/Repositorio-Im%C3%A1genes/filtro_elliptic_pz.jpg?raw=true" width="500">
</p>  
Los saltos vistos en la gráfica de fase indican que los ceros están en el círculo unitario, debido a estos se generarán cambios abruptos en la fase al cruzar las frecuencias críticas.

#### Filtro IIR - Chebyshev 2 orden 5
##### Respuesta de magnitud
<p align="center">
  <img src="https://github.com/PamelaVilchez/GRUPO-08-ISB-2025-II/blob/e45f1b74272b0034ff20d99f260f6c6286d16e6c/Repositorio-Im%C3%A1genes/filtro_cheb_magnitud.jpg?raw=true" width="500">
</p>    
La atenuación en la banda de rechazo es alta (~60 dB), lo cual es aceptable pues permite eliminar el ruido fuera de la banda de paso. Cabe resaltar que este presenta rizos en la banda de rechazo.

##### Respuesta de fase
<p align="center">
  <img src="https://github.com/PamelaVilchez/GRUPO-08-ISB-2025-II/blob/e45f1b74272b0034ff20d99f260f6c6286d16e6c/Repositorio-Im%C3%A1genes/filtro_cheb_fase.jpg?raw=true" width="500">
</p>   
Otro problema importante es que la fase no presenta un comportamiento lineal, es decir, hay saltos bruscos en la fase para varias frecuencias. 
Estos saltos indican que existirá un “group delay distortion”, lo que implica que diferentes componentes de frecuencia de la señal EMG llegarán con retrasos distintos.

##### Gráfico P/Z
<p align="center">
  <img src="https://github.com/PamelaVilchez/GRUPO-08-ISB-2025-II/blob/e45f1b74272b0034ff20d99f260f6c6286d16e6c/Repositorio-Im%C3%A1genes/filtro_cheb_pz.jpg?raw=true" width="500">
</p>   
Se observa que el Chebyshev II tiene ceros en el círculo unitario. Ello puede provocar que la fase tenga discontinuidades al cruzar esos puntos, los cuales se evidencia en la gráfica de fase.
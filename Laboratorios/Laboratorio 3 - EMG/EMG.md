# Índice
- [1. Introduccion](#1-introduccion)
- [2. Objetivos del laboratorio](#2-objetivos-del-laboratorio)
- [3. Materiales y equipo](#2-materiales-y-equipo)


# 1. Introduccion
### ¿Qué es el EMG? 🧠  
El electromiograma (EMG) es una técnica que permite registrar la actividad eléctrica generada por los músculos esqueléticos durante su contracción. Esta actividad proviene de los potenciales de acción que se propagan a lo largo de las fibras musculares cuando son activadas por el sistema nervioso.  
En el caso del EMG de superficie (sEMG), se utilizan electrodos colocados sobre la piel para detectar estas señales. Los electrodos no penetran el cuerpo, sino que captan los cambios de voltaje que ocurren justo debajo de la piel, generados por la suma de múltiples unidades motoras activas.

### ¿Para qué sirve? ⚡  
- Ayuda a entender si un músculo está funcionando bien o no.  
- Se usa en medicina para detectar problemas nerviosos o musculares.  
- También sirve en deportes y rehabilitación para ver cómo se activan los músculos.

### ¿Cómo se hace? 🩺  
- Se colocan sensores en la piel, cerca del músculo que se quiere estudiar.  
- La persona mueve el músculo, y el EMG muestra las señales en una pantalla.  
- Es rápido, no duele, y da información útil para médicos y terapeutas.

# 2. Objetivos del laboratorio
- Configuración precisa del sistema BiTalino para adquisición electromiográfica.  
- Captura de bioseñales musculares en los movimientos de contracción del bíceps y tríceps mediante EMG de superficie.  
- Procesamiento y análisis de datos EMG utilizando la plataforma OpenSignals (r)evolution y Python.

# 3. Materiales y equipo

<div align="center">

| Modelo       | Descripción   | Cantidad |
|:------------:|:-------------:|:--------:|
| (R)EVOLUTION | Kit BITalino  |    1     |
| -            | Laptop        |    1     |

</div>

<p align="center">
  <img src="../../Repositorio-Imágenes/Lab3_kit_BITalino.jpeg" alt="Kit BITalino" width="400" height="400"/>
</p>

# 4. Procedimiento

Se realizaron dos experimentos de registro de señales EMG: el primero en el bíceps y el segundo en el tríceps. En las siguientes secciones se detalla la ubicación de los electrodos en cada músculo, así como los resultados obtenidos en cada caso.

## Experimento 1: Bíceps
### Esquema de conexión de electrodos
Para el registro de la señal EMG en el bíceps se empleó el sensor de 3 electrodos de la placa BITalino, siguiendo las recomendaciones del manual de uso.

| ![BITalino_3_electrodos](../../Repositorio-Imágenes/Lab3_3electrodos.png) | ![BITalino_ubicación](../../Repositorio-Imágenes/Lab3_ubicación_electrodos.png) |
|:---------------------------------------------:|:--------------------------------------------:|
| **Sensor EMG de 3 electrodos** | **Esquema de conexión de los electrodos** |

### Comparación de la conexión correcta e incorrecta de los electrodos en el bíceps
En la conexión correcta se observa una señal limpia y representativa de la actividad muscular.
En la conexión incorrecta, debido a una mala colocación de los electrodos, la señal registrada presenta un nivel elevado de ruido, lo cual dificulta el análisis adecuado.


|**Conexión correcta ✅**|**Conexión incorrecta ❌**|
|:------------------|:--------------------|
| ![Conexión correcta](../../Repositorio-Imágenes/Lab3_I02_electrodos_correctos.jpeg) | ![Conexión incorrecta](../../Repositorio-Imágenes/Lab3_I01_electrodos_incorrectos.jpeg) |
| - **Electrodo rojo (+):** bíceps (zona activa)<br>- **Electrodo negro (–):** bíceps (zona pasiva)<br>- **Electrodo blanco:** espina ilíaca antero-superior (referencia) | - **Electrodo rojo (+):** bíceps (zona activa)<br>- **Electrodo negro (–):** espina ilíaca antero-superior (referencia)<br>- **Electrodo blanco:** bíceps (zona pasiva) |

### Prueba 1
Se registró la señal EMG con el participante en condición de reposo, a fin de establecer una línea base para posteriores comparaciones.

<p align="center">
  <img src="../../Repositorio-Imágenes/Lab3_B_P1_reposo.gif" alt="GIF de prueba" width="300" height="400"/>
</p>


### Prueba 2
El participante realizó flexión del brazo derecho durante un intervalo de 40 segundos seguido de un período de 30 segundos de reposo. Este procedimiento se repitió en tres ciclos consecutivos.

|**Intento 1**|**Intento 2**|**Intento 3**|
|--|--|--|
|![Prueba2_Intento_1](../../Repositorio-Imágenes/Lab3_B_P2_mov1.gif)| | |

### Prueba 3
El participante efectuó flexión del brazo derecho contra resistencia externa, aplicada para impedir el movimiento completo. Posteriormente, se consideró un período de 30 segundos de reposo. Al igual que en la prueba anterior, este protocolo se repitió en tres ciclos consecutivos.


## Experimento 2: Tríceps
### Ubicación de electrodos


















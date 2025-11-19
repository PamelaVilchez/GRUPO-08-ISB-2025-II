# Independent Component Analysis (ICA)
## 1. Motivación del Análisis de Componentes Independientes (ICA)
La motivación fundamental para el desarrollo de ICA es el problema del "cocktail-party".

Esta describe una situación en la que un individuo está en una sala donde dos personas hablan simultáneamente. Se utilizan dos micrófonos en ubicaciones diferentes para grabar dos señales temporales observadas, x1(t) y x2(t).
Cada señal grabada (x1(t) y x2(t)) es una suma ponderada lineal de las señales de voz originales emitidas por los dos hablantes, s1(t) y s2(t). 
El objetivo es estimar las dos señales de voz originales, utilizando solo las mezclas registradas. Si los parámetros de mezcla fueran conocidos, la ecuación lineal se podría resolver con métodos clásicos. Sin embargo, la dificultad clave radica en que los parámetros de mezcla se asumen desconocidos. 

La solución novedosa a este problema se encuentra al asumir que las señales de origen, son estadísticamente independientes en cada instante de tiempo t. La técnica de ICA permite estimar estos parámetros a_ij basándose en la información de su independencia, lo que a su vez permite la separación de las señales originales.

### 1.2. Otras Aplicaciones Impulsoras
Aunque ICA se desarrolló originalmente para el problema del cocktail-party, el principio tiene muchas otras aplicaciones relevntes en el ámbito biomédico. 
#### 1.2.1. Análisis de Señales Biomédicas:
 En grabaciones eléctricas de la actividad cerebral, como el electroencefalograma (EEG) y la magnetoencefalografía (MEG), los datos observados son mezclas de componentes subyacentes de la actividad cerebral. ICA puede revelar información relevante al aislar los componentes independientes de la actividad cerebral o, también, para separar los artefactos como movimientos oculares, parpadeos, actividad cardiaca o muscular de las señales cerebrales deseadas.
#### 1.2.2. Extracción de Características (Feature Extraction): 
ICA es útil para encontrar representaciones adecuadas de datos de imágenes o audio para tareas como la compresión y la eliminación de ruido. Por ejemplo, al aplicar ICA a parches de imágenes naturales, se pueden obtener funciones de base que actúan como "características independientes" de las imágenes.
#### 1.2.3. Finanzas y Econometría: 
ICA se aplica a series temporales paralelas, como datos de flujo de caja o tasas de cambio, para revelar factores subyacentes comunes que podrían estar afectando los datos, como variaciones estacionales o tendencias.

## 2. Concepto y Definición Rigurosa de ICA
El Análisis de Componentes Independientes (ICA) se formula matemáticamente como un modelo estadístico de variables latentes.

##### El Modelo Generativo
La definición rigurosa de ICA asume que observamos n mezclas lineales x1,…,xn de n componentes independientes s1,…,sn. En notación matricial, el modelo de mezcla se escribe como: x=As.
- x es el vector aleatorio de las mezclas observadas.
- s es el vector de los componentes independientes (variables latentes).
- A es la matriz de mezcla, la cual se asume desconocida.

ICA es un modelo generativo porque describe cómo los datos observados "x" son generados por un proceso de mezcla de los componentes s_i. 
El **objetivo del ICA** es estimar tanto la matriz de mezcla A como los componentes s, utilizando únicamente x. Una vez estimada A, los componentes independientes se recuperan mediante la matriz inversa W (la matriz separadora): s=Wx.

#### Principios Fundamentales del ICA
El concepto de ICA se basa en tres principios estadísticos y una restricción crucial:

1. Independencia Estadística: 
El punto de partida de ICA es la asunción de que los componentes si son estadísticamente independientes. Dos variables y1 y y2 son independientes si la información sobre el valor de y1 no proporciona ninguna información sobre y2. Técnicamente, esto se define si la función de densidad de probabilidad conjunta se puede factorizar como el producto de sus densidades marginales.

2. La Necesidad de la No-Gaussianidad: 
La restricción fundamental del ICA es que los componentes independientes deben tener distribuciones no-gaussianas para que el ICA sea posible.
Si los componentes fueran gaussianos, la distribución de cualquier transformación ortogonal de las mezclas gaussianas sería exactamente la misma. Una distribución gaussiana es completamente simétrica y no contiene información sobre las direcciones de los vectores de la matriz de mezcla A, lo que hace que A no sea identificable. En resumen, la distribución gaussiana es la "más aleatoria" o la menos estructurada de todas las distribuciones con igual varianza.
3. El Principio de Máxima No-Gaussianidad: 
La clave para estimar el modelo ICA es la no-gaussianidad.
El **Teorema del Límite Central** establece que la distribución de una suma de variables aleatorias independientes tiende a ser gaussiana. Por lo tanto, una combinación lineal de componentes independientes será "más gaussiana" que cualquiera de sus componentes originales.
El principio básico de la estimación de ICA se convierte en buscar un vector de pesos w tal que la proyección w^T.x (una combinación lineal de las mezclas) maximice la no-gaussianidad. Cuando esta no-gaussianidad se maximiza, la proyección es igual a uno de los componentes independientes.
4. Medidas de No-Gaussianidad (Conceptos de Contraste): 
Para utilizar el principio de máxima no-gaussianidad, se requieren medidas cuantitativas, o funciones de contraste.
E. Equivalencia Conceptual de Estimación: El enfoque de máxima no-gaussianidad se vincula rigurosamente con otros principios de estimación:

El modelo de ICA presenta ambigüedades inherentes que no pueden resolverse:
- Varianza/Energía y Signo: 
No se puede determinar la varianza (o energía) ni el signo de los componentes independientes. Convencionalmente, se asume que cada componente tiene varianza unitaria para fijar la magnitud.
- Orden de los Componentes:
El orden de los componentes independientes no se puede determinar libremente, ya que una permutación simplemente resulta en una nueva matriz de mezcla desconocida que debe ser resuelta.

## 3. Principios de ICA
### 3.1 Objetivo matemático y fundamento estadístico
El objetivo central de ICA es encontrar una transformación de los datos que produzca señales latentes (componentes) que sean máximamente independientes entre sí. Desde el punto de vista matemático, ICA busca minimizar la información mutua entre los componentes o maximizar la entropía conjunta. Esto garantiza que la actividad de una fuente no pueda predecir la actividad de otra, lo cual es indispensable para separar generadores independientes en EEG.

### 3.2 Fuentes máximamente independientes
Los algoritmos de ICA intentan recuperar fuentes cuyos patrones temporales no presenten solapamiento o dependencia. Esto incluye tanto fuentes neuronales con activaciones dinámicas específicas como artefactos fisiológicos repetitivos. Los componentes extraídos deben mostrar independencia estadística en su actividad temporal.

### 3.3 Independencia más allá de la correlación
Un aspecto clave es que ICA no se basa únicamente en la correlación lineal. La independencia estadística implica que las correlaciones de todos los órdenes (lineales y no lineales) deben ser nulas. Para evaluar esa independencia completa, ICA utiliza estadísticas de orden superior, lo cual le permite separar señales que PCA (Análisis de Componentes Principales) no puede distinguir.

### 3.4 ICA versus PCA
Aunque ICA y PCA son métodos de descomposición lineal, sus objetivos son distintos:
- PCA busca maximizar la varianza explicada por componentes no correlacionados mientras que ICA busca maximizar la independencia, permitiendo separar fuentes fisiológicamente significativas (actividad ocular, muscular, cerebral).

Por ello, ICA es más adecuado que PCA para el análisis de señales biomédicas (especialmente EEG), donde la independencia entre generadores fisiológicos es más relevante que la varianza.

### 3.5 Supuesto de mezcla lineal
ICA funciona correctamente cuando las fuentes se mezclan linealmente, sin retardos diferenciales. En el EEG esto se cumple debido a que la conducción de volumen desde los generadores neuronales hacia los electrodos de superficie es esencialmente lineal e instantánea, lo que hace a ICA especialmente adecuado para este tipo de señales.

### 3.6 Distribución no gaussiana
ICA requiere que las fuentes tengan distribuciones no gaussianas. Las señales fisiológicas y artefactuales en EEG cumplen este criterio: parpadeos y actividad muscular presentan distribuciones super-gaussianas, mientras que ruido de línea suele ser sub-gaussiano. Para este último caso, la variante Infomax extendida permite separar tanto fuentes sub-gaussianas como super-gaussianas.


## 4. Preprocesamiento para la aplicación de ICA
La correcta preparación de los datos es esencial para garantizar el funcionamiento adecuado de ICA, ya que el algoritmo depende de supuestos estadísticos y de la calidad de los datos.

### 4.1 Preparación general de los datos
Antes de aplicar ICA, es necesario someter a la señal biomédica a un conjunto de operaciones estándar:
- Filtrado de la señal para eliminar ruido de baja y alta frecuencia no deseado.
- Segmentación en épocas basadas en los eventos experimentales.
- Corrección de línea de base para normalizar los valores previos al estímulo.
- Re-referenciación, comúnmente mediante referencia promedio.
- Remuestreo para facilitar el procesamiento y reducir carga computacional.

Estas operaciones preparan la señal y garantizan un marco adecuado para la descomposición ICA.

### 4.2 Eliminación de artefactos y no linealidades
#### 4.2.1 Artefactos que deben conservarse
El objetivo de ICA es precisamente identificar y separar componentes fisiológicos y artefactuales. Por ello, no deben eliminarse antes del ICA los artefactos repetitivos tales como:
- Parpadeos
- Movimientos oculares
- Actividad muscular
- Ruido de línea

Eliminar estos eventos impediría que ICA los identifique y los separe adecuadamente.

#### 4.2.2 Artefactos que deben eliminarse

Existen artefactos que sí deben eliminarse, ya que violan el modelo lineal sobre el que se basa ICA:
- Clipping: saturación del amplificador que corta los picos de la señal.
- Wrap-around: inversión brusca causada por exceder el rango del convertidor A/D.

Estos fenómenos introducen no linealidad en los datos y pueden generar componentes ICA espurios.

### 4.3 Suficiencia de datos

ICA es un método estadístico: aprende la independencia a partir de la variabilidad temporal. Por ello, requiere una cantidad significativa de datos.

Regla práctica:
- Los datos deben contener al menos varias veces (número de canales)² puntos temporales.

Si los datos son insuficientes, ICA no podrá separar fuentes de manera estable y producirá resultados poco confiables.

### 4.4 Manejo de redundancias: PCA automática

En algunas configuraciones, como al usar referencia promedio, ciertos canales pueden volverse combinaciones lineales de otros. Esto crea dependencias lineales que complican la descomposición.

La función runica() implementada en EEGLAB aplica una etapa de PCA automática para:

- Detectar canales redundantes
- Reducir la dimensionalidad al rango real
- Prevenir errores en la estimación del ICA
- Mantener únicamente dimensiones matemáticamente válidas

Esto garantiza que ICA opere sobre un conjunto de datos adecuado y no intente separar más fuentes de las que realmente existen.


## 5. Método de Punto Fijo para Maximizar la No-Gaussianidad

El algoritmo FastICA constituye una de las aproximaciones más eficientes para la estimación de componentes independientes. Su fundamento se basa en la maximización de la no-gaussianidad de las combinaciones lineales de las señales observadas, utilizando un esquema iterativo de punto fijo.

### 5.1 Principios del algoritmo
- **Preprocesamiento**: los datos se centran (media cero) y se blanquean (decorrelación y varianza unitaria).
- **Iteración de punto fijo**:  
  Se actualiza un vector de pesos \(w\) mediante la regla:
  \[
  w_{\text{nuevo}} = \mathbb{E}\{x \, g(w^T x)\} - \mathbb{E}\{g'(w^T x)\} \, w
  \]
  donde:
  - \(x\) es el vector de observaciones,
  - \(g(\cdot)\) es una función no lineal (polinómica o exponencial),
  - \(g'(\cdot)\) es su derivada.
- **Normalización**: el vector \(w_{\text{nuevo}}\) se escala para mantener varianza unitaria.
- **Ortogonalización**: se asegura que los distintos vectores de pesos sean ortogonales, evitando redundancia en los componentes estimados.

### 5.2 Ventajas del método
- Convergencia rápida y estable, comparable a métodos de Newton pero con menor complejidad [1].
- Escalabilidad a grandes volúmenes de datos.
- Robustez frente a ruido moderado.
- Posibilidad de estimar múltiples componentes en paralelo.

---

## 6. Aplicaciones de ICA

El marco de ICA, y en particular el algoritmo FastICA, ha demostrado utilidad en diversos campos de investigación y práctica profesional [1]:

### 6.1 Neurociencia y biomédica
- Separación de artefactos en registros EEG y MEG (parpadeos, movimientos oculares, ruido muscular).
- Identificación de patrones de actividad cerebral independientes.
- Mejora de la reproducibilidad en análisis de señales biomédicas.

### 6.2 Procesamiento de audio
- Resolución del denominado *problema del cóctel*: separación de voces o instrumentos en grabaciones.
- Limpieza de señales acústicas en ambientes ruidosos.

### 6.3 Imágenes y visión por computadora
- Extracción de características independientes en imágenes naturales.
- Reducción de ruido y compresión adaptativa.
- Representaciones más eficientes que PCA para texturas y bordes.

### 6.4 Finanzas
- Detección de factores ocultos en series temporales de mercado.
- Análisis de riesgos y diversificación de portafolios.

### 6.5 Telecomunicaciones y radar
- Separación de señales mezcladas en canales de transmisión.
- Identificación y mitigación de interferencias.

---
## 7. Repositorio
El repositorio desarrollado por Kevin Tan presenta un pipeline de procesamiento de EEG basado en Independent Component Analysis (ICA), diseñado principalmente para estudios de potenciales relacionados con eventos (ERP), aunque adaptable a otros análisis M/EEG como ERSP y clasificación de ensayos individuales. El flujo de trabajo se organiza en tres etapas: 
1.  **PREP**, que realiza el preprocesamiento inicial de las señales; 
2.  **ICA y localización de fuentes**, donde se descomponen las señales en componentes independientes y se estiman sus posibles orígenes corticales; y 
3. **Preprocesamiento final**, que incluye la sustracción de componentes artefactuales (oculares, musculares, entre otros) y prepara los datos para análisis posteriores. Este pipeline, probado en registros de 128 canales BioSemi, ha demostrado ser eficaz en la limpieza de artefactos y en la mejora de la calidad de los datos, aunque requiere recursos computacionales intensivos y no se encuentra actualmente en mantenimiento activo.

link del repositorio: https://github.com/kevmtan/EEG-ICA-pipeline/wiki 

## Referencias

- [1] A. Hyvärinen and E. Oja, "Independent Component Analysis: Algorithms and Applications," *Neural Networks*, vol. 13, no. 4–5, pp. 411–430, 2000.
- [2] A. Delorme and S. Makeig, “EEGLAB: an open source toolbox for analysis of single-trial EEG dynamics including independent component analysis,” Journal of Neuroscience Methods, vol. 134, no. 1, pp. 9–21, 2004.

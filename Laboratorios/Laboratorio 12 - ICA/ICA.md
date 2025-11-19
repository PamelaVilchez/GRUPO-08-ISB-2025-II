# Independent Component Analysis (ICA)

## 5. Método de Punto Fijo para Maximizar la No-Gaussianidad

El algoritmo FastICA constituye una de las aproximaciones más eficientes para la estimación de componentes independientes [1]. Su fundamento se basa en la maximización de la no-gaussianidad de las combinaciones lineales de las señales observadas, utilizando un esquema iterativo de punto fijo.

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

[1] A. Hyvärinen and E. Oja, "Independent Component Analysis: Algorithms and Applications," *Neural Networks*, vol. 13, no. 4–5, pp. 411–430, 2000.
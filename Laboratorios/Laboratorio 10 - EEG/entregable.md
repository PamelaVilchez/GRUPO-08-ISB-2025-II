## Evaluación de componentes ICA
INTEGRANTES
- Pamela Vilchez
- Franco Peralta
- Mariel Sánchez

### Criterios a evaluar

| Criterio | Descripción |
|---------|-------------|
| **Espectro de potencia** | Presenta una pendiente positiva entre 7 y 75 Hz, con energía distribuida en frecuencias medias-altas. | 
| **Topografía (topomap)** | Muestra un foco periférico, con dipolos localizados lejos del vértex (zona temporal). |
| **Morfología temporal** | La señal es espiculada, con picos irregulares y aspecto ruidoso típico de EMG.|
---

### Componentes ICA que cumplen los criterios
#### Evaluación del componente ICA000
**ICA000 cumple los criterios clásicos de artefacto muscular.**  
Este componente es un buen candidato para ser excluido del EEG reconstruido si el objetivo es limpiar artefactos musculares.
- Este patrón es característico de actividad muscular, especialmente en regiones como el músculo temporalis.
- La combinación de espectro ascendente, foco periférico y señal espiculada lo distingue de componentes neuronales.
![ICA000](https://github.com/PamelaVilchez/GRUPO-08-ISB-2025-II/blob/853d4118efc5cba81d2f582ad9d5edcd3fee1bbd/Repositorio-Im%C3%A1genes/0.png?raw=true)

#### Evaluación del componente ICA007 
En el componente **ICA007**, se observa que las zonas de mayor activación (representadas por los “blobs” en azul y rojo) están ubicadas **lejos del vértice**, es decir, alejadas de la parte superior central de la cabeza.

Esta distribución espacial sugiere un **foco periférico**, típico de artefactos musculares o señales no neuronales. La concentración de actividad en regiones laterales o cercanas a la cara refuerza esta hipótesis.

La imagen del topomap correspondiente muestra claramente esta configuración periférica, con los máximos y mínimos localizados en zonas externas del cuero cabelludo.

![ICA000](https://github.com/PamelaVilchez/GRUPO-08-ISB-2025-II/blob/853d4118efc5cba81d2f582ad9d5edcd3fee1bbd/Repositorio-Im%C3%A1genes/7.png?raw=true)



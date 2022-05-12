# LIME para entender VADR
Este proyecto aplica el modelo VADR a un conjunto de comentarios de YouTube para entender cuáles palabras determinan el score de negatividad del modelo.

## Resumen
El proyecto está dividido en tres partes:
1. Minar comentarios
2. Usar VADR para predecir el score negativo de los comentarios
3. Hacer modificaciones locales a los comentarios para determinar qué determina el score de negatividad

## Context
Los comentarios analizados en este proyecto se minaron del [trailer de lanzamiento de Battlefield 2042](https://www.youtube.com/watch?v=ASzOzrB-a9E).

Escogí este video porque Battlefield 2042 es considerado como uno de los peores lanzamientos de todos los tiempos. En las palabras de el blog de reseñas [_Kotaku_](https://kotaku.com/on-steam-farming-simulator-22-has-more-active-players-1848128969):
> "One of the biggest games of the year on one of the most popular digital stores in the world on one of the biggest gaming platforms in the world [...] isn't able to keep up with Farming Simulator 22.

Naturalmente, los comentarios en este video son mayormente negativos y presentan un buen caso de estudio para usar VADER como herramienta de análisis de sentimiento.
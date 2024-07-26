#**Descripción del Proyecto:**
La finalidad de este proyecto es construir un mínimo producto viable de una aplicación que nos ayude a encontrar información y que nos recomiende películas. 


#**Requisitos:**
Numpy, Pandas, re, itertools, matplotlib.pyplot, nltk, WordCloud, sklearn.


#**Estructura del Proyecto:**
datasets: En esta carpeta contiene todo los datasets utilizados en el modelo.
Fast_api: Aquí encontramos nuestro ambiente virtual y el archivo proyecto.py que contiene el deployment de la aplicación. 
Proyecto_Integrador_limpieza_y_funciones: Este notebook contiene todo el código para lograr el análisis y la limpieza de los datos.
requirements: Este archivo contiene las librerías necesarias, y sus versiones, para el deployment de la API en render.


#**Uso y Ejecución:**
  1.	En el notebook Proyecto_Integrador_limpieza_y_funciones se encuentra bien documentado el código para lograr la limpieza de datos.
  Las principales acciones que se tomaron: desanidar datos de columnas, unión de información de dos diferentes datasets, transformación de datos fecha, búsqueda de valores nulos y duplicados, cálculos de columnas, eliminación de de filas y columnas.
  2.	 También en en el notebook Proyecto_Integrador_limpieza_y_funciones se encuentra el arquetipo de todas las funciones utilizadas en el desarrollo de la API
  3.	Por último, también en Proyecto_Integrador_limpieza_y_funciones, se puede hallar el arquetipo del modelo de recomendación. Para este modelo hacemos tokenizacion, eliminación de stopwords y stemming para las sinopsis de las películas. 
  4.	Para correr el modelo en local hay que activar primero el entorno virtual en la carpeta Fast_api. Una vez activado, asegurándose que las librerías necesarias estén instaladas en el entorno, correr el comando uvicorn proyecto:app. Proyecto porque es el nombre de nuestro archivo Python que controla la creación de la API y app es el nombre que le dimos a nuestra aplicación.
  5.	Para correr el modelo deployado, seguir el enlace: https://primer-proyecto-integrado-r.onrender.com


#**Metodología**: 
Para realizar el sistema de recomendación, con la ayuda de la algoritmo de la similitud del coseno, hallamos las sinopsis y géneros que se parecen; además añadimos como variable el puntaje para darle peso en la recomendación a películas con buena puntuación.
   

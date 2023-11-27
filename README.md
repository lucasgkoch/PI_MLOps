# Proyecto individual MLOps

Este proyecto se centra en el desarrollo de una API que ofrece información detallada sobre juegos de Steam, usuarios y recomendaciones . Utilizando conjuntos de datos específicos de Steam, he implementado endpoints que proporcionan datos relevantes sobre juegos, reseñas de usuarios y elementos del juego. La API, creada con Python y FastAPI, ha sido optimizada para brindar respuestas rápidas y eficientes. Además, he incorporado un modelo de recomendación de juegos mediante machine learning. El proceso ETL garantiza la limpieza y eficiencia en el manejo de grandes conjuntos de datos. El servicio web está actualmente desplegado en Render, lo que permite un acceso fácil y rápido a esta valiosa información sobre la plataforma Steam.

## Tecnologías Utilizadas

- Python
- Pandas
- FastAPI
- Uvicorn
- Render

## Estructura del Proyecto

El repositorio está organizado de la siguiente manera:

- **root**: Contiene Jupyter Notebooks como `ETL_EDA_games.ipynb`, `ETL_EDA_items.ipynb`, y `ETL_EDA_reviews.ipynb`, donde se lleva a cabo el proceso de Extracción, Transformación y Análisis Exploratorio de Datos.

- **raw_data**: Aquí se encuentran los datasets originales recibidos en formato JSON

- **processed_data**: Esta carpeta almacena los datasets procesados y limpios generados durante el ETL/EDA.

- **API**: Contiene todo lo necesario para ejecutar la API en Render. Incluye los archivos esenciales como `main` y `functions.py`, además de los datasets optimizados para los endpoints.

- **assets**: En esta carpeta se encuentran recursos adicionales, como imágenes, utilizados en los Jupyter Notebooks y en la documentación.



## Proceso de Desarrollo

### Extracción de Datos

Recibí tres conjuntos de datos en formato JSON: `output_steam_games.json`, `australian_user_reviews.json`, y `australian_user_items.json`. Utilicé Pandas para cargar estos datos en dataframes.

### ETL Inicial

Realicé un proceso de ETL inicial en un Jupyter Notebook llamado [ETL_inicial](ETL_inicial.ipynb) para realizar limpiezas generales y visualizar la información de los datasets.

### Definición de Campos Necesarios

Elaboré una tabla en Excel destacando los campos necesarios de cada dataset para los distintos endpoints de la API.

https://docs.google.com/spreadsheets/d/1VMXfzuVTL1q-LO6SD5CEii_C-iBGNta8IEZz_Y_y4qE/edit?usp=sharing

### ETL/EDA Profundo

Realicé ETL/EDA más profundo a cada dataset en archivos Jupyter Notebook como[ETL_EDA_games]( ETL_EDA_games.ipynb) ,[ETL_EDA_items](ETL_EDA_items.ipynb), y[ETL_EDA_reviews](ETL_EDA_reviews.ipynb).

### Almacenamiento de Datos

Guardé los datasets limpios y listos para el consumo en formato Parquet: `games.parquet`, `items.parquet`, `reviews.parquet`.

### ETL Específicos para la API

Para evitar cargas pesadas en la API, realicé ETL específicos para proporcionar datasets reducidos y optimizados para los endpoints.

[ETL_functions](ETL_functions.ipynb)

### Modelo de Machine Learning

Implementé un modelo de recomendación en el archivo [modelo_item_item](modelo_item_item.ipynb) para el endpoint `recomendacion_juegos`.

### Configuración de la API

Creé un entorno virtual, configuré la instancia de FastAPI en el archivo `main` y definí los endpoints, creé un archivo `functions.py` donde se encuentra las funciones para cada endpoint.

### Prueba Local

Creé un virtual enviroment e inicié el servidor Uvicorn localmente con el comando `uvicorn main:app --reload` y verifiqué el correcto funcionamiento de la API.

### Deploy en Render

Creé un archivo `requirements.txt` con las dependencias necesarias y desplegué la API en Render, donde está actualmente funcionando y disponible online.

## Uso de la API

La API proporciona diversos endpoints para obtener información específica sobre juegos de Steam y realizar consultas personalizadas. A continuación, se detallan algunos de los endpoints disponibles:

- **/PlayTimeGenre/{genre}**
  - Devuelve el año con más tiempo de juego para un género específico.
  
- **/UserForGenre/{genre}**
  - Proporciona detalles sobre el usuario que acumula más horas jugadas para el género dado.
  
- **/UsersRecommend/{year}**
  - Devuelve el top 3 de juegos más recomendados por usuarios para el año dado.
  
- **/UsersWorstDeveloper/{year}**
  - Devuelve el top 3 de desarrolladoras con juegos menos recomendados por usuarios para el año dado.
  
- **/sentiment_analysis/{developer}**
  - Devuelve un análisis de sentimientos para un desarrollador específico.
  
- **/recomendacion_juego/{id}**
  - Recomienda 5 juegos similares al ID de juego ingresado.

### Ejemplos de Uso

- Para obtener el año con más tiempo de juego para el género "Action":
/PlayTimeGenre/Action


- Para detalles sobre el usuario que acumula más horas jugadas para el género "Indie":
/UserForGenre/Indie


- Para obtener el top 3 de juegos más recomendados por usuarios para el año 2012:
/UsersRecommend/2012


- Para obtener el análisis de sentimientos para el desarrollador "Valve":
/sentiment_analysis/Valve


- Para recibir recomendaciones de juegos similares al ID de juego 10:
/recomendacion_juego/10


## Contacto

Si tienes alguna pregunta, sugerencia o simplemente quieres ponerte en contacto, no dudes en hacerlo:

- **Correo Electrónico:** [lucasgabrielkoch1997@gmail.com](lucasgabrielkoch1997@gmail.com)
- **GitHub:** [lucasgkoch](https://github.com/lucasgkoch)
- **LinkedIn:** [Lucas Koch](https://www.linkedin.com/in/lucas-gkoch/)



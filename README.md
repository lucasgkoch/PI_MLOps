# Nombre del Proyecto

"Este proyecto se centra en el desarrollo de una API que ofrece información detallada sobre juegos de Steam, usuarios y recomendaciones personalizadas. Utilizando conjuntos de datos específicos de Steam, hemos implementado endpoints que proporcionan datos relevantes sobre juegos, reseñas de usuarios y elementos del juego. La API, creada con Python y FastAPI, ha sido optimizada para brindar respuestas rápidas y eficientes. Además, hemos incorporado un modelo de recomendación de juegos mediante machine learning. El proceso ETL garantiza la limpieza y eficiencia en el manejo de grandes conjuntos de datos. El servicio web está actualmente desplegado en Render, lo que permite un acceso fácil y rápido a esta valiosa información sobre la plataforma Steam."

## Tecnologías Utilizadas

- Python
- Pandas
- FastAPI
- Uvicorn
- Render

## Estructura del Proyecto

Explicación breve de la estructura de directorios y archivos importantes en tu repositorio.

## Proceso de Desarrollo

### Extracción de Datos

Recibí tres conjuntos de datos en formato JSON: `output_steam_games.json`, `australian_user_reviews.json`, y `australian_user_items.json`. Utilicé Pandas para cargar estos datos en dataframes.

### ETL Inicial

Realicé un proceso de ETL inicial en un Jupyter Notebook llamado `ETL_inicial.ipynb` para realizar limpiezas generales y visualizar la información de los datasets.

### Definición de Campos Necesarios

Elaboré una tabla en Excel destacando los campos necesarios de cada dataset para los distintos endpoints de la API.

[Tabla de Campos](enlace a la tabla de excel alojada en la web)

### ETL/EDA Profundo

Realicé ETL/EDA más profundo a cada dataset en archivos Jupyter Notebook como `ETL_EDA_games.ipynb`, `ETL_EDA_items.ipynb`, y `ETL_EDA_reviews.ipynb`.

### Almacenamiento de Datos

Guardé los datasets limpios y listos para el consumo en formato Parquet: `games.parquet`, `items.parquet`, `reviews.parquet`.

### ETL Específicos para la API

Para evitar cargas pesadas en la API, realicé ETL específicos para proporcionar datasets reducidos y optimizados para los endpoints.

[Enlace a ETL Functions](ETL_functions.ipynb)

### Modelo de Machine Learning

Implementé un modelo de recomendación en el archivo `modelo_item_item.ipynb` para el endpoint `recomendacion_juegos`.

### Configuración de la API

Creé un entorno virtual, configuré la instancia de FastAPI en el archivo `main`, y definí los endpoints utilizando `functions.py`.

### Prueba Local

Inicié el servidor Uvicorn localmente con el comando `uvicorn main:app --reload` y verifiqué el correcto funcionamiento de la API.

### Deploy en Render

Creé un archivo `requirements.txt` con las dependencias necesarias y desplegué la API en Render, donde está actualmente funcionando y disponible online.

## Uso de la API

Instrucciones sobre cómo utilizar la API, ejemplos de solicitudes y respuestas, etc.

## Contribuciones

Cómo los colaboradores pueden contribuir al proyecto, instrucciones para enviar solicitudes de extracción, etc.

## Licencia

Detalles sobre la licencia del proyecto.

## Contacto

Cómo ponerse en contacto contigo, enlaces a redes sociales, correo electrónico, etc.


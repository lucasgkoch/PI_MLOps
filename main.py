from fastapi import FastAPI
from typing import Union
from fastapi.responses import HTMLResponse
from typing import List, Dict, Tuple, Sequence, Any, Union, Optional, Callable
from functions import PlayTimeGenre
from functions import UserForGenre
from functions import UsersRecommend
from functions import UsersWorstDeveloper
from functions import sentiment_analysis
from functions import recomendacion_juego

app = FastAPI()


#@app.get("/")
#async def root():
#    return {"message": "PI_MLOps Lucas Koch"}

@app.get("/", response_class=HTMLResponse)
async def root():
    html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>API PI_MLOps</title>
            <style>
                body {
                    font-family: 'Roboto', sans-serif;
                    background-color: #1e1e1e; /* Fondo oscuro */
                    color: #d4d4d4; /* Color de texto claro */
                    margin: 20px;
                    line-height: 1.6;
                }

                h1, h2 {
                    color: #d19a66; /* Color de los encabezados */
                    text-shadow: 2px 2px 4px #333; /* Sombra para resaltar los encabezados */
                }

                 ul {
                    list-style: none; /* Quita los puntos de la lista */
                    padding: 0;
                }

                li {
                    margin-bottom: 10px;
                }

                a {
                    color: #e5c07b; /* Color del enlace */
                    text-decoration: none;
                    font-weight: bold;
                }

                a:hover {
                    text-decoration: underline;
                }
            </style>
        </head>
        <body>

            <h1>Bienvenido a la API PI_MLOps</h1>

            <p>¡Hola! Soy Lucas Koch, creador de este proyecto.</p>
            <p>Esta API ofrece consultas útiles basadas en datos de Steam relacionados con juegos, usuarios y reseñas.</p>

            <h2>Endpoints Disponibles:</h2>

            <ul>
                <li><strong><a href="/PlayTimeGenre/Action">/PlayTimeGenre/{genre}</a></strong>: Devuelve el año con mas tiempo de juego para un género específico.                             </li>
                <li><strong><a href="/UserForGenre/Indie">/UserForGenre/{genre}</a></strong>: Proporciona detalles sobre el usuario que acumula más horas jugadas para el género dado.</li>
                <li><strong><a href="/UsersRecommend/2012">/UsersRecommend/{year}</a></strong>: Devuelve el top 3 de juegos mas recomendados por usuarios para el año dado.</li>
                <li><strong><a href="/UsersWorstDeveloper/2014">/UsersWorstDeveloper/{year}</a></strong>: Devuelve el top 3 de desarrolladoras con juegos menos recomendados por usuarios para el año dado.</li>
                <li><strong><a href="/sentiment_analysis/Valve">/sentiment_analysis/{developer}</a></strong>: Devuelve análisis de sentimientos para un desarrollador específico.</li>
                <li><strong><a href="/recomendacion_juego/10">/recomendacion_juego/{id}</a></strong>: recomienda 5 juegos similares al id de juego ingresado.</li>
            </ul>

            <h3>Contacto:</h3>
            <p>Si tienes algún inconveniente con la API, ¡no dudes en contactarme!</p>
            <p>Mi perfil en GitHub: <a href="https://github.com/lucasgkoch">lucasgkoch</a></p>
            <p>Mi correo electrónico: <a href="lucasgabrielkoch1997@gmail.com">lucasgabrielkoch1997@gmail.com</a></p>

        </body>
        </html>
    """
    return HTMLResponse(content=html_content)

@app.get("/PlayTimeGenre/{genre}")
async def user(genre: str):
    try:
        result = PlayTimeGenre(genre)
        return result
    except Exception as e:
        return {"error": str(e)}
    

@app.get("/UserForGenre/{genre}")
async def user(genre: str):
    try:
        result = UserForGenre(genre)
        return result
    except Exception as e:
        return {"error": str(e)}
    

@app.get("/UsersRecommend/{year}")
async def user(year: int):
    try: 
        result = UsersRecommend(year)
        return result
    except Exception as e:
        return {"error": str(e)}  
    

@app.get("/UsersWorstDeveloper/{year}")
async def user(year: int):
    try:
        result = UsersWorstDeveloper(year)
        return result
    except Exception as e:
        return {"error": str(e)}  
    
    
@app.get("/sentiment_analysis/{developer}")
async def user(developer: str):
    try:
        result = sentiment_analysis(developer)
        return result
    except Exception as e:
        return {"error": str(e)}
    

@app.get("/recomendacion_juego/{id}")
async def user(id: int):
    try:
        result = recomendacion_juego(id)
        return result
    except Exception as e:
        return {"error": str(e)}
    

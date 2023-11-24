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
            <title>Presentación de la API</title>
        </head>
        <body>

            <h1>Bienvenido a la API de PI_MLOps</h1>

            <p>¡Hola! Mi nombre es Lucas Koch, y este es el proyecto PI_MLOps.</p>

            <h2>Endpoints Disponibles:</h2>

            <ul>
                <li><strong>/PlayTimeGenre/{genre}</strong>: Devuelve información sobre el tiempo de juego para un género específico.</li>
                <li><strong>/UserForGenre/{genre}</strong>: Proporciona detalles sobre los usuarios para un género dado.</li>
                <li><strong>/UsersRecommend/{year}</strong>: Muestra recomendaciones de usuarios para un año específico.</li>
                <li><strong>/UsersWorstDeveloper/{year}</strong>: Indica los peores desarrolladores según los usuarios para un año determinado.</li>
                <li><strong>/sentiment_analysis/{developer}</strong>: Realiza análisis de sentimientos para un desarrollador específico.</li>
                <li><strong>/recomendacion_juego/{id}</strong>: Ofrece recomendaciones de juego para un ID específico.</li>
            </ul>

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
    

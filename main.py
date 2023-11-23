from fastapi import FastAPI
from typing import Union
from fastapi.responses import JSONResponse
from typing import List, Dict, Tuple, Sequence, Any, Union, Optional, Callable
from functions import PlayTimeGenre
from functions import UserForGenre
from functions import UsersRecommend
from functions import UsersWorstDeveloper
from functions import sentiment_analysis

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "PI_MLOps Lucas Koch"}


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
        year_int = int(year) 
        result = UsersRecommend(year_int)
        return result
    except Exception as e:
        return {"error": str(e)}  
    

@app.get("/UsersWorstDeveloper/{year}")
async def user(year: int):
    try:
        year_int = int(year) 
        result = UsersWorstDeveloper(year_int)
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
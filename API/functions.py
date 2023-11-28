import pandas as pd
from collections import Counter

  
#funcion 1

def PlayTimeGenre(genre: str):
    '''
    """
    Devuelve el año de lanzamiento con más horas jugadas para un género específico.

    Parámetros:
    genre (str): El género para el cual se busca el año con más horas jugadas.

    Retorna:
    dict: Un diccionario que contiene el resultado de la búsqueda. Puede tener las siguientes claves:
          - "Año de lanzamiento con más horas jugadas para {genre}": El año de lanzamiento con más horas jugadas.
          - "No hay datos disponibles para el género {genre}": Mensaje si no hay datos disponibles para el género especificado.
          - "Error": Mensaje de error si el parámetro 'genre' no es una cadena (str).

    Ejemplo:
    >>> PlayTimeGenre("Action")
    {'Año de lanzamiento con más horas jugadas para Action': 2010}

    Nota:
    Esta función utiliza un dataset cargado previamente ('API/play_time_genre.parquet').
    """
    '''

    #Se verifica que el valor ingresado sea str
    if not isinstance(genre, str):
        return {"Error": "El parámetro 'genero' debe ser una cadena (str)"}
    
    #Se carga el dataset provisto para esta funcion
    df_max_year_per_genre=pd.read_parquet('API/play_time_genre.parquet')

    #Se filtra el DataFrame para el género especificado
    df_genre = df_max_year_per_genre[df_max_year_per_genre['genres'] == genre]

    # Verifica si el género está presente en el DataFrame
    if not df_genre.empty:
        #Se guarda el año con más horas jugadas para el género
        año_max_horas = int(df_genre.iloc[0]['release_year'])
    else:
        return {"No hay datos disponibles para el género {}".format(genre)}

    return {"Año de lanzamiento con más horas jugadas para {}: {}".format(genre, int(año_max_horas))}




#funcion 2

def UserForGenre(genre: str):
    """
    Devuelve el usuario con más horas jugadas y las horas jugadas por año para un género específico.

    Parámetros:
    genre (str): El género para el cual se busca el usuario con más horas jugadas.

    Retorna:
    dict: Un diccionario que contiene el resultado de la búsqueda. Puede tener las siguientes claves:
          - "Usuario con más horas jugadas para Género {genre}": El ID del usuario con más horas jugadas.
          - "Horas jugadas": Una lista de diccionarios que contiene información sobre las horas jugadas por año.
            Cada diccionario tiene las claves "Año" y "Horas".

          Ejemplo:
          {'Usuario con más horas jugadas para Género Action': 'usuario123',
           'Horas jugadas': [{'Año': 2010, 'Horas': 150}, {'Año': 2011, 'Horas': 200}]}

          - "No hay datos disponibles para el género {genre}": Mensaje si no hay datos disponibles para el género especificado.
          - "Error": Mensaje de error si el parámetro 'genre' no es una cadena (str).

    Nota:
    Esta función utiliza un dataset cargado previamente ('API/user_for_genre.parquet').
    """


    #Se verifica que el valor ingresado sea str
    if not isinstance(genre, str):
        return {"Error": "El parámetro 'genero' debe ser una cadena (str)"}
    
    #Se carga el dataset provisto para esta funcion
    df_max_user_per_genre=pd.read_parquet('API/user_for_genre.parquet')

    #Se filtra el DataFrame para el género especificado
    df_genre = df_max_user_per_genre[df_max_user_per_genre['genres'] == genre]

    #Se verifica si se encontro el genero solicitado
    if not df_genre.empty:

        user= df_genre.iloc[1]['user_id']
        #Se crea el diccionario de retorno
        result_dict = {
            "Usuario con más horas jugadas para Género {}".format(genre): user,
            "Horas jugadas": [{"Año": int(year), "Horas": int(hours)} for year, hours in zip(df_genre['release_year'], df_genre['playtime_forever']/60)]    
        }
      
    else:
        return {"No hay datos disponibles para el género {}".format(genre)}

    return result_dict
    

#funcion 3

def UsersRecommend(year: int):
    """
    Devuelve una lista con el top 3 de juegos recomendados para un año específico.

    Parámetros:
    year (int): El año para el cual se busca el top de juegos recomendados.

    Retorna:
    list: Una lista de diccionarios que contiene el top 3 de juegos recomendados.
          Cada diccionario tiene la clave "Puesto {i+1}" y el valor del juego.

          Ejemplo:
          [{'Puesto 1': 'Nombre del juego 1'},
           {'Puesto 2': 'Nombre del juego 2'},
           {'Puesto 3': 'Nombre del juego 3'}]

          - Si no hay datos disponibles para el año proporcionado, se devuelve una lista vacía.
          - Si se produce un error (por ejemplo, el año no es un entero), se devuelve un diccionario con el mensaje de error.

    Nota:
    Esta función utiliza dos datasets cargados previamente ('API/games_endpoints.parquet' y 'API/reviews.parquet').
    """
    #Se verifica que el dato ingresado sea adecuado
    try:
        year = int(year)

        #Se cargan los datasets
        df_games=pd.read_parquet('API/games_endpoints.parquet')
        df_reviews_complete=pd.read_parquet('API/reviews.parquet')

        #Se crean los dataframes solo con las columnas necesarias para trabajar
        df_reviews=df_reviews_complete[['posted_year','item_id','recommend','sentiment_analysis']]
        del df_reviews_complete

        #Se filtran las revisiones para el año dado, las recomendaciones y si el sentimiento es positivo o neutral
        filtered_reviews = df_reviews[(df_reviews['posted_year'] == year) & (df_reviews['recommend']) & (df_reviews['sentiment_analysis'].isin([1, 2]))]

        #Se unen los dataframes
        filtered_reviews['item_id'] = filtered_reviews['item_id'].astype(int)
        df_games['id'] = df_games['id'].astype(int)
        merged_df = pd.merge(filtered_reviews, df_games, left_on='item_id', right_on='id', how='inner')

        #Se calcula el número de recomendaciones para cada juego
        game_recommendations = merged_df['app_name'].value_counts()
        #print(game_recommendations)

        #Se busca el top 3 de juegos
        top_3_games = game_recommendations.head(3)
        #print(top_3_games)

        #Se crea la lista de resultados en el formato solicitado
        list = [{"Puesto {}".format(i + 1): game} for i, game in enumerate(top_3_games.index)]

        return list
    except Exception:
        return {"Error": "Por favor, ingrese un año válido como entero"}




#funcion 4

def UsersWorstDeveloper(year: int):
    """
    Devuelve una lista con el top 3 de desarrolladores con más juegos no recomendados para un año específico.

    Parámetros:
    year (int): El año para el cual se busca el top de desarrolladores con más juegos no recomendados.

    Retorna:
    list: Una lista de diccionarios que contiene el top 3 de desarrolladores con más juegos no recomendados.
          Cada diccionario tiene la clave "Puesto {i+1}" y el valor del nombre del desarrollador.

          Ejemplo:
          [{'Puesto 1': 'Nombre del desarrollador 1'},
           {'Puesto 2': 'Nombre del desarrollador 2'},
           {'Puesto 3': 'Nombre del desarrollador 3'}]

          - Si no hay datos disponibles para el año proporcionado, se devuelve una lista vacía.
          - Si se produce un error (por ejemplo, el año no es un entero), se devuelve un diccionario con el mensaje de error.

    Nota:
    Esta función utiliza dos datasets cargados previamente ('API/games_endpoints.parquet' y 'API/reviews.parquet').
    """
    #Se verifica que el dato ingresado sea adecuado
    try:
        year = int(year)

        #Se cargan los datasets
        df_games=pd.read_parquet('API/games_endpoints.parquet')
        df_reviews_complete=pd.read_parquet('API/reviews.parquet')

        #Se crean los dataframes solo con las columnas necesarias para trabajar
        df_reviews=df_reviews_complete[['posted_year','item_id','recommend','sentiment_analysis']]
        del df_reviews_complete

        #Se filtran las revisiones para el año dado, las no recomendaciones y si el sentimiento es negativo
        filtered_reviews = df_reviews[(df_reviews['posted_year'] == year) & (df_reviews['recommend']==False) & (df_reviews['sentiment_analysis']==0)]
        #print(filtered_reviews)

        #Se unen los dataframes
        filtered_reviews['item_id'] = filtered_reviews['item_id'].astype(int)
        df_games['id'] = df_games['id'].astype(int)
        merged_df = pd.merge(filtered_reviews, df_games, left_on='item_id', right_on='id', how='inner')

        #Se calcula el número de NO recomendaciones para cada developer
        developer_counts = merged_df['developer'].value_counts()
        #print(developer_counts)

        #Se busca el top 3 de developers con mas NO recomendaciones
        top_3_worst_developers = developer_counts.head(3)
        #print(top_3_worst_developers)

        #Se crea la lista de resultados en el formato solicitado
        list = [{"Puesto {}".format(i + 1): developer} for i, developer in enumerate(top_3_worst_developers.index)]

        return list
    except ValueError:
        return {"Error": "Por favor, ingrese un año válido como entero"}
    



#funcion 5

def sentiment_analysis(developer: str):
    """
    Realiza un análisis de sentimiento de las revisiones para juegos de un desarrollador específico.

    Parámetros:
    developer (str): El nombre del desarrollador para el cual se realiza el análisis de sentimiento.

    Retorna:
    dict: Un diccionario que contiene el análisis de sentimiento para el desarrollador dado.
          La estructura del diccionario es la siguiente:
          {
            "Nombre del desarrollador": {
                'Negative': Cantidad de revisiones con sentimiento negativo,
                'Neutral': Cantidad de revisiones con sentimiento neutral,
                'Positive': Cantidad de revisiones con sentimiento positivo
            }
          }

          Ejemplo:
          {'Nombre del desarrollador': {'Negative': 50, 'Neutral': 30, 'Positive': 20}}

          - Si no hay datos disponibles para el desarrollador proporcionado, se devuelve un diccionario vacío.
          - Si se produce un error (por ejemplo, el desarrollador no es una cadena), se devuelve un diccionario con el mensaje de error.

    Nota:
    Esta función utiliza dos datasets cargados previamente ('API/games_endpoints.parquet' y 'API/reviews.parquet').
    """
    #Se verifica que el valor ingresado sea str
    if not isinstance(developer, str):
        return {"Error": "El parámetro 'genero' debe ser una cadena (str)"}
    
    #Se cargan los datasets
    df_games=pd.read_parquet('API/games_endpoints.parquet')
    df_reviews_complete=pd.read_parquet('API/reviews.parquet')
    
    #Se crean los dataframes solo con las columnas necesarias para trabajar
    df_reviews=df_reviews_complete[['item_id','sentiment_analysis']]
    
    #Se filtran las revisiones para la desarrolladora dada
    df_games['id'] = df_games['id'].astype(int)
    df_reviews['item_id'] = df_reviews['item_id'].astype(int)
    filtered_reviews = df_reviews[df_reviews['item_id'].isin(df_games[df_games['developer'] == developer]['id'])]
    #print(filtered_reviews)

    #Se cuenta la cantidad de registros para cada categoría de sentimiento
    #sentiment_counts = filtered_reviews['sentiment_analysis'].value_counts() NO FUNCIONA EN LA API(problema con versiones)
    sentiment_list = filtered_reviews['sentiment_analysis'].astype(int).tolist()
    sentiment_counts = Counter(sentiment_list)

    #Se crea el diccionario solicitado
    result = {developer: {'Negative': sentiment_counts.get(0, 0),
                                'Neutral': sentiment_counts.get(1, 0),
                                'Positive': sentiment_counts.get(2, 0)}}
    return result




#funcion 6

def recomendacion_juego(id: int):
    """
    Devuelve una lista de recomendaciones de juegos para un ID específico según un modelo de recomendación.

    Parámetros:
    id (int): El ID del juego para el cual se buscan recomendaciones.

    Retorna:
    list: Una lista de recomendaciones de juegos para el ID proporcionado. Puede contener hasta 5 elementos.

          Ejemplo:
          [123, 456, 789, 987, 654]

          - Si el ID no existe en el dataset, se devuelve un mensaje indicando que el ID no existe.
          - Si no hay recomendaciones disponibles para el ID proporcionado, se devuelve un mensaje indicando que no hay recomendaciones.
          - Si se produce un error (por ejemplo, el ID no es un entero), se devuelve un diccionario con el mensaje de error.

    Nota:
    Esta función utiliza un dataset cargado previamente ('API/games_recommendations.parquet') que contiene la columna 'recommended_5'.
    """
    #Se verifica que el dato ingresado sea adecuado
    try:
        id = int(id)

        #Se carga el parquet que contiene la columna resultante de aplicar el modelo a cada registro    
        df_games=pd.read_parquet('API/games_recommendations.parquet')

        if id not in df_games['id'].values:
            return "El id ingresado no existe en el dataset"

        # Filtrar el DataFrame para obtener las filas correspondientes al ID proporcionado
        resultados = df_games.loc[df_games['id'] == id, 'recommended_5']
    
        if not resultados.empty:
            # Si hay resultados, devolver la lista de recomendaciones (tomando solo los primeros 5)
            return resultados.iloc[0].tolist()
        else:
        
            return "No hay recomendaciones disponibles para el id ingresado"
    
    except ValueError:
        return {"Error": "Por favor, ingrese un año válido como entero"}

import pandas as pd
from collections import Counter

  
#funcion 1
'''
    Debe devolver año con mas horas jugadas para dicho género
'''
def PlayTimeGenre(genre: str):
    
    #Se verifica que el valor ingresado sea str
    if not isinstance(genre, str):
        return {"Error": "El parámetro 'genero' debe ser una cadena (str)"}
    
    #Se carga el dataset provisto para esta funcion
    df_max_year_per_genre=pd.read_parquet('play_time_genre.parquet')

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
'''
    Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.
'''
def UserForGenre(genre: str):
    #Se verifica que el valor ingresado sea str
    if not isinstance(genre, str):
        return {"Error": "El parámetro 'genero' debe ser una cadena (str)"}
    
    #Se carga el dataset provisto para esta funcion
    df_max_user_per_genre=pd.read_parquet('user_for_genre.parquet')

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
'''
    Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos/neutrales)
'''
def UsersRecommend(year: int):
    #Se verifica que el dato ingresado sea adecuado
    try:
        year = int(year)

        #Se cargan los datasets
        df_games=pd.read_parquet('games_endpoints.parquet')
        df_reviews_complete=pd.read_parquet('reviews.parquet')

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
    except ValueError:
        return {"Error": "Por favor, ingrese un año válido como entero"}




#funcion 4
'''
    Devuelve el top 3 de desarrolladoras con juegos MENOS recomendados por usuarios para el año dado. (reviews.recommend = False y comentarios negativos)
'''
def UsersWorstDeveloper(year: int):
    #Se verifica que el dato ingresado sea adecuado
    try:
        year = int(year)

        #Se cargan los datasets
        df_games=pd.read_parquet('games_endpoints.parquet')
        df_reviews_complete=pd.read_parquet('reviews.parquet')

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
'''
    Según la empresa desarrolladora, se devuelve un diccionario con el nombre de la desarrolladora como llave
     y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor.
'''
def sentiment_analysis(developer: str):

    #Se verifica que el valor ingresado sea str
    if not isinstance(developer, str):
        return {"Error": "El parámetro 'genero' debe ser una cadena (str)"}
    
    #Se cargan los datasets
    df_games=pd.read_parquet('games_endpoints.parquet')
    df_reviews_complete=pd.read_parquet('reviews.parquet')
    
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
'''
    Ingresando el id de producto, deberíamos recibir una lista con 5 juegos recomendados similares al ingresado.
'''
def recomendacion_juego(id: int):

    #Se verifica que el dato ingresado sea adecuado
    try:
        id = int(id)

        #Se carga el parquet que contiene la columna resultante de aplicar el modelo a cada registro    
        df_games=pd.read_parquet('games_recommendations.parquet')

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

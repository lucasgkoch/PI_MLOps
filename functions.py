import pandas as pd
from collections import Counter

#Se cargan los dataframes
#df_games_complete=pd.read_parquet('games.parquet')
#df_items_complete=pd.read_parquet('items.parquet')
#df_reviews_complete=pd.read_parquet('reviews.parquet')
#df_games_functions=pd.read_parquet('games_functions.parquet')

#funcion 1
def PlayTimeGenre(genre: str):
    #Se verifica que el valor ingresado sea str
    if not isinstance(genre, str):
        return {"Error": "El parámetro 'genero' debe ser una cadena (str)"}
    
    #Se cargan los datasets necesarios
    df_items_complete=pd.read_parquet('items.parquet')
    df_games_functions=pd.read_parquet('games_functions.parquet')


    #Se crean los dataframes solo con las columnas necesarias para trabajar
    #df_games=df_games_functions
    df_items=df_items_complete[['item_id','playtime_forever']]
    del df_items_complete
    
    #Se utiliza explode para desglosar las listas en la columna 'genres'
    #df_exploded = df_games.explode('genres')

    #Se filtra el DataFrame df_exploded por el género especificado
    df_filtered_games = df_games_functions[df_games_functions['genres'].str.contains(genre, case=False, na=False)]
    del df_games_functions

    #Se hace un join entre df_filtered_games y df_items usando 'id' y 'item_id'
    df_filtered_games['id'] = df_filtered_games['id'].astype(int)
    df_items['item_id'] = df_items['item_id'].astype(int)
    df_joined = pd.merge(df_filtered_games, df_items, left_on='id', right_on='item_id', how='inner')

    #verifica si df_joined esta vacio
    if df_joined.empty:
        return {"No hay datos disponibles para el género {}".format(genre)}

    #Se agrupa por año de lanzamiento y se suman las horas jugadas
    grouped_data = df_joined.groupby('release_year')['playtime_forever'].sum()

    #Se identifica el año con la máxima suma de horas jugadas
    max_year = grouped_data.idxmax()

    return {"Año de lanzamiento con más horas jugadas para {}: {}".format(genre, int(max_year))}




#funcion 2
def UserForGenre(genre: str):
    #Se verifica que el valor ingresado sea str
    if not isinstance(genre, str):
        return {"Error": "El parámetro 'genero' debe ser una cadena (str)"}
    
    #Se cargan los datasets necesarios
    df_items_complete=pd.read_parquet('items.parquet')
    df_games_functions=pd.read_parquet('games_functions.parquet')
    
    #Se crean los dataframes solo con las columnas necesarias para trabajar
    #df_games=df_games_functions
    df_items=df_items_complete[['user_id','item_id','playtime_forever']]
    del df_items_complete
    
    #Se utiliza explode para desglosar las listas en la columna 'genres'
    #df_exploded = df_games.explode('genres')

    #Se filtra el DataFrame df_exploded por el género especificado
    df_filtered_games = df_games_functions[df_games_functions['genres'].str.contains(genre, case=False, na=False)]
    del df_games_functions

    #Se elimina la columna generes para optimizar, ya que no sera necesaria
    df_filtered_games.drop(columns='genres',inplace=True)

    #Se hace un join entre df_filtered_games y df_items usando 'id' y 'item_id'
    df_filtered_games['id'] = df_filtered_games['id'].astype(int)
    df_items['item_id'] = df_items['item_id'].astype(int)
    df_joined = pd.merge(df_filtered_games, df_items, left_on='id', right_on='item_id', how='inner')

    del df_filtered_games
    del df_items

    #Se busca el usuario con más horas jugadas para el género dado
    user_max = df_joined.groupby('user_id')['playtime_forever'].sum().idxmax()

    #Se filtran las filas correspondientes al usuario con más horas
    df_user_max = df_joined[df_joined['user_id'] == user_max]
    #print(df_user_max)

    #Se agrupa por año y se suman las horas jugadas
    hours_per_year = df_user_max.groupby('release_year')['playtime_forever'].sum().reset_index()
    #print(hours_per_year)

    #Se crea el diccionario de retorno
    dict = {
        "Usuario con más horas jugadas para Género {}".format(genre): user_max,
        "Horas jugadas": [{"Año": int(year), "Horas": int(hours)} for year, hours in zip(hours_per_year['release_year'], hours_per_year['playtime_forever'])]
    }

    return dict




    

#funcion 3
def UsersRecommend(year: int):
    #Se verifica que el dato ingresado sea adecuado
    try:
        year = int(year)

        #Se cargan los datasets
        df_games_complete=pd.read_parquet('games.parquet')
        df_reviews_complete=pd.read_parquet('reviews.parquet')

        #Se crean los dataframes solo con las columnas necesarias para trabajar
        df_games=df_games_complete[['app_name','id']]
        del df_games_complete
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
def UsersWorstDeveloper(year: int):
    #Se verifica que el dato ingresado sea adecuado
    try:
        year = int(year)

        #Se cargan los datasets
        df_games_complete=pd.read_parquet('games.parquet')
        df_reviews_complete=pd.read_parquet('reviews.parquet')

        #Se crean los dataframes solo con las columnas necesarias para trabajar
        df_games=df_games_complete[['id','developer']]
        del df_games_complete
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

    #Se verifica que el valor ingresado sea str
    if not isinstance(developer, str):
        return {"Error": "El parámetro 'genero' debe ser una cadena (str)"}
    
    #Se cargan los datasets
    df_games_complete=pd.read_parquet('games.parquet')
    df_reviews_complete=pd.read_parquet('reviews.parquet')
    
    #Se crean los dataframes solo con las columnas necesarias para trabajar
    df_games=df_games_complete[['id','developer']]
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

    
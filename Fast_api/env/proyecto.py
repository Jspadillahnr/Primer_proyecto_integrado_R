from fastapi import FastAPI
import numpy as np 
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI()

# Lee el archivos Excel
datos_limpios = pd.read_excel('C:/Users/LENOVO/Documents/Henry/Primer_proyecto_integrado_R/datasets/datos_limpios.xlsx', engine='openpyxl')
df_ML= pd.read_excel('C:/Users/LENOVO/Documents/Henry/Primer_proyecto_integrado_R/datasets/datos_limpios_recomendar.xlsx', engine='openpyxl')

#score filmacion
@app.get("/score/{titulo_de_la_filmacion}")

def score_titulo(titulo_de_la_filmacion:str):
    
    for i, title in enumerate(datos_limpios['original_title']):
        if titulo_de_la_filmacion == title:
            year = datos_limpios['release_date'][i].year
            popularidad = datos_limpios['popularity'][i]
            return {"message":f'La película {titulo_de_la_filmacion} fue estrenada en el año {year} con un score/popularidad de {popularidad}'}
            break
    return {'error': f'Ups, la película {titulo_de_la_filmacion} no está en mi base. Por favor intenté el título de la película con todas las letras iniciales en mayúscula y con un sólo espacio entre palabras'}

#películas en un día
@app.get("/dia/{Dia}")
async def cantidad_filmaciones_dia(Dia:str):

    dia1 = Dia
    count = 0

    diccionario_traducción = {
        'Lunes':'Monday',
        'Martes':'Tuesday',
        'Miércoles':'Wednesday',
        'Jueves':'Thursday',
        'Viernes':'Friday',
        'Sábado':'Saturday',
        'Domingo':'Sunday'}
    
    if Dia in diccionario_traducción:
        for dates in datos_limpios['release_date']:
            date = dates.day_name()
            if date == diccionario_traducción[Dia]:
                count += 1
    else: 
        return {"error": "Por favor ingresar el día, sin abreviaciones, en español con la primera letra en mayúscula. Ej: Lunes, no acepta LUNES, lunes, Lun, etc"}
    return {"message": f'{count} películas fueron estrenadas en los días {Dia}'}

#peliculas por mes
@app.get("/mes/{Mes}")
def cantidad_filmaciones_mes(Mes:str):

    mes1 = Mes
    count = 0

    diccionario_traducción = {
        'Enero': 'January',
        'Febrero': 'February',
        'Marzo': 'March',
        'Abril': 'April',
        'Mayo': 'May',
        'Junio': 'June',
        'Julio': 'July',
        'Agosto': 'August',
        'Septiembre': 'September',
        'Octubre': 'October',
        'Noviembre': 'November',
        'Diciembre': 'December'}
    
    if Mes in diccionario_traducción:
        for months in datos_limpios['release_date']:
            month = months.month_name()
            if month == diccionario_traducción[Mes]:
                count += 1
    else: 
        return {'error':'Por favor ingresar el mes, sin abreviaciones, en español con la primera letra en mayúscula. Ej: Enero. No acepta enero, En, etc'}
    return {"message":f'{count} películas fueron estrenadas en los mes {mes1}'}

#actores
@app.get("/actores/{nombre_actor}")

def get_actor(nombre_actor):

    cantidad_de_peliculas = 0
    total_revenue = 0

    for i, reparto in enumerate(datos_limpios['cast']):
        if isinstance(reparto, str) and nombre_actor in reparto.split(", "):                   
            cantidad_de_peliculas += 1
            total_revenue += datos_limpios['revenue'][i]

    if cantidad_de_peliculas != 0:      
        return  {"message":f'El actor {nombre_actor} ha participado en {cantidad_de_peliculas} filmaciones, el mismo ha conseguido un retorno de {total_revenue} con un promedio de {total_revenue/cantidad_de_peliculas} por filmación'}
    else: 
        return {'error':f'Ups, el actor {nombre_actor} no está en mi base.'}
    


@app.get("/recomendar/{titulo_de_la_filmacion}")

def recomendar(titulo_de_la_filmacion:str):
    
    #recomendar por sinoposis
    df_ML['overview_clean'] = df_ML['overview_clean'].fillna('').astype(str)
    vectorizer_sinop = TfidfVectorizer()
    tfidf_matrix_sinop = vectorizer_sinop.fit_transform(df_ML['overview_clean'] )
    cosine_sim_sinop = cosine_similarity(tfidf_matrix_sinop)

    #recomendar por género
    df_ML['genres'] = df_ML['genres'].fillna('').astype(str)
    vectorizer_gen = TfidfVectorizer()  
    tfidf_matrix_gen = vectorizer_gen.fit_transform(df_ML['genres'])
    cosine_sim_gen = cosine_similarity(tfidf_matrix_gen)

    #recomendamos
    for i, nombre_pel in enumerate(df_ML['original_title']):
        if nombre_pel == titulo_de_la_filmacion:
            pel = i
            break

    df_ML['cos_gen'] = cosine_sim_gen[pel]
    df_ML['cos_sinop'] = cosine_sim_sinop[pel]
    df_ML['recommend_movie_score'] = (df_ML['cos_gen']*3) + (df_ML['cos_sinop']*10) + (df_ML['vote_average']/3)
    df_ordered = df_ML.sort_values(by='recommend_movie_score', ascending=False)

    return df_ordered['original_title'][1:6].tolist()



    
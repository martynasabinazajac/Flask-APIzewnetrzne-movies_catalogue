from flask import Flask
import json
import requests

app=Flask(__name__)

def get_popular_movies():
    api_data = "https://api.themoviedb.org/3/movie/popular"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxYTdmODg0ZTg4OGNiNGE0ZDk4ZjAzMDg0ODU4ZDA4NCIsInN1YiI6IjY0NDJjODVjZTJiY2E4MDJmYzQzNzkyZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.whb7JAM61hn-mAxwffEGxuyu28aESjSKZ9AaxUilAWI"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(api_data, headers=headers)
    results_movies=response.json()
    return results_movies

def get_poster_url(poster_api_path, size="w342"):
    base_url="https://image.tmdb.org/t/p/"
    return f'{base_url}{size}/{poster_api_path}'

#pobranie obazka
@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}

#funkcja odpowiedzialna z ilość wyswietlanych tytulów
def get_movies(how_many):
    data = get_popular_movies()
    return data["results"][:how_many]

if __name__=="__main__":
     app.run(debug=True)

  

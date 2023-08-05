import json
import requests
import os

API_TOKEN = os.environ.get("TMDB_API_TOKEN", "")

def header_endpoint(endpoint):
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()


def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    result = header_endpoint(endpoint)
    return result


def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"


# funkcja odpowiedzialna z ilość wyswietlanych tytulów
def get_movies(how_many, list_type):
    data = get_movies_list(list_type)
    return data["results"][:how_many]


# funkcja pobierająca z API szczegóły filmów:
def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    result = header_endpoint(endpoint)
    return result


# funkcja zwraca obsade dla danego filmu
def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    result = header_endpoint(endpoint)
    return result["cast"]


# utworzenie słownika z danymi tytuł:kod obrazka- odpowiedź w komentarzu zakomentuje tu tą funkcję
# def get_movie_info(list_type):
#     results_movies=get_movies_list(list_type)
#     results_movies2=results_movies["results"]
#     results_movies_dict={ x["title"]:x["poster_path"] for x in results_movies2}
#     return results_movies_dict

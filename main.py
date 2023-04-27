from flask import Flask, render_template
import tmdb_client
from flask import request

app = Flask(__name__)


# pobranie obazka
@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)

    return {"tmdb_image_url": tmdb_image_url}


# zachowanie aplikacji po wejściu na stronę główną
@app.route("/")
def homepage():
    movies_list = ["top_rated", "popular", "now_playing", "upcoming"]
    selected_list = request.args.get("list_type", "popular")
    if selected_list not in movies_list:
        selected_list = "popular"
    movies = tmdb_client.get_movies(how_many=8, list_type=selected_list)
    return render_template(
        "homepage.html",
        movies=movies,
        current_list=selected_list,
        lists=movies_list,
        list_type=selected_list,
    )


# odpytanie o szczegóły filmów
@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    cast = tmdb_client.get_single_movie_cast(movie_id)
    return render_template("movie_details.html", movie=details, cast=cast)


if __name__ == "__main__":
    app.run(debug=True)

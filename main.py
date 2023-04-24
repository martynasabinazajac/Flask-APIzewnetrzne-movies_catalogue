from flask import Flask, render_template
import tmdb_client


app=Flask(__name__)

#zachowanie aplikacji po wejściu na stronę główną
@app.route('/')
def homepage():
    movies = tmdb_client.get_movies(how_many=8)
    return render_template("homepage.html", movies=movies)

 # utworzenie słownika z danymi tytuł:kod obrazka   
def get_movie_info():
    results_movies=tmdb_client.get_popular_movies()
    results_movies2=results_movies["results"]
    results_movies_dict={ x["title"]:x["poster_path"] for x in results_movies2}
    return results_movies_dict

if __name__ == '__main__':
    app.run(debug=True)


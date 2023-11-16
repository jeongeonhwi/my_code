import requests
import json

api_key = "8705447c756fa62d8c95f823e7d9660c"
url = f"https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=en-US&page=1"

# response = requests.get(url)


popular_movies = requests.get(url).json()
# print(popular_movies)
movie_db = []
for movie in popular_movies['results']:
    movie_data = {
        "model": "movies.movie",
        "pk": movie['id'],
        "fields": {
            'title': movie['title'],
            'original_title': movie['original_title'],
            'overview': movie['overview'],
            'release_date': movie['release_date'],
            'popularity': movie['popularity'],
            'vote_average': movie['vote_average'],
            'poster_path': movie['poster_path'],
            'backdrop_path': movie['backdrop_path'],
            
    #         # 'runtime': runtime,
    #         # 'status': status,
    #         # 'tagline': tagline,

    #         # 'genres': genres,
    #         # 'actors': actors,
    #         # 'directors': directors,
    #         # 'keywords': keywords,
    #         # 'videos': videos,
    #         # 'providers': providers,
            }
    }
    
    movie_db.append(movie_data)

# JSON 파일로 저장
with open("movies_db.json", "w", encoding="utf-8") as json_file:
    json.dump(movie_db, json_file, ensure_ascii=False, indent=2)


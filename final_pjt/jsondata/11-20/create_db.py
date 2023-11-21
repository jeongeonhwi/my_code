import requests
import json

api_key = "8705447c756fa62d8c95f823e7d9660c"
url = f"https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=ko-KR&page="
# response = requests.get(url)


# print(popular_movies)
movie_db = []
actor_db = []
director_db = []
for page in range(1, 100):
    popular_url = url + str(page)
    popular_movies = requests.get(popular_url).json()
    for movie in popular_movies['results']:

        movie_id = movie['id']
        # 출연 감독, 배우 추출
        credit_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={api_key}&language=ko-KR"
        movie_credit = requests.get(credit_url).json()

        credit_flag = True

        actors = []
        tmp_actor_db = []
        # 배우 데이터 추출
        for actor in movie_credit["cast"][:4]:
            actor_id = actor['id']
            if type(actor_id) == int:

                actor_name = actor['name']
                actor_popularity = actor['popularity']
                actor_profile_path = actor['profile_path']

                if actor_name == "" or actor_popularity == 0 or actor_profile_path == None: # 필터링
                    credit_flag = False
                    break

                actors.append(actor_id)
                actor_data = {
                    "model": "movies.actor",
                    "pk": actor_id,
                    "fields": {
                        'name':actor_name,
                        'popularity':actor_popularity,
                        'profile_path':actor_profile_path,
                    }
                }
                actor_db.append(actor_data)

        # if not credit_flag or actors == []:
        #     continue
        # else:
        #     actor_db.append(tmp_actor_data)


        directors = []
        tmp_director_datas = []
        
        # 감독 데이터 추출
        for director in movie_credit["crew"]:
            if director.get('job') != 'Director':
                continue
            director_id = director['id']
            if type(director_id) == int:

                director_name = director['name']
                director_popularity = director['popularity']
                director_profile_path = director['profile_path']

                if director_name == "" or director_popularity == 0 or director_profile_path == None: # 필터링
                    credit_flag = False
                    break

                directors.append(director_id)
                director_data = {
                    "model": "movies.director",
                    "pk": director_id,
                    "fields": {
                        'name':director_name,
                        'popularity':director_popularity,
                        'profile_path':director_profile_path,
                    }
                }
                # tmp_director_datas = (director_data)
                director_db.append(director_data)

        if len(actors) == 0 or len(directors) == 0:
            continue
        # for actor in actors:

        # 무비 데이터 추출
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
                'actors': actors,
                'directors': directors,
                
        #         # 'runtime': runtime,
        #         # 'status': status,
        #         # 'tagline': tagline,

        #         # 'genres': genres,
        #         # 'keywords': keywords,
        #         # 'videos': videos,
        #         # 'providers': providers,
                }
        }
        
        movie_db.append(movie_data)
# JSON 파일로 저장
with open("movies_db.json", "w", encoding="utf-8") as json_file:
    json.dump(movie_db, json_file, ensure_ascii=False, indent=2)

with open("actors_db.json", "w", encoding="utf-8") as json_file:
    json.dump(actor_db, json_file, ensure_ascii=False, indent=2)

with open("directors_db.json", "w", encoding="utf-8") as json_file:
    json.dump(director_db, json_file, ensure_ascii=False, indent=2)


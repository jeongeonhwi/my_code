from django.urls import path
from . import views


urlpatterns = [
    # 영화 관련 
    path('movies/', views.movie_list),
    path('movies/<int:movie_pk>/', views.movie_detail),
    path('movies/<int:movie_pk>/actor/', views.movie_detail_actor),
    path('movies/<int:movie_pk>/director/', views.movie_detail_director),
    path('movies/<movie_name>/', views.find_movie),

    # 리뷰 관련
    path('review/<int:movie_pk>/', views.review),
    path('review/<int:movie_pk>/<int:review_pk>/', views.review_update_delete),
    
    # 추천 알고리즘
    path('latest/', views.latest_movie),
    path('recommended/', views.popularity_recommend_movie),
    path('popular_actor/', views.popular_actor),
    path('popular_director/', views.popular_director),

    # 배우 인기도순으로 정렬한 추천영화
    path('actor_population_movies/', views.actor_population_movies),

    # 감독 인기도순으로 정렬한 추천영화
    path('director_population_movies/', views.director_population_movies),
]
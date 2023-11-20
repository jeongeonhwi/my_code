from django.db import models
from django.conf import settings

# 감독
class Director(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    popularity = models.FloatField()
    profile_path = models.TextField(null=True, blank=True)


# 배우
class Actor(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    popularity = models.FloatField()
    profile_path = models.TextField(null=True, blank=True)


# # 장르
# class Genre(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=50)


# # 예고편
# class Preview(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=50)
#     key = models.CharField(max_length=50)
#     type = models.CharField(max_length=50)


# 키워드 // 얘는 완성하고 나중에 추가해보기 
# class Keyword(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=50)


# 나중에 볼 영화리스트

# 소통방
    


class Movie(models.Model):
    # user = models.ForeignKey(
    #     settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    # )
    id = models.IntegerField(primary_key=True)
    # pk = models.IntegerField()
    title = models.CharField(max_length=50)                             # 영화제목
    original_title = models.CharField(max_length=50)
    poster_path = models.TextField(null=True, blank=True)               # 포스터
    backdrop_path = models.TextField(null=True, blank=True)             # 디테일페이지 배경
    overview = models.TextField()                                   # 줄거리
    release_date = models.CharField(max_length=50)              # 개봉일
    popularity = models.FloatField()                            # 인기도
    runtime = models.IntegerField(null=True)                    # 러닝타임
    tagline = models.TextField()                                    # 포스터밑에 간단한 소개글
    video = models.TextField()  
    # status = models.CharField(max_length=50, null=True, blank=True) # 개봉여부
    # preview = models.ForeignKey(Preview, blank=True, null=True)
    vote_average = models.CharField(max_length=50)
    vote_count = models.CharField(max_length=50)

    # N:M 인 애들 
    like_movie = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="liked_movies")
    save_movie = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="saved_movies")

    # genres = models.ManyToManyField(Genre, blank=True)
    actors = models.ManyToManyField(Actor, blank=True)
    directors = models.ManyToManyField(Director, blank=True)


class Review(models.Model):
    content = models.TextField()
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


# # 별점 // 나중에 
# class Rating(models.Model):
#     id = models.IntegerField(primary_key=True)
#     movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
#     user = models.
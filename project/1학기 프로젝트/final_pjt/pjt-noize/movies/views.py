from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import *
from .serializers import *
from django.http import JsonResponse
from rest_framework.decorators import authentication_classes
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from django.db.models import Avg
from datetime import datetime


# Create your views here.
# 영화 관련
@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()[:10]
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)
    

@api_view(['GET'])
def find_movie(request, movie_name):
    print(movie_name)
    if request.method == 'GET':
        movies = Movie.objects.filter(title__icontains=movie_name)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)
    

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)

    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


@api_view(['GET'])
def movie_detail_actor(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    actors = Actor.objects.filter(id__in=movie.actors.all())
    if request.method == 'GET':
        serializer = ActorSerializer(actors, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def movie_detail_director(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    directors = Director.objects.filter(id__in=movie.directors.all())
    if request.method == 'GET':
        serializer = DirectorSerializer(directors, many=True)
        return Response(serializer.data)


# 리뷰 관련
@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
def review(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.method == 'GET':
        reviews = movie.review_set.all()
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ReviewListSerializer(data=request.data)
        # print('여기까지 오나?')
        # print(serializer)
        # print(request.user.pk)
        if serializer.is_valid(raise_exception=True):
            # print('여기까지 오나?222')
            serializer.save(movie=movie, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
def review_update_delete(request, movie_pk, review_pk):
    print('안녕!!!!!!!!!!!!!!!!!!!!!!!!')
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'PUT':
        review = get_object_or_404(Review, pk=review_pk, movie=movie)
        if review.user.pk == request.user.pk:
            serializer = ReviewListSerializer(review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)

    elif request.method == 'DELETE':
        review = get_object_or_404(Review, pk=review_pk, movie=movie)
        # 리뷰작성자와 로그인 유저가 같은지 확인
        if review.user.pk == request.user.pk:
            # print(review.user.pk)
            # print(request.user.pk)
            review.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
 #### 영화추천알고리즘 

# Json데이터의 popularity 기반으로 영화 추천
#


 # 1. 최신영화순서
@api_view(['GET'])
def latest_movie(request):
    print('안녕하세요 최신무비입니다.')
    today = datetime.now().date()

    # 오늘 이전에 개봉한 영화를 최신순으로 10개 가져옵니다.
    movies = Movie.objects.filter(release_date__lt=today).order_by('-release_date')[:10]

    # 가져온 영화 정보를 시리얼라이즈합니다.
    serialized_movies = []
    for movie in movies:
        # release_date를 문자열에서 datetime 객체로 변환합니다.
        movie.release_date = datetime.strptime(movie.release_date, "%Y-%m-%d").date()
        serialized_movies.append(movie)

    serializer = MovieListSerializer(serialized_movies, many=True)
    # print(serialized_movies)
    return Response(serializer.data)


# 1. 영화 인기도 순
@api_view(['GET'])
def popularity_recommend_movie(request):
    # 영화를 인기도(popularity) 기준으로 내림차순 정렬하여 가져옵니다.
    recommended_movies = Movie.objects.all().order_by('-popularity')[:16]

    # 가져온 영화 정보를 시리얼라이즈합니다.
    serializer = MovieListSerializer(recommended_movies, many=True)

    return JsonResponse(serializer.data, safe=False)

# 2. 배우 인기도 순
@api_view(['GET'])
def popular_actor(request):
    actors = Actor.objects.all().order_by('-popularity')[:100]
    serializer = ActorSerializer(actors, many=True)
    return JsonResponse(serializer.data, safe=False)


# 3. 감독 인기도 순
@api_view(['GET'])
def popular_director(request):
    pass



 # 4. 배우 인기도 평균 순서로 정렬한 영화 추천 
@api_view(['GET'])
def actor_population_movies(request):
    # 전체 영화 목록 가져오기
    movies = Movie.objects.all()

    # 모든 영화에 출연한 배우들의 인기도를 평균내서 정렬
    related_movies = (
        Movie.objects.annotate(average_actor_popularity=Avg('actors__popularity'))
        .order_by('-average_actor_popularity')[:16]
    )

    # 시리얼라이즈
    result_data = []
    for related_movie in related_movies:
        result_data.append({
            'id': related_movie.pk,
            'title': related_movie.title,
            'average_actor_popularity': related_movie.average_actor_popularity,
            'poster_path': related_movie.poster_path
        })

    return Response({'related_movies': result_data})


# 5. 감독 인기도 평균 순서로 정렬한 영화 추천
@api_view(['GET'])
def director_population_movies(request):
    # 전체 영화 목록 가져오기
    movies = Movie.objects.all()

    # 모든 영화에 제작진으로 참여한 감독들의 인기도를 평균내서 정렬
    related_movies = (
        Movie.objects.annotate(average_director_popularity=Avg('directors__popularity'))
        .order_by('-average_director_popularity')[:16]
    )

    # 시리얼라이즈
    result_data = []
    for related_movie in related_movies:
        result_data.append({
            'id': related_movie.pk,
            'title': related_movie.title,
            'average_director_popularity': related_movie.average_director_popularity,
            'poster_path': related_movie.poster_path
        })

    return Response({'related_movies': result_data})
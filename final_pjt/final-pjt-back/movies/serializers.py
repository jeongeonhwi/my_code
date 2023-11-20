from rest_framework import serializers
from .models import *

# 영화 리스트
class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


# 배우
class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'


# 감독
class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


# 영화 디테일페이지 
class MovieSerializer(serializers.ModelSerializer):

    actors = ActorSerializer(many=True, read_only=True)
    directors = DirectorSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'


# 배우가 출연한 영화 찾기용 
class ActorMovieSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = '__all__'


# 감독이 제작(?)한 영화 찾기용
class DrirectorMovieSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = Director
        fields = '__all__'


# 리뷰 시리얼라이즈
class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie', 'user')
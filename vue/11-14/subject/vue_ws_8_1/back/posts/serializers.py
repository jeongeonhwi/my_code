from rest_framework import serializers
from .models import Category, Post, Comment

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['pk', 'title', 'category']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
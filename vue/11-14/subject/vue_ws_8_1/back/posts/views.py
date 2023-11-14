from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostListSerializer, PostSerializer, CategorySerializer, CategoryListSerializer
from .models import Post, Category, Comment


# Create your views here.
@api_view(['GET', 'POST'])
def posts(request):
    if request.method == 'GET':
        post_list = Post.objects.all()
        serializer = PostListSerializer(post_list, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()


@api_view(['GET', 'POST'])
def category(request):
    if request.method == 'GET':
        category_list = Category.objects.all()
        serializer = CategoryListSerializer(category_list, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        # print(request.data)
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
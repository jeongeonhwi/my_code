from django.http import JsonResponse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.permissions import *
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.response import Response
from .models import User
from .serializers import UserInfoSerializer
from movies.models import *
from movies.serializers import *
from rest_framework.decorators import authentication_classes
from rest_framework.authentication import TokenAuthentication, BasicAuthentication


# Create your views here.
@api_view(['GET'])
def profile(request, user_pk):
    User = get_user_model()
    person = get_object_or_404(User, pk=user_pk)


@api_view(['GET'])
def check_user_id(request, user_name):
    print('체크유저 도착 !!!!!!!!!!!')
    user = User.objects.get(username=user_name)
    serializer = UserInfoSerializer(user)
    return Response(serializer.data)


@api_view(['GET'])
def user(request, user_id):
    print('유저 도착 !!!!!!!!!!!')
    user = User.objects.get(pk=user_id)
    serializer = UserInfoSerializer(user)
    return Response(serializer.data)


@api_view(['GET'])
def user_review(request, user_id):
    print('리뷰유저 도착 !!!!!!!!!!!')
    reviews = Review.objects.filter(user=user_id)
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
def user_like(request, user_id):
    print('라이크유저 도착 !!!!!!!!!!!')
    user = User.objects.get(pk=request.user.pk)
    print(user)
    person = User.objects.get(pk=user_id)
    print(person)
    if user_id != request.user.pk:
        if person in user.like.all():
            user.like.remove(person.pk)
        else:
            user.like.add(person.pk)
        # print(user.like)
        print('좋아요 추가완료')
    else:
        print('좋아요 추가실패')
    return Response()


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
def user_hate(request, user_id):
    print('라이크유저 도착 !!!!!!!!!!!')
    user = User.objects.get(pk=request.user.pk)
    person = User.objects.get(pk=user_id)
    if user_id != request.user.pk:
        if person in user.hate.all():
            user.hate.remove(person.pk)
        else:
            user.hate.add(person.pk)
        # print(user.hate)
        print('싫어요 추가완료')
    else:
        print('싫어요 추가실패')
    return Response()


@api_view(['GET'])
def all_user(request):
    print('올유저 도착!!')
    user = User.objects.all()
    serializer = UserInfoSerializer(user, many=True)
    return Response(serializer.data)
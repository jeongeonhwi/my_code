from django.http import JsonResponse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.permissions import *
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.response import Response


# Create your views here.
@api_view(['GET'])
def profile(request, user_pk):
    User = get_user_model()
    person = get_object_or_404(User, pk=user_pk)
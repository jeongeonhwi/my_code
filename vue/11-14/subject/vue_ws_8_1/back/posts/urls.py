from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.posts),
    path('category/', views.category),
]

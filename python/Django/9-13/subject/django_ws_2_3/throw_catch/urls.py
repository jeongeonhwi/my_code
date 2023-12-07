from django.urls import path
from . import views

app_name = 'throw_catch'
urlpatterns = [
    path('first/', views.first, name='throw_catch1'),
    path('second/', views.second, name='throw_catch2'),
]
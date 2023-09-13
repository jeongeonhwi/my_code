from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:user_id>/<int:article_pk>/', views.detail, name='detail'),
]

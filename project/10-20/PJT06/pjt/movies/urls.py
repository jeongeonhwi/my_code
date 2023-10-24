from django.urls import path
from . import views


app_name='movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('<int:movie_pk>/delete', views.delete, name='delete'),
    path('<int:movie_pk>/update/', views.update, name='update'),
    path('<int:movie_pk>/comments_create/', views.comment_create, name='comments_create'),
    path('<int:movie_pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name='comments_delete'),
    path('<int:movie_pk>/likes/', views.likes, name='likes'),
    path('<int:movie_pk>/<int:comment_pk>/recomment/', views.recomment, name='recomment'),
    path('<int:movie_pk>/recomments/<int:recomment_pk>/delete/', views.recomment_delete, name='recomments_delete'),
    path('<int:movie_pk>/<int:comment_pk>/comment_update/', views.comment_update, name='comment_update'),
]

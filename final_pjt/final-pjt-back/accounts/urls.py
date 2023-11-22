from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.all_user),
    path('<int:user_pk>/profile/', views.profile),
    path('<user_name>/check_user_id/', views.check_user_id),
    path('<int:user_id>/user/', views.user),
    path('<int:user_id>/user_review/', views.user_review),
    path('<int:user_id>/user_like/', views.user_like),
    path('<int:user_id>/user_hate/', views.user_hate),
    # path('<int:user_pk>/hate/', views.hate),
]
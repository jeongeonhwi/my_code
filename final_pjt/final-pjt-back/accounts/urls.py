from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('<int:user_pk>/profile/', views.profile),
    # path('<int:user_pk>/hate/', views.hate),
]
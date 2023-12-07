from django.urls import path
from . import views

app_name = 'calculators'
urlpatterns = [
    path('calculator/<int:one>/<int:two>/', views.calculators, name = 'calculators'),
]
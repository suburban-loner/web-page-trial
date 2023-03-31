from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('batman/', views.batman, name='batman'),
    path('joker/', views.joker, name='joker'),
    path('heroes/', views.heroes, name='heores'),
    path('villains/', views.villains, name='villains'),
]
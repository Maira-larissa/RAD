from django.urls import path
from . import views

urlpatterns = [
    path('welcome/', views.welcome, name="welcome"),
    path('eco/<str:palavra>', views.eco),
    path('info', views.info),
    path('nome/<str:nome>', views.nome),
    path('home', views.home, name="home"),
    path('contato/<str:numero>', views.contato, name="contato")
]
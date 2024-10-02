# Estas son las urls a utilizar para mi aplicación de productos

from django.urls import path
from producto import views

urlpatterns = [
   path('holamundo', views.hola_mundo),
   path('', views.inicio)
]
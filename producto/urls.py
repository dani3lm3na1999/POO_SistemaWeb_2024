# Estas son las urls a utilizar para mi aplicación de productos

from django.urls import path
from producto import views

urlpatterns = [
   path('', views.inicio, name="index"),
   path('productos/', views.ProductoListView.as_view(), name="productos"),
   path('productos/nuevo', views.ProductoCreateView.as_view(), name="producto_create"),
   path('productos/<int:pk>/editar', views.ProductoUpdateView.as_view(), name="producto_update")
]
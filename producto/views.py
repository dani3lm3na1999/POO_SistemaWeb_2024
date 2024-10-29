from django.shortcuts import render
# Importamos HttpResponse
from django.http import HttpResponse
# Importamos Productos
from .models import Productos

# Create your views here.
def hola_mundo(request):
    # Devolvemos un hola mundo a través de un encabezado h1
    return HttpResponse("<h1>Hola mundo desde mi aplicación web</h1><br><p>Esta es una prueba de párrafo</p>")

# Crear vista principal
def inicio(request):
    return render(request, 'base.html')

# Crear vista home
def listado_productos(request):

    productos = Productos.objects.all()
    return render(request, 'productos.html', {'productos': productos })

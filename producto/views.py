from django.shortcuts import render
# Importamos HttpResponse
from django.http import HttpResponse

# Create your views here.
def hola_mundo(request):
    # Devolvemos un hola mundo a través de un encabezado h1
    return HttpResponse("<h1>Hola mundo desde mi aplicación web</h1><br><p>Esta es una prueba de párrafo</p>")

# Crear vista principal
def inicio(request):
    return render(request, 'pages/index.html')

def productos(request):

    productos = []

    for i in range(5):
        producto = {
            "nombre": "Coca-Cola",
            "precio": 0.75,
            "cantidad": 24
        }
        productos.append(producto)

    # Diccionario es una colleción de clave, valor
    contexto = {
        "productos": productos,
        "usuario": "Francisco Peñate"
    }

    return render(request, 'pages/productos.html', contexto)

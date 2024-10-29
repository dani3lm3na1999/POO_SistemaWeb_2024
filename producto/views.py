from django.shortcuts import render
# Importamos HttpResponse
from django.http import HttpResponse
# Importar nuestro modelo
from .models import Productos
# Importar las vistas genéricas CRUD (Create, Read, Update, Delete)
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
# Importamos reverse_lazy desde Url
from django.urls import reverse_lazy
# Importamos nuestro formulario
from .forms import ProductosForm

usuario = "Francisco Daniel Peñate"

# Create your views here.
def hola_mundo(request):
    # Devolvemos un hola mundo a través de un encabezado h1
    return HttpResponse("<h1>Hola mundo desde mi aplicación web</h1><br><p>Esta es una prueba de párrafo</p>")

# Crear vista principal
def inicio(request):
    autenticado = False
    
    contexto = {
        "esta_autenticado": autenticado,
        "user": usuario
    }
    return render(request, 'pages/index.html', contexto)

# Crear vistas genéricas

# Crear una vista para el listado de productos
class ProductoListView(ListView):
    model = Productos
    template_name = "pages/producto_list.html"
    context_object_name = "productos"

# Crear una vista para guardar un producto
class ProductoCreateView(CreateView):
    model = Productos
    form_class = ProductosForm
    template_name = "pages/producto_form.html"
    success_url = reverse_lazy('productos')

# Crar una vista para actualizar un producto
class ProductoUpdateView(UpdateView):
    model = Productos
    form_class = ProductosForm
    template_name = "pages/producto_form.html"
    success_url = reverse_lazy('productos')

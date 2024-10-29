# importamos forms desde Django
from django import forms
from .models import Productos

class ProductosForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['Nombre', 'Descripcion', 'Precio', 'Cantidad', 'Estado']
        
    
    
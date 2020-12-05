from django.forms import (Select, ModelForm, CharField, TextInput, ValidationError)
from .models import Empleado, Area

class EmpleadoForm(ModelForm):
    class Meta:
        model = Empleado
        fields = ('nombre', 'apellido_paterno', 'apellido_materno', 'area')
        widgets = {
            'nombre': TextInput(attrs={'class':'form-control', 'placeholder': 'Escribe el nombre del empleado...'}),
            'apellido_paterno': TextInput(attrs={'class':'form-control'}),
            'apellido_materno': TextInput(attrs={'class':'form-control'}),
            'area':Select(attrs={'class':'form-control'})
        }

        
class AreaForm(ModelForm):
    class Meta:
        model = Area
        fields = ('nombre_area',)
        widgets = {
            'nombre_area': TextInput(attrs={'class':'form-control', 'placeholder': 'Escribe el nombre del área de trabajo...'})

        }
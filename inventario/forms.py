from django.forms import (Select, ModelForm, CharField,  DateInput, TextInput, IntegerField, ValidationError)
from .models import Productos, Partidas, Stock, Salida_productos

class ProductosForm(ModelForm):
    class Meta:
        model = Productos
        fields = ('nombre','marca','precio','giro','unidad','presentacion','partida')
        widgets = {
            'nombre': TextInput(attrs={'class':'form-control'}),
            'marca': TextInput(attrs={'class':'form-control'}),
            'precio': TextInput(attrs={'class':'form-control'}),
            'giro': TextInput(attrs={'class':'form-control'}),
            'unidad': TextInput(attrs={'class':'form-control'}),
            'presentacion': TextInput(attrs={'class':'form-control'}),
            'partida': Select(attrs={'class':'form-control'}), 
        }

class PartidasForm(ModelForm):
    class Meta:
        model = Partidas
        fields = ('numero_partida','nombre_partida','descripcion')
        widgets = {
            'numero_partida': TextInput(attrs={'class':'form-control'}),
            'nombre_partida': TextInput(attrs={'class':'form-control'}),
            'descripcion': TextInput(attrs={'class':'form-control'}),
        }

class StockForm(ModelForm):
    class Meta:
        model = Stock
        fields = ('no_factura','fecha','producto','cantidad')
        widgets = {
            'no_factura': TextInput(attrs={'class':'form-control'}),
            'fecha': DateInput(attrs={'class':'datepicker'}),
            'producto': Select(attrs={'class':'form-control'}),
            'cantidad': TextInput(attrs={'class':'form-control'}),
        }

class Salida_productosForm(ModelForm):
    class Meta:
        model = Salida_productos
        fields = ('empleado', 'fecha', 'producto_stock', 'cantidad')
        widgets = {
            'empleado': Select(attrs={'class':'form-control'}),
            'fecha': DateInput(attrs={'class':'datepicker'}),
            'producto_stock': Select(attrs={'class':'form-control'}),
            'cantidad': TextInput(attrs={'class':'form-control'}),       
        }


        




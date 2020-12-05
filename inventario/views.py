from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from .models import Productos, Partidas, Stock, Salida_productos
from django.views.generic.list import ListView
from .forms import PartidasForm, ProductosForm, StockForm, Salida_productosForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin


#Partidas
class Partidas_lista(ListView):
    model = Partidas
    template_name = 'lista_partidas.html'

class Nueva_Partida(CreateView):
    template_name = 'partida_form.html'
    model = Partidas
    form_class = PartidasForm
    success_url = reverse_lazy('inventario:Partidas_lista')
    
#Aqui se pone la funcionalidad de eliminar una partida del registro.
class Eliminar_Partida(DeleteView):
    model = Partidas
    success_url = reverse_lazy('inventario:Partidas_lista')
    template_name = 'partida_confirm_delete.html'

#En esta parte se implementa la parte para editar una partida.
class Editar_partida(SuccessMessageMixin, UpdateView):
    model = Partidas
    form_class = PartidasForm
    extra_context = {'editar':True}
    template_name = 'partida_form.html'
    success_url = reverse_lazy('inventario:Partidas_lista')

#Productos
class Lista_Productos(ListView):
    model = Productos
    template_name = 'lista_productos.html'

class Nuevo_Producto(CreateView):
    template_name = 'producto_form.html'
    model = Productos
    form_class = ProductosForm
    success_url = reverse_lazy('inventario:ListaProductos')

class Eliminar_Producto(DeleteView):
    model = Productos
    success_url = reverse_lazy('inventario:ListaProductos')
    template_name = 'partida_confirm_delete.html'  


class Editar_Producto(SuccessMessageMixin, UpdateView):
    model = Productos
    form_class = ProductosForm
    extra_context = {'editar':True}
    template_name = 'producto_form.html'
    success_url = reverse_lazy('inventario:ListaProductos')


#Inventario
class Inventario_lista(ListView):
    model = Stock
    template_name = 'lista_inventario.html'

class Añadir_inventario(SuccessMessageMixin, CreateView):
    model = Stock
    template_name = 'stock_form.html'
    form_class = StockForm
    success_url = reverse_lazy('inventario:inventarioLista')
    success_message = "Se agregó con éxito el producto al inventario"

    
    
class Sacar_inventario(CreateView):
    template_name = 'salida_productos_form.html'
    model = Salida_productos
    form_class = Salida_productosForm







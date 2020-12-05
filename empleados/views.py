from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Empleado, Area
from .forms import  EmpleadoForm, AreaForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .forms import  EmpleadoForm
from django.urls import reverse_lazy

#Clase para listar los empleados.
class Lista_Empelados(ListView):
    model = Empleado
    template_name = 'lista_de_empleados.html'

#Esta clase implementa la funcionalidad para añadir un nuevo empleado.
class Nuevo_empleado(CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleado_form.html'
    success_url = reverse_lazy('empleados:listaEmpleados')

#En esta parte se implementa la parte para editar un empleado.
class Editar_empleado(SuccessMessageMixin, UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    extra_context = {'editar':True}
    template_name = 'empleado_form.html'
    success_url = reverse_lazy('empleados:listaEmpleados')


#Aqui se pone la funcionalidad de eliminar un empleado del registro.
class Eliminar_empleado(DeleteView):
    model = Empleado
    success_url = reverse_lazy('empleados:listaEmpleados')
    template_name = 'empleado_confirm_delete.html'


#En esta parte se listan las areas de trabajo de los empleados.
class Lista_Areas(ListView):
    model = Area
    template_name = 'lista_de_areas.html'

#Esta clase implementa la funcionalidad para añadir un nuevo empleado.
class Nueva_area(CreateView):
    model = Area
    form_class = AreaForm
    template_name = 'areas_form.html'
    success_url = reverse_lazy('empleados:listaAreas')

#En esta parte se implementa la parte para editar un empleado.
class Editar_area(SuccessMessageMixin, UpdateView):
    model = Area
    form_class = AreaForm
    extra_context = {'editar':True}
    template_name = 'areas_form.html'
    success_url = reverse_lazy('empleados:listaAreas')
    

#Aqui se pone la funcionalidad de eliminar una area del registro.
class Eliminar_area(DeleteView):
    model = Area
    success_url = reverse_lazy('empleados:listaAreas')
    template_name = 'area_confirm_delete.html'

    
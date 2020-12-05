from django.urls import path
from .views import (Nuevo_empleado, Lista_Empelados, Lista_Areas, Eliminar_empleado, Editar_empleado, Nueva_area, Eliminar_area, Editar_area)
from .views import (Nuevo_empleado, Lista_Empelados, Lista_Areas, Editar_empleado, Eliminar_empleado)

app_name = 'empleados'

urlpatterns = [

    path('lista_empleados/', Lista_Empelados.as_view(), name='listaEmpleados'),
    path('lista_areas/', Lista_Areas.as_view(), name='listaAreas'),
    
    path('nuevo_empleado/', Nuevo_empleado.as_view(), name='nuevoEmpleado'),
    path('editar_empleado/<int:pk>', Editar_empleado.as_view(), name='editarEmpleado'),
    path('eliminar_empleado/<int:pk>', Eliminar_empleado.as_view(), name='eliminarEmpleado'),
    
    path('nueva_area/', Nueva_area.as_view(), name='nuevoArea'),
    path('editar_area/<int:pk>', Editar_area.as_view(), name='editarArea'),
    path('eliminar_area/<int:pk>', Eliminar_area.as_view(), name='eliminarArea'),

]

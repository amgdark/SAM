from django.urls import path
from .views import Lista_Productos, Productos, Partidas_lista, Nueva_Partida, Eliminar_Partida, Editar_partida, Nuevo_Producto, Eliminar_Producto, Editar_Producto
from .views import Inventario_lista, Añadir_inventario, Sacar_inventario

app_name = 'inventario'

app_name = 'inventario'

urlpatterns = [    
    #Productos
    path('lista_productos/', Lista_Productos.as_view(), name='ListaProductos'),
    path('nuevoProducto/', Nuevo_Producto.as_view(), name='NuevoProducto'),
    path('eliminar_producto/<int:pk>', Eliminar_Producto.as_view(), name='EliminarProducto'),
    path('editar_producto/<int:pk>', Editar_Producto.as_view(), name='EditarProducto'),  




    #Partidas
    path('lista_partida/', Partidas_lista.as_view(), name='Partidas_lista'),
    path('nuevaPartida/', Nueva_Partida.as_view(), name='NuevaPartida'),
    path('eliminar_partida/<int:pk>', Eliminar_Partida.as_view(), name='eliminacionDePartida'),
    path('editar_partida/<int:pk>', Editar_partida.as_view(), name='editarPartida'),



    #Inventario
    path('inventario_lista/', Inventario_lista.as_view(), name='inventarioLista'),
    path('añadir_inventario/', Añadir_inventario.as_view(), name='Añadir_Inventario'),
    path('inventario_salida/', Sacar_inventario.as_view(), name='Salida_Inventario'),
    

    



]

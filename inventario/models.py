from django.db import models
from django.contrib.auth.models import User
from empleados.models import Empleado

class Partidas(models.Model):
    numero_partida = models.IntegerField("Numero de partida", primary_key=True)
    nombre_partida = models.CharField("Nombre de partida", max_length=200)
    descripcion = models.CharField("Descripcion", max_length=700)

    def __str__(self):
        return str(self.numero_partida)
        
    

class Productos(models.Model):
    nombre = models.CharField("Nombre del producto", max_length=200)
    marca = models.CharField("Marca del producto", max_length=100)
    precio = models.DecimalField("Precio", max_digits=8, decimal_places=2)
    giro = models.CharField("Giro", max_length=100)
    unidad = models.CharField("Unidad", max_length=50)
    presentacion = models.CharField("Presentación", max_length=100)
    partida = models.ForeignKey(Partidas, verbose_name="Partida", on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Stock(models.Model):
    no_factura = models.CharField("Número de factura", max_length=50)
    fecha = models.DateField("Fecha de registro")
    producto = models.ForeignKey(Productos, verbose_name="Producto", on_delete=models.CASCADE)
    cantidad = models.IntegerField("Cantidad en stock")

class Salida_productos(models.Model):
    empleado = models.ForeignKey(Empleado, verbose_name="Nombre de empleado", on_delete=models.CASCADE)
    fecha = models.DateField(verbose_name="Fecha de solicitud")
    producto_stock = models.ForeignKey(Stock, verbose_name="Producto", on_delete=models.CASCADE)
    cantidad = models.IntegerField("Cantidad")
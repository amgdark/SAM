from django.db import models

class Area(models.Model):
    nombre_area = models.CharField("Nombre del área", max_length=150)
    
    def __str__(self):
        return self.nombre_area

class Empleado(models.Model):
    nombre = models.CharField("Nombre del empleado", max_length=50)
    apellido_paterno = models.CharField("Apellido paterno", max_length=50)
    apellido_materno = models.CharField("Apellido materno", max_length=50, null=True, blank=True)
    area = models.ForeignKey(Area, verbose_name="Area de trabajo", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre +" "+ self.apellido_paterno

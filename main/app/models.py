from django.db import models
from django.db.models.base import Model

# Create your models here.


#clase marca
class Marca(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre



class Producto(models.Model):
    nombre = models.CharField(max_length=120)
    precio = models.IntegerField()
    descripcion = models.TextField()
    disponible = models.BooleanField()
    marca = models.ForeignKey(Marca,on_delete=models.PROTECT)
    fecha_creada = models.DateField()
    imagen = models.ImageField(upload_to ="productos",null = True)

    def __str__(self):
        return self.nombre






opciones_consultas = [
    [0,"consulta"],
    [1,"reclamo"],
    [2,"sugerencia"],
    [3,"felicidades"]

]

class Contacto(models.Model):
    nombre = models.CharField(max_length=120)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre
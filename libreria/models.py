from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Tatuaje(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    fecha_fabricacion = models.DateField()
    imagen = models.ImageField(upload_to="tatuajes", null=True)
    principal = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

class Diseno(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    fecha_fabricacion = models.DateField()
    imagen = models.ImageField(upload_to="diseños", null=True)
    principal = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

opciones_consultas = [
    [0, "consulta"],
    [1, "reclamo"],
    [2, "sugerencia"],
    [3, "felicitacions"]
]


class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre
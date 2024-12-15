from django.db import models
from django.contrib.auth.models import User

class Discoteca(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    capacidad = models.PositiveIntegerField(blank=True, null=True)
    horario_apertura = models.TimeField(blank=True, null=True)
    horario_cierre = models.TimeField(blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    es_activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Calificacion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    discoteca = models.ForeignKey(Discoteca, related_name='calificaciones', on_delete=models.CASCADE)
    puntaje = models.IntegerField()
    comentario = models.TextField(blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} -> {self.discoteca.nombre}: {self.puntaje}"

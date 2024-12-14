from django.db import models

class Discoteca(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200, blank=True, null=True)  # Campo opcional
    capacidad = models.PositiveIntegerField(blank=True, null=True)  # Campo opcional
    horario_apertura = models.TimeField(blank=True, null=True)  # Campo opcional
    horario_cierre = models.TimeField(blank=True, null=True)  # Campo opcional
    telefono = models.CharField(max_length=20, blank=True, null=True)  # Campo opcional
    email = models.EmailField(blank=True, null=True)  # Campo opcional
    descripcion = models.TextField(blank=True, null=True)  # Campo opcional
    es_activo = models.BooleanField(default=True)  # Este campo no necesita ser opcional

    def __str__(self):
        return self.nombre

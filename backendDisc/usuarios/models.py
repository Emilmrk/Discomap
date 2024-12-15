from django.contrib.auth.models import User
from django.db import models

class Favorito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    discoteca = models.ForeignKey('discoteca.Discoteca', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.usuario.username} -> {self.discoteca.nombre} (Favorito)"

class Reciente(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    discoteca = models.ForeignKey('discoteca.Discoteca', on_delete=models.CASCADE)
    visto_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} -> {self.discoteca.nombre} (Visto en: {self.visto_en})"

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    biografia = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.usuario.username}"

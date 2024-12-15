from django.contrib import admin
from .models import Favorito, Reciente, Perfil

@admin.register(Favorito)
class FavoritoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'discoteca')

@admin.register(Reciente)
class RecienteAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'discoteca', 'visto_en')

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'avatar', 'biografia')

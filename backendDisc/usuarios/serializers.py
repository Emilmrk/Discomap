from rest_framework import serializers
from .models import Favorito, Reciente, Perfil

class FavoritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorito
        fields = '__all__'

class RecienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reciente
        fields = '__all__'

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = '__all__'

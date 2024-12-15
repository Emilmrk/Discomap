from rest_framework import serializers
from .models import Discoteca, Calificacion

class DiscotecaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discoteca
        fields = '__all__'

class CalificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calificacion
        fields = '__all__'

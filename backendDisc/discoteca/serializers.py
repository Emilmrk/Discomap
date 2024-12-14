from rest_framework import serializers
from .models import Discoteca

class DiscotecaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discoteca
        fields = '__all__'

from rest_framework import generics
from .models import Discoteca, Calificacion
from .serializers import DiscotecaSerializer, CalificacionSerializer

# Vista para listar y crear Discotecas
class DiscotecaList(generics.ListCreateAPIView):
    queryset = Discoteca.objects.all()
    serializer_class = DiscotecaSerializer

# Vista para obtener, actualizar y eliminar una Discoteca específica
class DiscotecaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Discoteca.objects.all()
    serializer_class = DiscotecaSerializer

# Vista para listar y crear Calificaciones
class CalificacionList(generics.ListCreateAPIView):
    queryset = Calificacion.objects.all()
    serializer_class = CalificacionSerializer

# Vista para obtener, actualizar y eliminar una Calificación específica
class CalificacionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Calificacion.objects.all()
    serializer_class = CalificacionSerializer

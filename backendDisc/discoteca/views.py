from rest_framework import generics
from .models import Discoteca
from .serializers import DiscotecaSerializer

class DiscotecaList(generics.ListCreateAPIView):
    queryset = Discoteca.objects.all()
    serializer_class = DiscotecaSerializer

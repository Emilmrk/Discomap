import json
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from .models import Favorito, Reciente, Perfil  # Asegúrate de importar los modelos
from .serializers import FavoritoSerializer, RecienteSerializer, PerfilSerializer  # Importar los serializadores

@csrf_exempt
def login_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode('utf-8'))
            username = data.get('username')
            password = data.get('password')
            print('Datos recibidos para login:', username, password)  # Añadir este print

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                token, created = Token.objects.get_or_create(user=user)
                return JsonResponse({"token": token.key})
            else:
                return JsonResponse({"error": "Invalid credentials"}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

@csrf_exempt
def register_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode('utf-8'))
            username = data.get('username')
            password = data.get('password')
            print('Datos recibidos para registro:', username, password)  # Añadir este print

            if not username or not password:
                return JsonResponse({"error": "Username and password are required"}, status=400)
            if User.objects.filter(username=username).exists():
                return JsonResponse({"error": "Username already exists"}, status=400)

            user = User.objects.create_user(username=username, password=password)
            user.save()
            # Perfil.objects.create(user=user)  # Puedes descomentar esto si usas un modelo Perfil
            token, created = Token.objects.get_or_create(user=user)
            return JsonResponse({"token": token.key}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        except Exception as e:
            print(f"Error al registrar usuario: {e}")
            return JsonResponse({"error": str(e)}, status=500)

# Definir los conjuntos de vistas para Favorito, Reciente y Perfil

class FavoritoViewSet(viewsets.ModelViewSet):
    queryset = Favorito.objects.all()
    serializer_class = FavoritoSerializer

class RecienteViewSet(viewsets.ModelViewSet):
    queryset = Reciente.objects.all()
    serializer_class = RecienteSerializer

class PerfilViewSet(viewsets.ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer

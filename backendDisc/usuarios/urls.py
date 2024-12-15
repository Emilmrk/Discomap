from django.urls import path, include
from .views import login_view, register_view
from rest_framework.routers import DefaultRouter
from .views import FavoritoViewSet, RecienteViewSet, PerfilViewSet

# Configurar enrutador para las vistas de conjuntos de vistas
router = DefaultRouter()
router.register(r'favoritos', FavoritoViewSet)
router.register(r'recientes', RecienteViewSet)
router.register(r'perfiles', PerfilViewSet)

# Incluir las rutas del enrutador junto con las rutas de autenticación
urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),  # Añadir esta línea
    path('', include(router.urls)),  # Incluir las rutas del enrutador
]

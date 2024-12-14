from django.urls import path
from .views import login_view, register_view  # Asegúrate de importar la vista de registro

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),  # Añadir esta línea
]

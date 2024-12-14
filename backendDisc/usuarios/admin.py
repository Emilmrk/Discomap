from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser  # Importa tu modelo personalizado

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # Puedes personalizar la configuración del admin aquí si es necesario
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

from django.urls import path
from .views import DiscotecaList

urlpatterns = [
    path('discotecas/', DiscotecaList.as_view(), name='discoteca-list'),
]

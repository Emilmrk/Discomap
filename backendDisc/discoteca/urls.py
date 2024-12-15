from django.urls import path
from .views import DiscotecaList, DiscotecaDetail, CalificacionList, CalificacionDetail

urlpatterns = [
    path('discotecas/', DiscotecaList.as_view(), name='discoteca-list'),
    path('discotecas/<int:pk>/', DiscotecaDetail.as_view(), name='discoteca-detail'),
    path('calificaciones/', CalificacionList.as_view(), name='calificacion-list'),
    path('calificaciones/<int:pk>/', CalificacionDetail.as_view(), name='calificacion-detail'),
]

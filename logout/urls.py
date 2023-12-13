from django.urls import path
from .views import cerrar_sesion

urlpatterns = [
    path('cerrar/', cerrar_sesion, name='logout'),
]

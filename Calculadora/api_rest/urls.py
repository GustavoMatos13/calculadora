from django.urls import path

from .views import ProtectedView

urlpatterns = [
    path('calcular/<str:operador>/<str:numero_um>/<str:numero_dois>/', ProtectedView.get, name='calcular'),
 
]

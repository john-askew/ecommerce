from django.urls import path, include
from .views import tienda

urlpatterns = [
    path('tienda/', tienda, name = 'tienda'),
    ]

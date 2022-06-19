from django.shortcuts import render
from django.contrib import admin
from django.urls import path, include
from ClientesApp.views import CrearCliente, ListarClientes, DetalleCliente, EliminarCliente, UpdateCliente
from django.conf import settings
from django.conf.urls.static import static
from tay.settings import MEDIA_ROOT, MEDIA_URL


urlpatterns = [
    path('clientes/', ListarClientes.as_view(), name = "clientes"),
    path('crear_cliente/', CrearCliente.as_view(), name = "crear_cliente"),
    path('detalle_cliente/<int:pk>/', DetalleCliente.as_view(), name = "detalle_cliente"),
    path('update_cliente/<int:pk>/', UpdateCliente.as_view(), name = "update_cliente"),
    path('eliminar_cliente/<int:pk>/', EliminarCliente.as_view(), name = "eliminar_cliente"),
    
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

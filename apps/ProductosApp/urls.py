from django.shortcuts import render
from django.contrib import admin
from django.urls import path, include
from apps.ProductosApp.views import CrearProducto, ListarProductos, DetalleProducto, EliminarProducto, UpdateProducto 
from django.conf import settings
from django.conf.urls.static import static
from tay.settings import MEDIA_ROOT, MEDIA_URL



urlpatterns = [
    path('productos/', ListarProductos.as_view(), name = "productos"),
    path('crear_productos/', CrearProducto.as_view(), name = "crear_productos"),
    path('detalle_producto/<int:pk>/', DetalleProducto.as_view(), name = "detalle_producto"),
    path('update_producto/<int:pk>/', UpdateProducto.as_view(), name = "update_producto"),
    path('eliminar_producto/<int:pk>/', EliminarProducto.as_view(), name = "eliminar_producto"),
    
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

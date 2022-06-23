from django.shortcuts import render, redirect
from apps.ProductosApp.models import Producto
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from .forms import ProductoForm
from django.http import	request

# Create your views here.

class ListarProductos(ListView):
    model = Producto
    template_name= 'templates_productos/productos.html'
    context_object_name = 'productos'

class DetalleProducto(DetailView):
    model = Producto
    template_name= 'templates_productos/detalle_producto.html'

class CrearProducto(LoginRequiredMixin, CreateView):
    model = Producto
    template_name = 'templates_productos/crear_producto.html'
    fields = '__all__'

    def get_success_url(self):
        return render(request, f'templates_productos/detalle_producto/{self.object.pk}')

class EliminarProducto(DeleteView):
    model = Producto
    template_name = 'templates_productos/eliminar_producto.html'

    def get_success_url(self):
        return reverse('productos')

class UpdateProducto(UpdateView):
    model = Producto
    template_name = 'templates_productos/update_producto.html'
    fields = ['nombre', 'precio', 'categoria', 'stock', 'descripcion']

    def get_success_url(self):
        return reverse('detalle_producto', kwargs = {'pk':self.object.pk})

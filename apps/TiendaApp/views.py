from django.shortcuts import render, redirect
from apps.ProductosApp.models import Producto
from apps.TiendaApp.carro import Carro


def tienda(request):

    productos = Producto.objects.all()

    return render(request, 'templates_tienda/tienda.html', {'productos': productos})

def agregar_producto(request, producto_id):

    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.agregar(producto=producto)
    redirect ('tienda')

def eliminar_producto(request, producto_id):

    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    redirect ('tienda')

def disminuir_producto(request, producto_id):

    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.disminuir(producto=producto)
    redirect ('tienda')

def disminuir_producto(request, producto_id):

    carro = Carro(request)
    carro.limpiar()
    redirect ('tienda')
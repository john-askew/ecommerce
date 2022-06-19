from django.contrib import admin
from ClientesApp.models import Cliente
from ProductosApp.models import Producto

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Producto)
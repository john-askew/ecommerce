from django.contrib import admin
from apps.ProductosApp.models import Producto, ImagenProducto, CategoriaProducto



class CategoriaProductoAdmin(admin.ModelAdmin):

    readonly_fields = ('fecha_alta', 'fecha_modificacion')

class ProductoAdmin(admin.ModelAdmin):

    readonly_fields = ('fecha_alta', 'fecha_modificacion')

class ImagenProductoAdmin(admin.ModelAdmin):

    readonly_fields = ('fecha_alta',)

admin.site.register(Producto, ProductoAdmin)
admin.site.register(ImagenProducto, ImagenProductoAdmin)
admin.site.register(CategoriaProducto, ProductoAdmin)

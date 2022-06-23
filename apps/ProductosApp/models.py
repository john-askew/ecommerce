from tabnanny import verbose
from django.db import models

class CategoriaProducto(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_alta = models.DateField(auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Categoria de Producto'
        verbose_name_plural = 'Categorias de Productos'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField('Nombre', max_length=100)
    precio = models.DecimalField('Precio',max_digits=6, decimal_places=2)
    categoria = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE, default=1)
    stock = models.IntegerField('Stock', default=0)
    descripcion = models.TextField('Descripcion', max_length=500, blank=True, null=True)
    activo = models.BooleanField('Activo', default=True)
    fecha_alta = models.DateField(auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.nombre    

class ImagenProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='imagenes')
    imagen = models.ImageField('Imagen', upload_to='imagenes_productos', null=True, blank=True)
    fecha_alta = models.DateField('Fecha de Alta', auto_now_add=True)

    def __str__(self) -> str:
        return (f'Imagen de {self.producto}')
    
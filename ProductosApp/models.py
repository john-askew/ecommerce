from django.db import models


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField()
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='imagenes_productos', null=True, blank=True)

    def __str__(self):
        return self.nombre    

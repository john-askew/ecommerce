from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.

class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField('Apellido',max_length=100, blank = False, null = False)
    email = models.EmailField('Email', max_length=100, blank = False, null = False)
    telefono = models.CharField('Telefono', max_length=100, blank = False, null = False)
    direccion = models.CharField('Direccion',max_length=100, blank = False, null = False)
    ciudad = models.CharField('Ciudad', max_length=100, blank = False, null = False)
    estado = models.CharField('Estado', max_length=100, blank = False, null = False)
    pais = models.CharField('Pais', max_length=100, blank = False, null = False)
    cp = models.IntegerField('Codigo Postal', blank = False, null = False)
    fecha_registro = models.DateField('Fecha de Registro', auto_now_add=True)
    validado = models.BooleanField('Validado', default=False)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['apellido']

    def __str__(self):
        return self.nombre + ' ' + self.apellido


class ImagenCliente(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='imagenes')
    imagen = models.ImageField('Imagen Documento', upload_to='media_clientes', null=True, blank=True)
    fecha_alta = models.DateField('Fecha de Alta', auto_now_add=True)

    class Meta:
        verbose_name = 'Imagen Cliente'
        verbose_name_plural = 'Imagenes Clientes'
        ordering = ['cliente']

    def __str__(self) -> str:
        return self.cliente


class FAQs(models.Model):
    pregunta = models.CharField('Pregunta', max_length=200, blank=False, null=False)
    respuesta = models.TextField('Respuesta', blank=False, null=False)

    def __str__(self) -> str:
        return self.pregunta

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'


    
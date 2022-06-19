from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    nick = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    apellido = models.CharField('Apellido',max_length=100, blank = False, null = False)
    email = models.EmailField('E-Mail', max_length=100, blank = False, null = False)
    telefono = models.CharField('Telefono', max_length=100, blank = False, null = False)
    direccion = models.CharField('Direccion',max_length=100, blank = False, null = False)
    ciudad = models.CharField('Ciudad', max_length=100, blank = False, null = False)
    estado = models.CharField('Estado', max_length=100, blank = False, null = False)
    pais = models.CharField('Pais', max_length=100, blank = False, null = False)
    cp = models.IntegerField('Codigo Postal', blank = False, null = False)
    imagen_documento = models.ImageField('Foto Documento frente', upload_to='media_clientes', null=True, blank=True)
    fecha_registro = models.DateField('Fecha de Registro', auto_now = True, auto_now_add=False)
    validado = models.BooleanField('Validado', default=False)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['apellido']

    def __str__(self):
        return self.nombre + ' ' + self.apellido

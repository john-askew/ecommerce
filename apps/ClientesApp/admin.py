from django.contrib import admin
from apps.ClientesApp.models import Cliente, ImagenCliente, FAQs

# Register your models here.

admin.site.register(Cliente)
admin.site.register(ImagenCliente)
admin.site.register(FAQs)
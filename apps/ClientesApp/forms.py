from django import forms
from apps.ClientesApp.models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre',
         'apellido',
         'direccion',
         'telefono', 
         'email', 
         'direccion', 
         'ciudad', 
         'estado', 
         'pais', 
         'cp',
        ]


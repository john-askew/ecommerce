import re
from urllib import request
from django.shortcuts import render, redirect
from apps.ClientesApp.models import Cliente
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from apps.ClientesApp.models import FAQs


class ListarClientes(ListView):
    model = Cliente
    template_name= 'templates_clientes/clientes.html'
    context_object_name = 'clientes'

class DetalleCliente(DetailView):
    model = Cliente
    template_name= 'templates_clientes/detalle_cliente.html'

class CrearCliente(LoginRequiredMixin, CreateView):
    model = Cliente
    template_name = 'templates_clientes/crear_cliente.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detalle_cliente', kwargs={'pk': self.object.id})

class EliminarCliente(LoginRequiredMixin, DeleteView):
    model = Cliente
    template_name = 'templates_clientes/eliminar_cliente.html'

    def get_success_url(self):
        return reverse('clientes')

class UpdateCliente(LoginRequiredMixin, UpdateView):
    model = Cliente
    template_name = 'templates_clientes/update_cliente.html'
    fields = '__all__'


    def get_success_url(self):
        return reverse('detalle_cliente', kwargs = {'pk':self.object.pk})


def ListFAQs(request):
     faqs = FAQs.objects.all()
     context = {'faqs': faqs}
     return render(request, 'base.html', context=context)
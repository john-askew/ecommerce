from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from tay.forms import UserRegisterForm
from ProductosApp.models import Producto


def login_view(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username, password = password)
            
            if user is not None:
                login(request, user)
                context = {"mensaje": "Bienvenido {}".format(username)}
                return render(request, 'index.html', context=context)
            else:
                context = {"mensaje": "Usuario o contraseña incorrectos"}
                form = AuthenticationForm()
                return render(request, 'auth/login.html', context=context)
        else:
            errors = form.errors
            form = AuthenticationForm()
            context = {"mensaje": errors, "form": form}
            return render(request, 'auth/login.html', context=context)
    else:
        form = AuthenticationForm()
        context = {'form': form}
        return render(request, 'auth/login.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('index')


def register_view(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            context = {"mensaje": "Bienvenido {}".format(username)}
            return render(request, 'index.html', context=context)
        else:
            errors = form.errors
            form = UserRegisterForm()
            context = {"mensaje": errors, "form": form}
            return render(request, 'auth/register.html', context=context)
    else:   
        form = UserRegisterForm()
        context = {'form': form}
        return render(request, 'auth/register.html', context=context)


def index(request):
    return render(request, 'index.html')


def buscar(request):
    try:
        producto = Producto.objects.get(nombre__icontains= request.GET['search'])
        context = {'producto': producto}
        return render(request, 'buscar.html', context = context)
    except:
        context = {'errors':'No se encontro el producto'}
        return render(request, 'buscar.html', context = context)
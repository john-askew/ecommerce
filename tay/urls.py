from django.shortcuts import render
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from tay.views import login_view, index, logout_view, register_view, buscar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name = "index"),
    path('login/', login_view, name = "login"),
    path('logout/', logout_view, name = "logout"),
    path('register/', register_view, name = "register"),
    path('buscar/', buscar, name = "buscar"),
    path('productos/', include('apps.ProductosApp.urls')),
    path('clientes/', include('apps.ClientesApp.urls')),
    path('tienda/', include('apps.TiendaApp.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


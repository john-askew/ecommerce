from django.shortcuts import render
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from tay.views import login_view, index, logout_view, register_view, buscar
from .settings import MEDIA_ROOT, MEDIA_URL


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name = "index"),
    path('login/', login_view, name = "login"),
    path('logout/', logout_view, name = "logout"),
    path('register/', register_view, name = "register"),
    path('buscar/', buscar, name = "buscar"),
    path('productos/', include('ProductosApp.urls')),
    path('clientes/', include('ClientesApp.urls')),

]#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

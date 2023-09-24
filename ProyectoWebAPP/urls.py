
from django.contrib import admin
from django.urls import path

from ProyectoWebAPP.views import *

urlpatterns = [
    path('', home, name='Home'),   
    path('servicios', servicios ,name='Servicios'), 
    path('tienda', tienda ,name='Tienda'), 
    path('blog', blog ,name='Blog'), 
    path('contacto', contacto ,name='Contacto'),
]
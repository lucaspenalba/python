from django.contrib import admin
from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('familiares/', familiar, name="familiar"),
    path('', inicio, name="inicio"),
    path('clientes/', inicio, name="clientes"),
    path('inventario/', inventario, name="inventario"),
    path('empleados/', empleados, name="empleados"),
    path('clienteFormulario/', clienteFormulario, name="clienteFormulario"),

]
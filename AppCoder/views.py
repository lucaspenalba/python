from django.shortcuts import render
from .models import Cliente, Empleado, Inventario
from django.http import HttpResponse
from django.template import Template, loader
from django.db.models import Q

from AppCoder.forms import ClienteForm, EmpleadoForm, InventarioForm
# Create your views here.

    
def inicio(request):
    return render (request, "AppCoder/inicio.html")

def clientes(request):
    return render (request, "AppCoder/clientes.html")

def empleados(request):
    if request.method=="POST":
        form=EmpleadoForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data 
            nom=info["nombre"]
            ape=info["apellido"]
            correo=info["mail"]

            empleado=Empleado(nombre=nom, apellido=ape, mail=correo)
            empleado.save()
            return render (request, "AppCoder/inicio.html", {"mensaje":"Ingresado Correctamente"})
    else:
        formulario=EmpleadoForm()

    return render (request, "AppCoder/empleados.html", {"form":formulario})   

def inventario(request):
    if request.method=="POST":
        form=InventarioForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data 
            ser=info["serie"]
            nom=info["nombre"]
            des=info["descripcion"]
            can=info["cantidad"]
            pre=info["precio"]

            inventario=Inventario(serie=ser, nombre=nom, descripcion=des, cantidad=can, precio=pre)
            inventario.save()
            return render (request, "AppCoder/inicio.html", {"mensaje":"Ingresado Correctamente"})
    else:
        formulario=InventarioForm()

    return render (request, "AppCoder/inventario.html", {"form":formulario})   



def clienteFormulario(request):
    if request.method=="POST":
        form=ClienteForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data 
            nom=info["nombre"]
            ape=info["apellido"]
            mail=info["correo"]

            cliente=Cliente(nombre=nom, apellido=ape, correo=mail)
            cliente.save()
            return render (request, "AppCoder/inicio.html")
    else:
        formulario=ClienteForm()

    return render (request, "AppCoder/clienteFormulario.html", {"form":formulario})    

def busquedaProducto(request):
    return render(request, "AppCoder/busquedaProducto.html")       

def buscar(request):
    if 'search' in request.GET:
        search = request.GET['search']
        data=Inventario.objects.filter(nombre__icontains=search)
        return render(request,"Appcoder/resultadoBusqueda.html", {"data":data} )
    else:
        return render(request, "Appcoder/busquedaProducto.html", {"mensaje":"Ingresa un nombre "})
  
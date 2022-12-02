from django.shortcuts import render
from .models import Cliente, Empleado, Inventario
from django.http import HttpResponse
from django.template import Template, loader

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
    if request.GET["serie"]:
        serie=request.GET['serie']
        inventarios=Inventario.objects.filter(serie_icontains=serie)
        return render(request, "AppCoder/resultadoBusqueda.html", {"inventarios":inventarios, "serie":serie}) 
    else:
        respuesta = "no enviaste datos"
        return HttpResponse(respuesta)






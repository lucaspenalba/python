from django.shortcuts import render
from .models import Familiares
from django.http import HttpResponse
from django.template import Template, loader
# Create your views here.

def familiar(request):
    familiar=Familiares(nombre="Lucas", apellido="Peñalba", mail="lucas@gmail.com", fecha_nacimiento="1986-02-15", edad=36, sexo="masculino"  )
    familiar2=Familiares(nombre="Florencia", apellido="Peñalba", mail="florencia@gmail.com", fecha_nacimiento="1994-06-17", edad=27, sexo="femenino"  )
    familiar3=Familiares(nombre="Flavia", apellido="Peñalba", mail="flavia@gmail.com", fecha_nacimiento="1990-08-06", edad=32, sexo="femenino"  )
    familiar4=Familiares(nombre="Benjamin", apellido="Peñalba", mail="benjamin@gmail.com", fecha_nacimiento="2013-03-26", edad=9, sexo="masculino"  )
    familiar5=Familiares(nombre="Mariano", apellido="Peñalba", mail="mariano@gmail.com", fecha_nacimiento="1965-01-13", edad=57, sexo="masculino"  )
    familiar6=Familiares(nombre="Silvia", apellido="Vergara", mail="silvia@gmail.com", fecha_nacimiento="1963-11-26", edad=58, sexo="femenino"  )

    familiar.save()
    familiar2.save()
    familiar3.save()
    familiar4.save()
    familiar5.save()
    familiar6.save()

    diccionario = Familiares.objects.all().values()    
    plantilla=loader.get_template("template1.html")

    context = {'diccionario': diccionario,}


    return HttpResponse(plantilla.render(context, request))




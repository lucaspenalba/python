from django.shortcuts import render
from .models import Familiares
from django.http import HttpResponse
# Create your views here.

def familiar(request):
    familiar=Familiares(nombre="Lucas", apellido="Peñalba", mail="lucas@gmail.com", fecha_nacimiento="1986-02-15", edad=36, sexo="masculino"  )
    familiar2=Familiares(nombre="Florencia", apellido="Peñalba", mail="florencia@gmail.com", fecha_nacimiento="1986-02-15", edad=36, sexo="femenino"  )
    familiar3=Familiares(nombre="Flavia", apellido="Peñalba", mail="flavia@gmail.com", fecha_nacimiento="1986-02-15", edad=36, sexo="femenino"  )
    familiar4=Familiares(nombre="Benjamin", apellido="Peñalba", mail="benjamin@gmail.com", fecha_nacimiento="1986-02-15", edad=36, sexo="masculino"  )
    familiar5=Familiares(nombre="Mariano", apellido="Peñalba", mail="mariano@gmail.com", fecha_nacimiento="1986-02-15", edad=36, sexo="masculino"  )
    familiar=Familiares(nombre="Silvia", apellido="Vergara", mail="silvia@gmail.com", fecha_nacimiento="1986-02-15", edad=36, sexo="femenino"  )

    familiar.save()
    cadena_texto="Familiar Guardado "+familiar.nombre+" "+familiar.apellido
    return HttpResponse(cadena_texto)




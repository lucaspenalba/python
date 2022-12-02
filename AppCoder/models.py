from django.db import models

# Create your models here.

class Familiares(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    mail=models.EmailField()
    fecha_nacimiento=models.DateField()
    sexo=models.CharField(max_length=50)

    def _str_(self):
	    return self.nombre+" "+self.apellido


class Cliente(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    mail=models.EmailField()
    fecha_nacimiento=models.DateField()
    sexo=models.CharField(max_length=50)

    def _str_(self):
	    return self.nombre+" "+self.apellido


class Empleado(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    mail=models.EmailField()
    fecha_nacimiento=models.DateField()
    sexo=models.CharField(max_length=50)

    def _str_(self):
	    return self.nombre+" "+self.apellido    
            

class Inventario(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=50)    
    cantidad=models.IntegerField()
    precio=models.IntegerField()

    def _str_(self):
	    return self.nombre        



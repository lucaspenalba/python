from django.db import models

# Create your models here.

class Cliente(models.Model):    
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    correo=models.EmailField()

    def _str_(self):
	    return self.nombre+" "+self.apellido


class Empleado(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    mail=models.EmailField()

    def _str_(self):
	    return self.nombre+" "+self.apellido    


class Inventario(models.Model):
    serie=models.IntegerField()
    nombre=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=50)    
    cantidad=models.IntegerField()
    precio=models.IntegerField()

    def _str_(self):
	    return self.nombre        



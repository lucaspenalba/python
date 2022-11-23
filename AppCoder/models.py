from django.db import models

# Create your models here.

class Familiares(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    mail=models.EmailField()
    fecha_nacimiento=models.DateField()
    edad=models.IntegerField()
    sexo=models.CharField(max_length=50)

    def _str_(self):
	    return self.nombre+" "+self.apellido



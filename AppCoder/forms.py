from django import forms

class ClienteForm(forms.Form):
    nombre= forms.CharField(max_length=50)
    apellido= forms.CharField(max_length=50)
    correo= forms.EmailField()

class EmpleadoForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    mail=forms.EmailField()

class InventarioForm(forms.Form):
    serie=forms.IntegerField()
    nombre=forms.CharField(max_length=50)
    descripcion=forms.CharField(max_length=50)    
    cantidad=forms.IntegerField()
    precio=forms.IntegerField()



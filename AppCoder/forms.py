from django import forms

class ClienteForm(forms.Form):
    nombre= forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    mail=forms.EmailField()
    fecha_nacimiento=forms.DateField()
    sexo=forms.CharField(max_length=50)
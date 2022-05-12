from django import forms

class formularioProducto(forms.Form):
    nombre = forms.CharField(max_length=100)
    variedad = forms.CharField(max_length=100)
    caracteristica = forms.CharField(max_length=100)

class formularioProveedor(forms.Form):
    nombre = forms.CharField(max_length=100)
    telefono = forms.IntegerField()
    email = forms.EmailField()

class formularioCliente(forms.Form):
    nombre = forms.CharField(max_length=100)
    telefono = forms.IntegerField()
    email = forms.EmailField()
    observaciones = forms.CharField(max_length=250)
    

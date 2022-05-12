from http.client import HTTPResponse
from django.shortcuts import render

from AppAGranel.forms import formularioProducto, formularioProveedor, formularioCliente
from .models import Producto, Proveedor, Cliente
from django.template import loader
from django.http import HttpResponse


# Create your views here.
def producto(self):
    producto = Producto(nombre="Galletitas", variedad="Diabest", caracteristica="Apto diabeticos")
    producto.save()
    diccionario = {"mercaderia":producto}

    plantilla = loader.get_template('mercaderia.html')
    texto = plantilla.render(diccionario)
    return HttpResponse(texto)

#_____________________________________________________

def inicio(request):
    return render (request, 'AppAGranel/inicio.html')

def productos(request):
    if request.method == 'POST':
       formulario=formularioProducto(request.POST)
       if formulario.is_valid():
           informacion=formulario.cleaned_data
           producto=Producto(nombre=informacion['nombre'], variedad=informacion['variedad'], caracteristica=informacion['caracteristica'])
           producto.save()
           return render (request, 'AppAGranel/inicio.html')
    else:
        formulario=formularioProducto()
        return render (request, 'AppAGranel/productos.html', {'formulario':formulario})


def proveedores(request):
    if request.method == 'POST':
       formulario=formularioProveedor(request.POST)
       if formulario.is_valid():
           informacion=formulario.cleaned_data
           proveedor = Proveedor(nombre=informacion['nombre'], telefono=informacion['telefono'], email=informacion['email'])
           proveedor.save()
           return render (request, 'AppAGranel/inicio.html')
    else:
        formulario=formularioProveedor()
        return render (request, 'AppAGranel/proveedores.html', {'formulario':formulario})

def clientes(request):
    if request.method == 'POST':
       formulario=formularioCliente(request.POST)
       if formulario.is_valid():
           informacion=formulario.cleaned_data
           cliente = Cliente (nombre=informacion['nombre'], telefono=informacion['telefono'], email=informacion['email'], observaciones=informacion['observaciones'])
           cliente.save()
           return render (request, 'AppAGranel/inicio.html')
    else:
        formulario=formularioCliente()
        return render (request, 'AppAGranel/clientes.html', {'formulario':formulario})

def busquedaProductos(request):
    return render(request, 'AppAGranel/busquedaProductos.html')

def buscar(request):
    if request.get['caracteristica']:
       caracteristica = request.GET['caracteristica']
       productos = Producto.objects.filter(caracteristica__icontains = caracteristica)
       return render(request, 'AppAGranel/resultados.html', {'productos':producto,})
    else:
        respuesta = "No se ingreso producto"
        return HttpResponse(respuesta)

from django.urls import path
from .views import busquedaProductos, inicio, productos, proveedores, clientes, producto, buscar

urlpatterns = [

    path('', inicio, name='inicio'),
    path('agregaProducto/', producto),
    path('productos/', productos, name='productos'),
    path('proveedores/', proveedores, name='proveedores'),
    path('clientes/', clientes, name='clientes'),
    path('busquedaProductos', busquedaProductos, name='busquedaProductos'),
    path('buscar/', buscar, name="buscar"),
    
    ]
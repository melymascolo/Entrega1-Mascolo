from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    variedad = models.CharField(max_length=100)
    caracteristica = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre+" "+self.variedad

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.IntegerField()
    email = models.EmailField()
    observaciones = models.CharField(max_length=250)
    
    def __str__(self):
        return self.nombre+" "+self.observaciones

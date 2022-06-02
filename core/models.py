from django.db import models
from sqlalchemy import true

# Create your models here.
class categoria (models.Model):
    idCategoria = models.IntegerField(primary_key=true, verbose_name='Id de categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre de la categoria')

    def __str__(self):
        return self.nombreCategoria

# Modelo para el Vehiculo

class Vehiculo(models.Model):
    patente = models.CharField(max_length=6, primary_key=true, verbose_name='Patente')
    marca = models.CharField(max_length=20, verbose_name='Marca vehiculo')
    modelo = models.CharField(max_length=20, null=true, blank=true, verbose_name='Modelo')
    categoria = models.ForeignKey(categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.patente

        
from distutils.command.upload import upload
from django.db import models

# Create your models here.
class cliente(models.Model):
    idcliente=models.CharField(max_length=20, verbose_name="Ci",primary_key=True)
    nomcliente=models.CharField(max_length=30, verbose_name="Nombre")
    appaterno=models.CharField(max_length=30, verbose_name="Apellido Paterno")
    apmaterno=models.CharField(max_length=30, verbose_name="Apellido Materno")
    direccion=models.CharField(max_length=100, verbose_name="Direccion")
    edad=models.IntegerField( verbose_name="Edad")
    numcelular=models.IntegerField(verbose_name="Nº celular")

    def __str__(self):
        fila="Nombre:" + self.nomcliente
        return fila
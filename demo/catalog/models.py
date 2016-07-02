from __future__ import unicode_literals

from django.db import models

class Deudor(models.Model):
    rut = models.CharField(max_length=100,unique=True)
    nombres = models.TextField()
    apellido_p = models.CharField(max_length=100)
    apellido_m = models.CharField(max_length=100)
    estado_civil = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Deuda(models.Model):
    acreedor = models.CharField(max_length=200)
    date = models.TextField(blank=True,null=True)
    monto_deuda = models.IntegerField(default=0)
    deudor = models.ForeignKey(Deudor)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
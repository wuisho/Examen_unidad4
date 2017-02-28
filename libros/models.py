from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Libros(models.Model):
    Nombre = models.CharField(max_length=200, blank=False)
    Autor = models.CharField(max_length=200, blank=False)
    Editorial = models.CharField(max_length=200, blank=False)
    ISBN = models.CharField(max_length=200, blank=False)
    Precio = models.DecimalField(max_digits=1000, decimal_places=2,null=True, blank=True)

    def __unicode__(self):
        return self.Nombre

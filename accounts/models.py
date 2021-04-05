from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Tabla_test(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    columna_uno = models.CharField(max_length=200)
    columna_dos = models.CharField(max_length=200)
    columna_tres = models.CharField(max_length=200)
    columna_cuatro = models.CharField(max_length=200)
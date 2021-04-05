from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

GENDERS = (
    ('H', 'Hombre'),
    ('M', 'Mujer'),
    ('O', 'Otro'),
)
# Create your models here.
class Tabla_test(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    columna_uno = models.CharField(max_length=200)
    columna_dos = models.CharField(max_length=200)
    columna_tres = models.CharField(max_length=200)
    columna_cuatro = models.CharField(max_length=200)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, default='No indica')
    gender = models.CharField(max_length=1, choices=GENDERS, default='N')
    city = models.CharField(max_length=50, default='No indica')
    phone = models.IntegerField(default=0)
    
    def __str__(self):
        return self.user.first_name

# Función que se ejecuta cuando se crea un usuario nuevo, realiza un trigger que asocia ese usuario nuevo a un perfil UserProfile
def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile, sender=User)
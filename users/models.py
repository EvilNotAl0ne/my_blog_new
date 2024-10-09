from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, verbose_name="Televon")
    citi = models.CharField(max_length=100, verbose_name='Gorod')
    image = models.ImageField(upload_to='users/', null=True, verbose_name='Izobrachenie')


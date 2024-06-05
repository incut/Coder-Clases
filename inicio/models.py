from django.db import models

class Auto(models.Model):
    modelo = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    
    def __str__(self):
        return f'soy el auto {self.marca} {self.modelo}'
# Create your models here.

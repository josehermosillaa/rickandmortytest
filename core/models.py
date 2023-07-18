from django.db import models

# Create your models here.
class Personaje(models.Model):
    id = models.AutoField(primary_key=True)   #se iran creando id de manera automatica
    name = models.CharField(max_length=200, verbose_name="Nombre")   #1, 2,3,4,.......
    status = models.CharField(max_length=200 , verbose_name="Estado")
    species = models.CharField(max_length=200, verbose_name="Especie")
    gender = models.CharField(max_length=200, verbose_name="Género")
    image = models.URLField(max_length=200, verbose_name="URL imagen")
    #buenas practicas 
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

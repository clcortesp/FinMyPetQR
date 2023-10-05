from django.db import models
#from django.contrib.auth.models import User

# Create your models here.
class TipoMascota(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    


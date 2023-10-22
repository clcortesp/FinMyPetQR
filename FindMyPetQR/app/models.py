from django.db import models
from django.contrib.auth.models import User
from .choices import COLOR_CHOICES, GENERO
from django.db.models.signals import post_save
import uuid
import os
from django.conf import settings
from django.core.files.storage import default_storage

class ServicioApi(models.Model):
    client_id = models.CharField(max_length=100)
    grant_type = models.CharField(max_length=100)
    client_secret = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100, null=True)
    url = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


def mascota_picture_path(instance, filename):
    random_filename = str(uuid.uuid4())
    extension = os.path.splitext(filename)[1]
    # Utiliza el nombre de la mascota como parte de la ruta
    return 'mascotas/{}/{}{}'.format(instance.nombre, random_filename, extension)

def profile_picture_path(instance, filename):
    random_filename = str(uuid.uuid4())

    extension = os.path.splitext(filename)[1]

    return 'users/{}/{}{}'.format(instance.user.username, random_filename, extension)

# Create your models here.
class TipoMascota(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
class RazaMascota(models.Model):
    nombre = models.CharField(max_length=100)
    tipo_mascota = models.ForeignKey(TipoMascota, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nombre
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=100, null=True)
    ciudad = models.CharField(max_length=50, null=True)
    imagen = models.ImageField(default='default.png', upload_to=profile_picture_path, null=True)

    def save(self, *args, **kwargs):
        if self.pk and self.imagen.name != 'default.png':
            old_profile = UserProfile.objects.get(pk=self.pk)
            default_image_path = os.path.join(settings.MEDIA_ROOT, 'default.png')

            if old_profile.imagen.path != self.imagen.path and old_profile.imagen.path != default_image_path:
                default_storage.delete(old_profile.imagen.path)
        
        super(UserProfile, self).save(*args, **kwargs)
    

    def __str__(self):
        return self.user.username


class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.ForeignKey(TipoMascota, on_delete=models.CASCADE)
    raza = models.ForeignKey(RazaMascota, on_delete=models.CASCADE)
    edad = models.PositiveIntegerField()
    color = models.CharField(max_length=50, choices=COLOR_CHOICES, null=True)
    sexo = models.CharField(max_length=50, choices=GENERO, null=True)
    dueño = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    imagen = models.ImageField(upload_to=mascota_picture_path, null=True)
    sobre_mi = models.TextField(max_length=200, null=True)
    detalles_adicionales = models.TextField(max_length=200, null=True)
    perdida = models.BooleanField(default=False)
    

    def __str__(self):
        return self.nombre


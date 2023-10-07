from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Mascota

class MascotaForm(forms.ModelForm):
    
    class Meta:
        model = Mascota
        fields = ['nombre', 'tipo', 'raza', 'edad', 'color', 'sexo', 'imagen', 'sobre_mi', 'detalles_adicionales']
    
    

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Requerido. Ingrese una dirección de correo válida.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
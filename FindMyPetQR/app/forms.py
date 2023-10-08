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

class MascotaFormEdit(forms.ModelForm):

    class Meta:
        model = Mascota
        fields = ['edad', 'imagen', 'sobre_mi', 'detalles_adicionales']
        widgets = {
            'edad': forms.NumberInput(attrs={'class': 'form-control', 'style': 'border: 1px solid #f96332;'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control', 'style': 'border: 1px solid #f96332;'}),
            'sobre_mi': forms.Textarea(attrs={'class': 'form-control', 'style': 'border: 1px solid #f96332;'}),
            'detalles_adicionales': forms.Textarea(attrs={'class': 'form-control', 'style': 'border: 1px solid #f96332;'}),
        }
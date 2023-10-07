from django.shortcuts import render, redirect, get_object_or_404
from .models import Mascota, UserProfile, RazaMascota, TipoMascota
from .forms import UserRegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
# Create your views here.


def home(request):
    return render(request, 'app/home.html')

def landing(request):
    return render(request, 'app/landing-page.html')

def registro(request):
    data = {
        'form': UserRegistrationForm()
    }

    if request.method == 'POST':
        formulario = UserRegistrationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            
            login(request, user)

            user_profile = UserProfile(user=user)
            user_profile.save()

            messages.success(request, "Te has registrado correctamente")
            return redirect(to='home')
        else:
            form = UserRegistrationForm()
    return render(request, 'registration/registro.html', data)
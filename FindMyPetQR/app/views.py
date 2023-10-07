from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
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

@login_required
def profile(request):
    user = get_object_or_404(User, id=request.user.id)
    usuario = UserProfile.objects.filter(user=user)
    mascotas = Mascota.objects.filter(dueño=user)
    perros_count = Mascota.objects.filter(dueño=user, tipo__nombre='Perro').count()
    gatos_count = Mascota.objects.filter(dueño=user, tipo__nombre='Gato').count()
    total_mascotas = Mascota.objects.filter(dueño=user).count()
    data = {
        'usuario': usuario,
        'mascota': mascotas,
        'perros_count': perros_count,
        'gatos_count': gatos_count,
        'total_mascotas': total_mascotas,
    }
    return render(request, 'app/profile-page.html', data)

def petProfile(request, id):
    mascota = Mascota.objects.get(id=id)
    data = {
        'mascota': mascota,
    }
    return render(request, 'app/pet-profile.html', data)
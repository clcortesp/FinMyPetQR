from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from app.serializers import RazaSerializer, MascotasSerializer
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from app.models import Mascota, UserProfile, RazaMascota, TipoMascota, ServicioApi
from app.forms import UserRegistrationForm, MascotaForm, MascotaFormEdit, ProfileFormEdit
from django.contrib.auth import login, authenticate
from django.contrib import messages
from app.api import getToken, enviar_correo, getDireccion

# Create your views here.
def home(request):
    return render(request, 'inv/base.html')
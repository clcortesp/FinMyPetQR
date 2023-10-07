from django.urls import path, include
from .views import home, landing, registro

urlpatterns = [
    path('', home, name="home"),
    path('landing', landing, name="landing"),

    path('registro/', registro, name='registro'),
]
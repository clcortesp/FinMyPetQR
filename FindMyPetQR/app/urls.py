from django.urls import path, include
from .views import home, landing, registro, profile

urlpatterns = [
    path('', landing, name="home"),

    path('registro/', registro, name='registro'),

    path('profile/', profile, name="profile"),
]
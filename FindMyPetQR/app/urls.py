from django.urls import path, include
from .views import home, landing

urlpatterns = [
    path('', home, name="home"),
    path('landing', landing, name="landing"),
]
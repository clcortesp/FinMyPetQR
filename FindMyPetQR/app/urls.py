from django.urls import path, include
from .views import home, landing, registro, profile, petProfile, newPet, RazaViewset, MascotasViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'apiRazas', RazaViewset, basename='raza')
router.register(r'apiMascotas', MascotasViewset)


urlpatterns = [
    path('', landing, name="home"),

    path('registro/', registro, name='registro'),
    path('api/', include(router.urls)),

    path('profile/', profile, name="profile"),
    path('newPet/', newPet, name="newPet"),
    path('petProfile/<id>/', petProfile, name="petProfile"),
]

urlpatterns += router.urls
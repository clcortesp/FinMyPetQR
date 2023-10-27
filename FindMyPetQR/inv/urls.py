from django.urls import path, include
from app.views import landing, registro, profile, petProfile, newPet, RazaViewset, MascotasViewset, deletePet, petEdit, reportar_perdida, reportar_encontrada, profileEdit
from rest_framework import routers
from .views import home

router = routers.DefaultRouter()
router.register(r'apiRazas', RazaViewset, basename='raza')
router.register(r'apiMascotas', MascotasViewset)


urlpatterns = [
    path('casa/', home, name="home"),

    #path('registro/', registro, name='registro'),
    path('api/', include(router.urls)),

    #path('profile/', profile, name="profile"),
    #path('profileEdit/', profileEdit, name="profileEdit"),
    #path('newPet/', newPet, name="newPet"),
    #path('petProfile/<id>/', petProfile, name="petProfile"),
    #path('deletePet/<id>/', deletePet, name="deletePet"),
    #path('petEdit/<id>/', petEdit, name="petEdit"),

    #path('reportar_perdida/<int:id>/', reportar_perdida, name='reportar_perdida'),
    #path('reportar_encontrada/<int:id>/', reportar_encontrada, name='reportar_encontrada'),

]

urlpatterns += router.urls
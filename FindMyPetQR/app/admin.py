from django.contrib import admin
from .models import TipoMascota, RazaMascota, UserProfile, Mascota, ServicioApi

# Register your models here.

class RazaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'tipo_mascota']
    search_fields = ['nombre']
    list_filter = ['tipo_mascota']

class MascotasAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'tipo', 'raza', 'color', 'sexo', 'dueño', 'perdida']
    search_fields = ['nombre', 'dueño']
    list_filter = ['tipo']

admin.site.register(TipoMascota)
admin.site.register(RazaMascota, RazaAdmin)
admin.site.register(UserProfile)
admin.site.register(ServicioApi)
admin.site.register(Mascota, MascotasAdmin)
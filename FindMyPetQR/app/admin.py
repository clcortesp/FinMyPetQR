from django.contrib import admin
from .models import TipoMascota, RazaMascota, UserProfile, Mascota

# Register your models here.

class RazaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'tipo_mascota']
    search_fields = ['nombre']
    list_filter = ['tipo_mascota']

class MascotasAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'tipo', 'raza', 'dueño']
    search_fields = ['nombre', 'dueño']
    list_filter = ['tipo']

admin.site.register(TipoMascota)
admin.site.register(RazaMascota, RazaAdmin)
admin.site.register(UserProfile)
admin.site.register(Mascota, MascotasAdmin)
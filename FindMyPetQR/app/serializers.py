from .models import RazaMascota, Mascota
from rest_framework import serializers

class RazaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RazaMascota
        fields = '__all__'


class MascotasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = '__all__'
        
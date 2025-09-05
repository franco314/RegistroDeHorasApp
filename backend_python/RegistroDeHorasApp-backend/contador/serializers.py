from rest_framework import serializers
from .models import RegistroDeHoras

class RegistroDeHorasSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroDeHoras
        fields = ['id', 'usuario', 'fecha', 'horas']
        read_only_fields = ['id', 'usuario']


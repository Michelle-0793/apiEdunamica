#INFORMACIÓN QUE SE VA A USAR Y COMO SE VA A USAR
from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
    def validate_Nombre(self, value):
        if len(value) <= 2:
            raise serializers.ValidationError("El nombre debe tener más de 2 caracteres.")
        return value

    def validate_Apellido(self, value):
        if len(value) <= 2:
            raise serializers.ValidationError("El Apellido debe tener más de 2 caracteres.")
        return value  
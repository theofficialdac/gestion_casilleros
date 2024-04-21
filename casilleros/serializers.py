# En tu archivo serializers.py
from rest_framework import serializers
from .models import Casillero, Contrato, Arrendatario
from accounts.models import CustomUser

class ArrendatarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arrendatario
        fields = ['nombre', 'rut', 'celular', 'email']


class CasilleroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Casillero
        fields = ['id', 'numero', 'ubicacion', 'ocupado']


class ContratoSerializer(serializers.ModelSerializer):
    arrendatario = ArrendatarioSerializer()

    class Meta:
        model = Contrato
        fields = ['id', 'casillero', 'arrendatario', 'fecha_inicio', 'fecha_fin', 'pagado']

    def create(self, validated_data):
        arrendatario_data = validated_data.pop('arrendatario')
        arrendatario, created = Arrendatario.objects.get_or_create(**arrendatario_data)
        contrato = Contrato.objects.create(arrendatario=arrendatario, **validated_data)
        return contrato

from django.contrib.auth import get_user_model

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'nombre', 'apellido', 'rut', 'telefono', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance

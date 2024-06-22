from rest_framework import serializers
from sagasouls.models import Director, Genero, SagaSouls


class SagaSoulsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SagaSouls
        fields = ['name', 'año', 'company', 'GOTY']


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['name', 'country', 'company', 'GOTY']


class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = ['name', 'subgenero']

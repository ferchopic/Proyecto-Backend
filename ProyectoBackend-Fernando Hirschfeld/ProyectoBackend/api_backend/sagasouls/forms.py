from django import forms
from sagasouls.models import Director, Genero, SagaSouls, User


class SagaSoulsForm(forms.ModelForm):
    class Meta:
        model = SagaSouls
        fields = [
            'name',
            'año',
            'company',
            'GOTY',
        ]


class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = [
            'name',
            'company',
            'GOTY',
        ]


class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = [
            'name',
            'subgenero',
        ]


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'name',
            'sagasouls',
            'directors',
            'genero',
        ]

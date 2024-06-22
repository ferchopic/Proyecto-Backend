from django.db import models

# Create your models here.


class SagaSouls(models.Model):
    name = models.CharField(max_length=128)
    año = models.IntegerField()
    company = models.CharField(max_length=128)
    GOTY = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id} - {self.name}'


class Director(models.Model):
    name = models.CharField(max_length=128)
    company = models.CharField(max_length=128)
    GOTY = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id} - {self.name}'


class Genero(models.Model):
    name = models.CharField(max_length=128)
    subgenero = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.id} - {self.name}'


class User(models.Model):
    name = models.CharField(max_length=128)
    sagasouls = models.ManyToManyField(SagaSouls, blank=True)
    directors = models.ManyToManyField(Director, blank=True)
    genero = models.ManyToManyField(Genero, blank=True)

    def __str__(self):
        return self.name

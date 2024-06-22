from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import CreateView
from sagasouls.forms import DirectorForm, GeneroForm, SagaSoulsForm, UserForm
from sagasouls.models import Director, Genero, SagaSouls
from sagasouls.serializers import (DirectorSerializer, GeneroSerializer,
                                   SagaSoulsSerializer)

# Create your views here.


def get_all_sagasouls():
    sagasouls = SagaSouls.objects.all().order_by('name')
    sagasouls_serializers = SagaSoulsSerializer(sagasouls, many=True)
    return sagasouls_serializers.data


def get_all_directors():
    directors = Director.objects.all().order_by('name')
    directors_serializers = DirectorSerializer(directors, many=True)
    return directors_serializers.data


def get_all_genero():
    genero = Genero.objects.all().order_by('name')
    genero_serializers = GeneroSerializer(genero, many=True)
    return genero_serializers.data


def sagasouls_rest(request):
    sagasouls = get_all_sagasouls()
    return JsonResponse(sagasouls, safe=False)


def directors_rest(request):
    directors = get_all_directors()
    return JsonResponse(directors, safe=False)


def genero_rest(request):
    genero = get_all_genero()
    return JsonResponse(genero, safe=False)


def index_sagasouls(request):
    sagasouls = get_all_sagasouls()
    directors = get_all_directors()
    genero = get_all_genero()
    return render(request, 'index_sagasouls.html', {'sagasouls': sagasouls, 'directors': directors, 'genero': genero})


def users_rest(request):
    return JsonResponse("Ok", safe=False)


class NewSagaSoulsView(CreateView):
    form_class = SagaSoulsForm
    template_name = 'form_sagasouls.html'
    success_url = '/'


class NewDirectorView(CreateView):
    form_class = DirectorForm
    template_name = 'form_director.html'
    success_url = '/'


class NewGeneroView(CreateView):
    form_class = GeneroForm
    template_name = 'form_genero.html'
    success_url = '/'


class NewUserView(CreateView):
    form_class = UserForm
    template_name = 'form_usu.html'
    success_url = '/'

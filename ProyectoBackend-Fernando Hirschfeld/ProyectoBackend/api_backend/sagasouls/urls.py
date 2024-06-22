from django.urls import path
from sagasouls import views

urlpatterns = [
    path('', views.index_sagasouls, name='index_sagasouls'),
    path('sagasouls_rest/', views.sagasouls_rest, name='sagasouls_rest'),
    path('directors_rest/', views.directors_rest, name='directors_rest'),
    path('genero_rest/', views.genero_rest, name='genero_rest'),
    path('users_rest/', views.users_rest, name='users_rest'),
    path('new_sagasouls/', views.NewSagaSoulsView.as_view(), name='new_sagasouls'),
    path('new_director/', views.NewDirectorView.as_view(), name='new_director'),
    path('new_genero/', views.NewGeneroView.as_view(), name='new_genero'),
    path('new_userp/', views.NewUserView.as_view(), name='new_userp'),
]

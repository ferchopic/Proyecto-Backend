from django.urls import path
from funko_api import views

urlpatterns = [
    path('index_funko/', views.index, name='funkos'),
    path('funkos_rest/', views.funkos_rest, name='funkos_rest'),
    path('users_rest/', views.users_rest, name='users_rest'),
    path('new_funko/', views.NewFunkoView.as_view(), name='new_funko'),
    path('new_user/', views.NewUserView.as_view(), name='new_userf'),
]
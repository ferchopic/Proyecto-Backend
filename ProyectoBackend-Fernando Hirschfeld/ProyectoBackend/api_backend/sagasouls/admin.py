from django.contrib import admin
from sagasouls.models import Director, Genero, SagaSouls, User

# Register your models here.

admin.site.register(SagaSouls)
admin.site.register(User)
admin.site.register(Director)
admin.site.register(Genero)

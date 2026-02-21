from django.contrib import admin
from .models import Gastos, Entradas, Fixos, Cartao

admin.site.register(Gastos)
admin.site.register(Entradas)
admin.site.register(Fixos)
admin.site.register(Cartao)
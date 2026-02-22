from django.contrib import admin
from .models import Entradas, Fixos, Cartao, Caixinhas, Dividas

admin.site.register(Entradas)
admin.site.register(Fixos)
admin.site.register(Cartao)
admin.site.register(Caixinhas)
admin.site.register(Dividas)
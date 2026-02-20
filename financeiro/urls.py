from django.urls import path
from . import views

app_name = 'financeiro'

urlpatterns = [
    path('', views.visao_geral, name="inicio"),
    path('entradas/', views.cadastrar_entradas, name='entradas')
]
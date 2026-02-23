from django.urls import path
from . import views

app_name = 'entradas'

urlpatterns = [
    path('', views.entradas, name='entradas'),
    path('cadastrar_entradas/', views.cadastrar_entradas, name='cadastrar_entradas'),
    path('editar_entradas/<int:id>', views.editar_entradas, name="editar_entradas"),
    path('excluir_entradas/<int:id>', views.excluir_entradas, name='excluir_entradas'),
]
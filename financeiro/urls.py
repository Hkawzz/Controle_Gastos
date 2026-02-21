from django.urls import path
from . import views

app_name = 'financeiro'

urlpatterns = [
    path('', views.visao_geral, name="inicio"),
    path('cadastrar_entradas/', views.cadastrar_entradas, name='cadastrar_entradas'),
    path('editar_entradas/<int:id>', views.editar_entradas, name="editar_entradas"),
    path('excluir_entradas/<int:id>', views.excluir_entradas, name='excluir_entradas'),
    path('cadastrar_gastos/', views.cadastrar_gastos, name='cadastrar_gastos'),
    path('editar_gastos/<int:id>', views.editar_gastos, name='editar_gastos'),
    path('excluir_gastos/<int:id>', views.excluir_gastos, name='excluir_gastos'),
    path('cadastrar_fixos/', views.cadastrar_fixos, name='cadastrar_fixos'),
    path('excluir_fixos/<int:id>', views.excluir_fixos, name='excluir_fixos'),
]
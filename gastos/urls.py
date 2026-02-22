from django.urls import path
from . import views

app_name = 'gastos'

urlpatterns = [
    path('', views.gastos, name='gastos'),
    path('cadastrar_gasto/', views.cadastrar_gasto, name='cadastrar_gasto'),
    path('editar_gasto/<int:id>', views.editar_gasto, name='editar_gasto'),
    path('excluir_gasto/<int:id>', views.excluir_gasto, name='excluir_gasto'),
]
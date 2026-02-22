from django.urls import path
from . import views

app_name = 'financeiro'

urlpatterns = [
    path('', views.visao_geral, name="inicio"),
    path('entradas/', views.entradas, name='entradas'),
    path('cadastrar_entradas/', views.cadastrar_entradas, name='cadastrar_entradas'),
    path('editar_entradas/<int:id>', views.editar_entradas, name="editar_entradas"),
    path('excluir_entradas/<int:id>', views.excluir_entradas, name='excluir_entradas'),
    path('gastos/', views.gastos, name='gastos'),
    path('cadastrar_gasto/', views.cadastrar_gasto, name='cadastrar_gasto'),
    path('editar_gasto/<int:id>', views.editar_gasto, name='editar_gasto'),
    path('excluir_gasto/<int:id>', views.excluir_gasto, name='excluir_gasto'),
    path('fixos', views.fixos, name='fixos'),
    path('cadastrar_fixos/', views.cadastrar_fixos, name='cadastrar_fixos'),
    path('editar_fixos/<int:id>', views.editar_fixos, name='editar_fixos'),
    path('excluir_fixos/<int:id>', views.excluir_fixos, name='excluir_fixos'),
    path('cartao/', views.cartao, name='cartao'),
    path('cadastrar_cartao/', views.cadastrar_cartao, name='cadastrar_cartao'),
    path('editar_cartao/<int:id>', views.editar_cartao, name='editar_cartao'),
    path('excluir_cartao/<int:id>', views.excluir_cartao, name='excluir_cartao'),
    path('cadastrar_caixinhas/', views.cadastrar_caixinhas, name='cadastrar_caixinha'),
    path('editar_caixinha/<int:id>', views.editar_caixinha, name='editar_caixinha'),
    path('excluir_caixinha/<int:id>', views.excluir_caixinha, name='excluir_caixinha'),
    path('cadastrar_divida/', views.cadastrar_divida, name='cadastrar_divida'),
    path('editar_id/<int:id>', views.editar_divida, name='editar_divida'),
    path('excluir_divida/<int:id>', views.excluir_divida, name='excluir_divida'),
]
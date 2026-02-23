from django.urls import path
from . import views

app_name = 'financeiro'

urlpatterns = [
    path('', views.visao_geral, name="inicio"),
    path('caixinhas/', views.caixinhas, name='caixinhas'),
    path('cadastrar_caixinha/', views.cadastrar_caixinha, name='cadastrar_caixinha'),
    path('editar_caixinha/<int:id>', views.editar_caixinha, name='editar_caixinha'),
    path('excluir_caixinha/<int:id>', views.excluir_caixinha, name='excluir_caixinha'),
    path('dividas/', views.dividas, name='dividas'),
    path('cadastrar_divida/', views.cadastrar_divida, name='cadastrar_divida'),
    path('editar_id/<int:id>', views.editar_divida, name='editar_divida'),
    path('excluir_divida/<int:id>', views.excluir_divida, name='excluir_divida'),
]
from django.urls import path
from . import views

app_name = 'caixinhas'

urlpatterns = [
    path('', views.caixinhas, name='caixinhas'),
    path('cadastrar_caixinha/', views.cadastrar_caixinha, name='cadastrar_caixinha'),
    path('editar_caixinha/<int:id>', views.editar_caixinha, name='editar_caixinha'),
    path('excluir_caixinha/<int:id>', views.excluir_caixinha, name='excluir_caixinha'),
]
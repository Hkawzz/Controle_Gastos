from django.urls import path
from . import views

app_name = 'cartao'

urlpatterns = [
    path('', views.cartao, name='cartao'),
    path('cadastrar_cartao/', views.cadastrar_cartao, name='cadastrar_cartao'),
    path('editar_cartao/<int:id>', views.editar_cartao, name='editar_cartao'),
    path('excluir_cartao/<int:id>', views.excluir_cartao, name='excluir_cartao'),
]
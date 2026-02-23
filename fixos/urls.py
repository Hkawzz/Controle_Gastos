from django.urls import path
from . import views

app_name = 'fixos'

urlpatterns = [
    path('', views.fixos, name='fixos'),
    path('cadastrar_fixos/', views.cadastrar_fixos, name='cadastrar_fixos'),
    path('editar_fixos/<int:id>', views.editar_fixos, name='editar_fixos'),
    path('excluir_fixos/<int:id>', views.excluir_fixos, name='excluir_fixos'),
]
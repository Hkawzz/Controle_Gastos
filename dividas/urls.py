from django.urls import path
from . import views

app_name = 'dividas'

urlpatterns = [
    path('', views.dividas, name='dividas'),
    path('cadastrar_divida/', views.cadastrar_divida, name='cadastrar_divida'),
    path('editar_id/<int:id>', views.editar_divida, name='editar_divida'),
    path('excluir_divida/<int:id>', views.excluir_divida, name='excluir_divida'),
]
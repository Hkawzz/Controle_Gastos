from django.urls import path
from . import views

app_name = 'financeiro'

urlpatterns = [
    path('', views.inicio, name="inicio")
]
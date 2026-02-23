from django.shortcuts import render
from gastos.models import Gastos
from entradas.models import Entradas
from fixos.models import Fixos
from cartao.models import Cartao
from caixinhas.models import Caixinhas
from dividas.models import Dividas

def visao_geral(request):
    saldo_total = saldo()
    
    return render(request, "visao_geral/index.html", {'saldo_total': saldo_total})

def saldo():
    gastos = Gastos.objects.all()
    entradas = Entradas.objects.all()

    total_gastos = sum(item.valor for item in gastos)
    total_entradas = sum(item.valor for item in entradas)
    saldo = total_entradas - total_gastos

    return saldo

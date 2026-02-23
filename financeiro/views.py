from django.shortcuts import render
from gastos.models import Gastos
from entradas.models import Entradas
from fixos.models import Fixos
from cartao.models import Cartao
from caixinhas.models import Caixinhas
from dividas.models import Dividas

def visao_geral(request):
    saldo_total, total_gastos, total_entradas = saldo()
    total_caixinhas = caixinha()
    fixos = Fixos.objects.all()
    cartao = Cartao.objects.all()
    dividas = Dividas.objects.all()
    caixinhas = Caixinhas.objects.all()
    
    return render(request, "visao_geral/index.html", {
        'saldo_total': saldo_total,
        'total_gastos': total_gastos,
        'total_entradas': total_entradas,
        'total_caixinhas': total_caixinhas,
        'fixos': fixos,
        'cartao': cartao,
        'dividas': dividas,
        'caixinhas': caixinhas,
        })

def saldo():
    gastos = Gastos.objects.all()
    entradas = Entradas.objects.all()

    total_gastos = sum(item.valor for item in gastos)
    total_entradas = sum(item.valor for item in entradas)
    saldo = total_entradas - total_gastos

    return saldo, total_gastos, total_entradas

def caixinha():
    caixinhas = Caixinhas.objects.all()

    total_caixinhas = sum(item.guardado for item in caixinhas)
    return total_caixinhas
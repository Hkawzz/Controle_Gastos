from django.shortcuts import render, redirect, get_object_or_404
from .models import Gastos, Entradas, Fixos, Cartao, Caixinhas, Dividas
from .forms import GastosForm, EntradasForm, FixosForm, CartaoForm, CaixinhasForm, DividasForm

def visao_geral(request):
    gastos = Gastos.objects.all()
    fixos = Fixos.objects.all()
    cartao = Cartao.objects.all()
    caixinhas = Caixinhas.objects.all()
    dividas = Dividas.objects.all()

    return render(request, "visao_geral/index.html", {
        'gastos': gastos,
        'entradas': entradas,
        'fixos': fixos,
        'cartao': cartao,
        'caixinhas': caixinhas,
        'dividas': dividas})

def entradas(request):
    entradas = Entradas.objects.all()

    return render(request, "entradas/index.html", {'entradas': entradas})

def cadastrar_entradas(request):
    if request.method == 'POST':
        form = EntradasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('financeiro:entradas')
        
    else:
        form = EntradasForm()
    
    return render(request, "entradas/form.html", {'form': form})

def editar_entradas(request, id):
    entrada = get_object_or_404(Entradas, id=id)
    if request.method == 'POST':
        form = EntradasForm(request.POST, instance=entrada)
        if form.is_valid():
            form.save()

            return redirect('financeiro:entradas')

    else:
        form = EntradasForm(instance=entrada)

    return render(request, "entradas/form.html", {'form': form})

def excluir_entradas(request, id):
    entradas = get_object_or_404(Entradas, id=id)
    entradas.delete()

    return redirect('financeiro:entradas')

def gastos(request):
    gastos = Gastos.objects.all()

    return render(request, "gastos/index.html", {'gastos': gastos})

def cadastrar_gasto(request):
    if request.method == 'POST':
        form = GastosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('financeiro:gastos')
        
    else:
        form = GastosForm()
    
    return render(request, "gastos/form.html", {'form': form})

def editar_gasto(request, id):
    gasto = get_object_or_404(Gastos, id=id)
    if request.method == 'POST':
        form = GastosForm(request.POST, instance=gasto)
        if form.is_valid():
            form.save()

            return redirect('financeiro:gastos')

    else:
        form = GastosForm(instance=gasto)

    return render(request, "gastos/form.html", {'form': form})

def excluir_gasto(request, id):
    gasto = get_object_or_404(Gastos, id=id)
    gasto.delete()

    return redirect('financeiro:gastos')

def fixos(request):
    fixos = Fixos.objects.all()

    return render(request, "fixos/index.html", {'fixos': fixos})


def cadastrar_fixos(request):
    if request.method == 'POST':
        form = FixosForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('financeiro:fixos')
        
    else:
        form = FixosForm()

    return render(request, "fixos/form.html", {'form': form})

def editar_fixos(request, id):
    fixo = get_object_or_404(Fixos, id=id)
    if request.method == 'POST':
        form =FixosForm(request.POST, instance=fixo)
        if form.is_valid():
            form.save()

            return redirect('financeiro:fixos')
        
    else:
        form = FixosForm(instance=fixo)

    return render(request, "fixos/form.html", {'form': form})

def excluir_fixos(request, id):
    fixo =get_object_or_404(Fixos, id=id)
    fixo.delete()

    return redirect('financeiro:fixos')

def cartao(request):
    cartao = Cartao.objects.all()

    return render(request, "cartao/index.html", {'cartao': cartao})

def cadastrar_cartao(request):
    if request.method == 'POST':
        form = CartaoForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('financeiro:cartao')
        
    else:
        form = CartaoForm()

    return render(request, "cartao/form.html", {'form': form})

def editar_cartao(request, id):
    form = get_object_or_404(Cartao, id=id)
    if request.method == 'POST':
        form = CartaoForm(request.POST, instance=form)
        if form.is_valid():
            form.save()

            return redirect('financeiro:cartao')
        
    else:
        form = CartaoForm(instance=form)

    return render(request, "cartao/form.html", {'form': form})

def excluir_cartao(request, id):
    form = get_object_or_404(Cartao, id=id)
    form.delete()

    return redirect('financeiro:cartao')

def cadastrar_caixinhas(request):
    if request.method == 'POST':
        form = CaixinhasForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('financeiro:inicio')
        
    else:
        form = CaixinhasForm()

    return render(request, "caixinhas/form.html", {'form': form})

def editar_caixinha(request, id):
    form = get_object_or_404(Caixinhas, id=id)
    if request.method == 'POST':
        form = CaixinhasForm(request.POST, instance=form)
        if form.is_valid():
            form.save()

            return redirect('financeiro:inicio')
        
    else:
        form = CaixinhasForm(instance=form)

    return render(request, "caixinhas/form.html", {'form': form})

def excluir_caixinha(request, id):
    form = get_object_or_404(Caixinhas, id=id)
    form.delete()

    return redirect('financeiro:inicio')

def cadastrar_divida(request):
    if request.method == 'POST':
        form = DividasForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('financeiro:inicio')
        
    else:
        form = DividasForm()

    return render(request, "dividas/form.html", {'form': form})

def editar_divida(request, id):
    form = get_object_or_404(Dividas, id=id)
    if request.method == 'POST':
        form = DividasForm(request.POST, instance=form)
        if form.is_valid():
            form.save()

            return redirect('financeiro:inicio')
        
    else:
        form = DividasForm(instance=form)

    return render(request, "dividas/form.html", {'form': form})

def excluir_divida(request, id):
    form = get_object_or_404(Dividas, id=id)
    form.delete()

    return redirect('financeiro:inicio')
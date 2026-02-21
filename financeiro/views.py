from django.shortcuts import render, redirect, get_object_or_404
from .models import Gastos, Entradas, Fixos, Cartao, Caixinhas, Dividas
from .forms import GastosForm, EntradasForm, FixosForm, CartaoForm, CaixinhasForm, DividasForm

def visao_geral(request):
    gastos = Gastos.objects.all()
    entradas = Entradas.objects.all()
    fixos = Fixos.objects.all()
    cartao = Cartao.objects.all()

    return render(request, "visao_geral/index.html", {
        'gastos': gastos,
        'entradas': entradas,
        'fixos': fixos,
        'cartao': cartao})

def cadastrar_entradas(request):
    if request.method == 'POST':
        form = EntradasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('financeiro:inicio')
        
    else:
        form = EntradasForm()
    
    return render(request, "entradas/index.html", {'form': form})

def editar_entradas(request, id):
    entrada = get_object_or_404(Entradas, id=id)
    if request.method == 'POST':
        form = EntradasForm(request.POST, instance=entrada)
        if form.is_valid():
            form.save()

            return redirect('financeiro:inicio')

    else:
        form = EntradasForm(instance=entrada)

    return render(request, "entradas/index.html", {'form': form})

def excluir_entradas(request, id):
    entradas = get_object_or_404(Entradas, id=id)
    entradas.delete()

    return redirect('financeiro:inicio')

def cadastrar_gastos(request):
    if request.method == 'POST':
        form = GastosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('financeiro:inicio')
        
    else:
        form = GastosForm()
    
    return render(request, "gastos/index.html", {'form': form})

def editar_gastos(request, id):
    gasto = get_object_or_404(Gastos, id=id)
    if request.method == 'POST':
        form = GastosForm(request.POST, instance=gasto)
        if form.is_valid():
            form.save()

            return redirect('financeiro:inicio')

    else:
        form = GastosForm(instance=gasto)

    return render(request, "gastos/index.html", {'form': form})

def excluir_gastos(request, id):
    gasto = get_object_or_404(Gastos, id=id)
    gasto.delete()

    return redirect('financeiro:inicio')

def cadastrar_fixos(request):
    if request.method == 'POST':
        form = FixosForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('financeiro:inicio')
        
    else:
        form = FixosForm()

    return render(request, "fixos/index.html", {'form': form})

def editar_fixos(request, id):
    fixo = get_object_or_404(Fixos, id=id)
    if request.method == 'POST':
        form =FixosForm(request.POST, instance=fixo)
        if form.is_valid():
            form.save()

            return redirect('financeiro:inicio')
        
    else:
        form = FixosForm(instance=fixo)

    return render(request, "fixos/index.html", {'form': form})

def excluir_fixos(request, id):
    fixo =get_object_or_404(Fixos, id=id)
    fixo.delete()

    return redirect('financeiro:inicio')

def cadastrar_cartao(request):
    if request.method == 'POST':
        form = CartaoForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('financeiro:inicio')
        
    else:
        form = CartaoForm()

    return render(request, "cartao/index.html", {'form': form})

def editar_cartao(request, id):
    form = get_object_or_404(Cartao, id=id)
    if request.method == 'POST':
        form = CartaoForm(request.POST, instance=form)
        if form.is_valid():
            form.save()

            return redirect('financeiro:inicio')
        
    else:
        form = CartaoForm(instance=form)

    return render(request, "cartao/index.html", {'form': form})

def excluir_cartao(request, id):
    form = get_object_or_404(Cartao, id=id)
    form.delete()

    return redirect('financeiro:inicio')

def cadastrar_caixinhas(request):
    if request.method == 'POST':
        form = CaixinhasForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('financeiro:inicio')
        
    else:
        form = CaixinhasForm()

    return render(request, "caixinhas/index.html", {'form': form})
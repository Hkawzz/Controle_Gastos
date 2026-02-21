from django.shortcuts import render, redirect, get_object_or_404
from .models import Gastos, Entradas, Fixos, Cartao
from .forms import GastosForm, EntradasForm, FixosForm, CartaoForm

def visao_geral(request):
    gastos = Gastos.objects.all()
    entradas = Entradas.objects.all()
    fixos = Fixos.objects.all()

    return render(request, "visao_geral/index.html", {'gastos': gastos, 'entradas': entradas, 'fixos': fixos})

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
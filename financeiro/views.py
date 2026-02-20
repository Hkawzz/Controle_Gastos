from django.shortcuts import render, redirect
from .models import Gastos, Entradas
from .forms import GastosForm, EntradasForm

def visao_geral(request):
    gastos = Gastos.objects.all()
    entradas = Entradas.objects.all()

    return render(request, "visao_geral/index.html", {'gastos': gastos, 'entradas': entradas})

def cadastrar_entradas(request):
    if request.method == 'POST':
        form = EntradasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('financeiro:inicio')
        
    else:
        form = EntradasForm()
    
    return render(request, "entradas/index.html", {'form': form})

def cadastrar_gastos(request):
    if request.method == 'POST':
        form = GastosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('financeiro:inicio')
        
    else:
        form = GastosForm()
    
    return render(request, "gastos/index.html", {'form': form})
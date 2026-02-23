from django.shortcuts import render, redirect, get_object_or_404
from .models import Entradas
from .forms import EntradasForm

def entradas(request):
    entradas = Entradas.objects.all()

    return render(request, "entradas/index.html", {'entradas': entradas})

def cadastrar_entradas(request):
    if request.method == 'POST':
        form = EntradasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('entradas:entradas')
        
    else:
        form = EntradasForm()
    
    return render(request, "entradas/form.html", {'form': form})

def editar_entradas(request, id):
    entrada = get_object_or_404(Entradas, id=id)
    if request.method == 'POST':
        form = EntradasForm(request.POST, instance=entrada)
        if form.is_valid():
            form.save()

            return redirect('entradas:entradas')

    else:
        form = EntradasForm(instance=entrada)

    return render(request, "entradas/form.html", {'form': form})

def excluir_entradas(request, id):
    entradas = get_object_or_404(Entradas, id=id)
    entradas.delete()

    return redirect('entradas:entradas')
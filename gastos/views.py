from django.shortcuts import render, redirect, get_object_or_404
from .models import Gastos
from .forms import GastosForm

def gastos(request):
    gastos = Gastos.objects.all()

    return render(request, "gastos/index.html", {'gastos': gastos})

def cadastrar_gasto(request):
    if request.method == 'POST':
        form = GastosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gastos:gastos')
        
    else:
        form = GastosForm()
    
    return render(request, "gastos/form.html", {'form': form})

def editar_gasto(request, id):
    gasto = get_object_or_404(Gastos, id=id)
    if request.method == 'POST':
        form = GastosForm(request.POST, instance=gasto)
        if form.is_valid():
            form.save()

            return redirect('gastos:gastos')

    else:
        form = GastosForm(instance=gasto)

    return render(request, "gastos/form.html", {'form': form})

def excluir_gasto(request, id):
    gasto = get_object_or_404(Gastos, id=id)
    gasto.delete()

    return redirect('gastos:gastos')
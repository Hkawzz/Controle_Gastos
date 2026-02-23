from django.shortcuts import render, redirect, get_object_or_404
from .models import Dividas
from .forms import DividasForm

def dividas(request):
    dividas = Dividas.objects.all()

    return render(request, "dividas/index.html", {'dividas': dividas})

def cadastrar_divida(request):
    if request.method == 'POST':
        form = DividasForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('dividas:dividas')
        
    else:
        form = DividasForm()

    return render(request, "dividas/form.html", {'form': form})

def editar_divida(request, id):
    form = get_object_or_404(Dividas, id=id)
    if request.method == 'POST':
        form = DividasForm(request.POST, instance=form)
        if form.is_valid():
            form.save()

            return redirect('dividas:dividas')
        
    else:
        form = DividasForm(instance=form)

    return render(request, "dividas/form.html", {'form': form})

def excluir_divida(request, id):
    form = get_object_or_404(Dividas, id=id)
    form.delete()

    return redirect('dividas:dividas')
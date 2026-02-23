from django.shortcuts import render, redirect, get_object_or_404
from .models import Caixinhas, Dividas
from .forms import CaixinhasForm, DividasForm

def visao_geral(request):
    caixinhas = Caixinhas.objects.all()
    dividas = Dividas.objects.all()

    return render(request, "visao_geral/index.html", {
        'caixinhas': caixinhas,
        'dividas': dividas})

def caixinhas(request):
    caixinhas = Caixinhas.objects.all()

    return render(request, "caixinhas/index.html", {'caixinhas': caixinhas})

def cadastrar_caixinha(request):
    if request.method == 'POST':
        form = CaixinhasForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('financeiro:caixinhas')
        
    else:
        form = CaixinhasForm()

    return render(request, "caixinhas/form.html", {'form': form})

def editar_caixinha(request, id):
    form = get_object_or_404(Caixinhas, id=id)
    if request.method == 'POST':
        form = CaixinhasForm(request.POST, instance=form)
        if form.is_valid():
            form.save()

            return redirect('financeiro:caixinhas')
        
    else:
        form = CaixinhasForm(instance=form)

    return render(request, "caixinhas/form.html", {'form': form})

def excluir_caixinha(request, id):
    form = get_object_or_404(Caixinhas, id=id)
    form.delete()

    return redirect('financeiro:caixinhas')

def dividas(request):
    dividas = Dividas.objects.all()

    return render(request, "dividas/index.html", {'dividas': dividas})

def cadastrar_divida(request):
    if request.method == 'POST':
        form = DividasForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('financeiro:dividas')
        
    else:
        form = DividasForm()

    return render(request, "dividas/form.html", {'form': form})

def editar_divida(request, id):
    form = get_object_or_404(Dividas, id=id)
    if request.method == 'POST':
        form = DividasForm(request.POST, instance=form)
        if form.is_valid():
            form.save()

            return redirect('financeiro:dividas')
        
    else:
        form = DividasForm(instance=form)

    return render(request, "dividas/form.html", {'form': form})

def excluir_divida(request, id):
    form = get_object_or_404(Dividas, id=id)
    form.delete()

    return redirect('financeiro:dividas')
from django.shortcuts import render, redirect, get_object_or_404
from .models import Fixos, Cartao, Caixinhas, Dividas
from .forms import FixosForm, CartaoForm, CaixinhasForm, DividasForm

def visao_geral(request):
    fixos = Fixos.objects.all()
    cartao = Cartao.objects.all()
    caixinhas = Caixinhas.objects.all()
    dividas = Dividas.objects.all()

    return render(request, "visao_geral/index.html", {
        'fixos': fixos,
        'cartao': cartao,
        'caixinhas': caixinhas,
        'dividas': dividas})

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
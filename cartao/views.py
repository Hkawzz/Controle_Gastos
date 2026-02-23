from django.shortcuts import render, redirect, get_object_or_404
from .models import Cartao
from .forms import CartaoForm

def cartao(request):
    cartao = Cartao.objects.all()

    return render(request, "cartao/index.html", {'cartao': cartao})

def cadastrar_cartao(request):
    if request.method == 'POST':
        form = CartaoForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('cartao:cartao')
        
    else:
        form = CartaoForm()

    return render(request, "cartao/form.html", {'form': form})

def editar_cartao(request, id):
    form = get_object_or_404(Cartao, id=id)
    if request.method == 'POST':
        form = CartaoForm(request.POST, instance=form)
        if form.is_valid():
            form.save()

            return redirect('cartao:cartao')
        
    else:
        form = CartaoForm(instance=form)

    return render(request, "cartao/form.html", {'form': form})

def excluir_cartao(request, id):
    form = get_object_or_404(Cartao, id=id)
    form.delete()

    return redirect('cartao:cartao')
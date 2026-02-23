from django.shortcuts import render, redirect, get_object_or_404
from .models import Caixinhas
from .forms import CaixinhasForm

def caixinhas(request):
    caixinhas = Caixinhas.objects.all()

    return render(request, "caixinhas/index.html", {'caixinhas': caixinhas})

def cadastrar_caixinha(request):
    if request.method == 'POST':
        form = CaixinhasForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('caixinhas:caixinhas')
        
    else:
        form = CaixinhasForm()

    return render(request, "caixinhas/form.html", {'form': form})

def editar_caixinha(request, id):
    form = get_object_or_404(Caixinhas, id=id)
    if request.method == 'POST':
        form = CaixinhasForm(request.POST, instance=form)
        if form.is_valid():
            form.save()

            return redirect('caixinhas:caixinhas')
        
    else:
        form = CaixinhasForm(instance=form)

    return render(request, "caixinhas/form.html", {'form': form})

def excluir_caixinha(request, id):
    form = get_object_or_404(Caixinhas, id=id)
    form.delete()

    return redirect('caixinhas:caixinhas')
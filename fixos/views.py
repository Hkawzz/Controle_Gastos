from django.shortcuts import render, redirect, get_object_or_404
from .models import Fixos
from .forms import FixosForm

def fixos(request):
    fixos = Fixos.objects.all()

    return render(request, "fixos/index.html", {'fixos': fixos})


def cadastrar_fixos(request):
    if request.method == 'POST':
        form = FixosForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('fixos:fixos')
        
    else:
        form = FixosForm()

    return render(request, "fixos/form.html", {'form': form})

def editar_fixos(request, id):
    fixo = get_object_or_404(Fixos, id=id)
    if request.method == 'POST':
        form =FixosForm(request.POST, instance=fixo)
        if form.is_valid():
            form.save()

            return redirect('fixos:fixos')
        
    else:
        form = FixosForm(instance=fixo)

    return render(request, "fixos/form.html", {'form': form})

def excluir_fixos(request, id):
    fixo =get_object_or_404(Fixos, id=id)
    fixo.delete()

    return redirect('fixos:fixos')
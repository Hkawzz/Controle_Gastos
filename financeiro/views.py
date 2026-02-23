from django.shortcuts import render

def visao_geral(request):
    return render(request, "visao_geral/index.html")
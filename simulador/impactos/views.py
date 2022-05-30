from django.shortcuts import render
from impactos.models import *
from .form import *
# Create your views here.

def inicio(request):
    cov = Compounds.objects.all()
    contexto = {
        'cov': cov
    }
    return render(request, 'index.html', contexto)


def CrearCompuestos(request):
    form = CompuestoForms()
    contexto = {
        'form': form
    }
    return render(request, 'lista.html', contexto)
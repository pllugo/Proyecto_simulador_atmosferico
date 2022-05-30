from django.views.generic import CreateView, DeleteView, ListView, UpdateView, TemplateView

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .form import *
from impactos.models import *

from impactos.impactos_atm import *

class CompoundsList(ListView):
    model = Compounds
    template_name = 'index.html'


class CompoundCreate(CreateView):
    model = Compounds
    form_class = CompuestoForms
    template_name = 'lista.html'
    success_url = reverse_lazy('index')

class AcidificationCalculation(TemplateView):
    template_name = 'acidification.html'

    def get_context_data(self, **kwargs):
        '''
        Preparamos en nuestro contexto la lista de comics del usuario registrado.
        '''
        context = super().get_context_data(**kwargs)
        # Obtenemos la lista de comics:
        ap_calc = AcidificationCompound.objects.all()
        cov = Compounds.objects.all()
        #(peso_molecular, numero_cloro, numero_fluor, numero_nitrogeno, numero_azufre):
        tiempo = potencial_acidificacion(cov.get('molar_mass'), ap_calc.get('num_cl'), ap_calc.get('num_f'), ap_calc.get('num_n'), ap_calc.get('num_s'))
        return tiempo

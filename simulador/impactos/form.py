from dataclasses import fields
from pyexpat import model
from django import forms

from impactos.models import *

class CompuestoForms(forms.ModelForm):
    class Meta:
        model = Compounds
        fields = '__all__'

class AcidificacionForms(forms.ModelForm):
    class Meta:
        model = AcidificationCompound
        fields = '__all__'
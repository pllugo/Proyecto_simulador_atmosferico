from django.db import models

# NOTE: Para poder utilizar el modelo "user" que viene por defecto en Django,
# Debemos importarlo previamente:

# from django.contrib.auth.models import User

# Create your models here.


class Compounds(models.Model):
     '''
     Esta clase hereda de Django models.Model y crea una tabla llamada
     impactos_compounds. Las columnas toman el nombre especificado de cada objeto.
     '''
     id = models.BigAutoField(db_column='ID', primary_key=True)
     compound_id = models.PositiveIntegerField(
        verbose_name='compound ids', default=1, unique=True)
     name = models.CharField(
        verbose_name='name', max_length=120, default='')
     formula = models.CharField(
        verbose_name='formula', max_length=120, default='')
     description = models.TextField(
         verbose_name='descriptions', default='')
     molar_mass = models.FloatField(
         verbose_name='molar_mass', max_length=5, default=0.00)
     density = models.FloatField(
         verbose_name='density', max_length=5, default=0.00)
     picture = models.URLField(
         verbose_name='pictures', default='')

class Meta:
        '''
        Con "class Meta" podemos definir atributos de nuestras entidades como el nombre de la tabla.
        '''
        db_table = 'impactos_compounds'

def __str__(self):
        '''
        La función __str__ cumple la misma función que __repr__ en SQL Alchemy, 
        es lo que retorna cuando llamamos al objeto.
        '''
        return f'{self.id}'


class AcidificationReference(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)
    name_ref = models.CharField(
        verbose_name='name_ref', max_length=120, default='')
    formula_ref = models.CharField(
        verbose_name='formula_ref', max_length=120, default='')
    ap_ref = models.FloatField(
        verbose_name='ap_ref', max_length=5, default=0.00)
    

    class Meta:
        db_table = 'impactos_acidification'

    def __str__(self):
        return f'{self.name_ref}'

class AcidificationCompound(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)
    compound_id = models.ForeignKey(Compounds,
                                 verbose_name='Compounds',
                                 on_delete=models.DO_NOTHING,
                                 default=1, blank=True
                                 )
    #molar_mass = models.ForeignKey(Compounds,verbose_name='molar_mass',
     #                            on_delete=models.DO_NOTHING,
      #                           default=1, blank=True)
    num_f = models.FloatField(
        verbose_name='num_f', max_length=5, default=0.00)
    num_cl = models.FloatField(
        verbose_name='num_cl', max_length=5, default=0.00)
    num_n = models.FloatField(
        verbose_name='num_n', max_length=5, default=0.00)
    num_s = models.FloatField(
        verbose_name='num_s', max_length=5, default=0.00)
    

    class Meta:
        db_table = 'acidification_compounds'

    def __str__(self):
        return f'{self.id}'
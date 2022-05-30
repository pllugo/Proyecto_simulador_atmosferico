#!/usr/bin/env python
'''
Impactos Ambientales
---------------------------
Autor: Pedro Luis Lugo Garcia
Version: 1.0
 
Descripcion:
Programa creado para calcular los diferentes impactos
como son: AP, POCP y tiempo de residencia de un COV en la atmosfera.
'''

__author__ = "Pedro Luis Lugo Garcia"
__email__ = "pedro.lugo@unc.edu.ar"
__version__ = "1.0"

#from app import potencial_odp
#import parametros_ozono
import math
#import parametros_acidificacion
#import compuestos

#Función para calcular el POCP


#Función para calcular el AP de un COV
def potencial_acidificacion(peso_molecular, numero_cloro, numero_fluor, numero_nitrogeno, numero_azufre):
    potencial_ap = round((64.066 / peso_molecular) * (numero_cloro + numero_fluor + numero_nitrogeno + 2 * numero_azufre) / 2, 2)
    
    return potencial_ap

#Función para calcular el AP de un acido carboxilico hidrogenado




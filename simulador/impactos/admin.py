from django.contrib import admin

# NOTE: Tenemos que importar los modelos con los que vamos a trabajar:
from impactos.models import *

# Register your models here.

# NOTE: Aquí personalizamos los campos en el Django Admin.

@admin.register(Compounds)
class CompoundsAdmin(admin.ModelAdmin):
    # pass
    # NOTE: Para seleccionar los campos en la tabla de registros
    list_display = ('compound_id', 'name', 'formula', 'molar_mass', 'density')

    # NOTE: Filtro lateral de elementos:
    list_filter= ('compound_id','name')
    
    # NOTE: Buscador de elementos en la columna:
    search_fields = ['name']

    # NOTE: Para seleccionar los campos en el registro. 
    #fields = ('compound_id', 'name', 'formula')

    # NOTE: Genera un campo desplegable con los registros seleccionados.
    fieldsets = (
        (None, {
            'fields': ('compound_id', 'name', 'formula')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('description','molar_mass', 'density'),
        }),
    )


@admin.register(AcidificationReference)
class acidificationAdmin(admin.ModelAdmin):
    list_display = ('name_ref', 'formula_ref', 'ap_ref')

@admin.register(AcidificationCompound)
class acidificationCompoundAdmin(admin.ModelAdmin):
    list_display = ('compound_id', 'num_f', 'num_cl', 'num_n', 'num_s')
    
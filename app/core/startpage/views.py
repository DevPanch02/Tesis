from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.views.generic import ListView, TemplateView
from requests import Response
from .resources import PersonResource
from tablib import Dataset

from django.views.generic.base import TemplateView

from .models import *
from .forms import *

# Create your views here.
class TemplateListPersons(TemplateView):
    template_name="datatable/table.html"


    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['title']='Listado de usuarios'
        return context




def home(request):
    return render(request,'index.html')

#   IMPORT FILE EXCEL (XLS)
def import_files(request):
    if request.method == 'POST':
        person_resource=PersonResource()
        dataset=Dataset()
        new_person=request.FILES['myfile']

        if not (new_person.name.endswith('xls') or new_person.name.endswith('xlsx')):
            messages.info(request,'FORMATO INCORRECTO')
            return render(request,'index.html')
        

        imported_data=dataset.load(new_person.read(),format='xls')
        for data in imported_data:
            """ value=Person(
                data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],
                data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15],
                data[16],data[17]
            ) """

            persona = Person()
            persona.anio_tit = data[0]
            persona.num_reg = int(data[1])
            persona.RUC = data[2]
            persona.nombrecomercial = data[3]
            persona.razonsocial = data[4]
            persona.calleprincipal = data[5]
            persona.numerocasa = data[6]
            persona.callesecundaria = data[7]
            persona.sector = data[8]
            persona.patrimonio = data[9]
            persona.ced_ruc_representante = data[10]
            persona.nombrerepresentante = data[11]
            persona.apellidorepresentante = data[12]
            persona.negociotipo = data[13]
            persona.describenegocio = data[14]
            persona.rubro_pagado = data[15]
            persona.valorpagar = data[16]
            persona.fechpago = data[17]
            persona.estadotitulo = data[18]
            persona.fecharuc = data[19]
            persona.fecharegmunicipio = data[20]
            persona.abiertocerrado = data[21]
            persona.fechacierre = data[22]
            persona.canton_ruc = data[23]
            persona.provincia_ruc = data[24]


            persona.save()
            
        messages.success(request,"Datos cargados")



    return render(request,'files/import.html')


#   IMPORTED TIP OF DATA

def filter_adjudicacion(request):
    listadoAdjudicacion=Person.objects.filter(rubro_pagado='ADJUDICACION DE ENTE PUBLICO A PERSONA NATURAL')
    return render(request,'files/import.html', {"persons":listadoAdjudicacion} )

def filter_interes(request):
    listadoInteres=Person.objects.filter(rubro_pagado='INTERES TRIBUTARIO')
    data={
        "persons":listadoInteres
    }
    return render(request,'files/import.html',data)

def filter_patente(request):
    data={
        'persons':Person.objects.filter(rubro_pagado='PATENTE ANUAL')
    }
    return render(request,'files/import.html',data)

def filter_adm_patente(request):
    data={
        'persons':Person.objects.filter(rubro_pagado='SER. ADM. PATENTE')
    }
    return render(request,'files/import.html',data)

def filter_tercera_edad(request):
    data={
        'persons':Person.objects.filter(rubro_pagado='TERCERA EDAD')
    }
    return render(request,'files/import.html',data)

#   LIST DATA

#   IMPORTED TIP OF DATA
def filter_adjudicacion1(request):
    listadoAdjudicacion=Person.objects.filter(rubro_pagado='ADJUDICACION DE ENTE PUBLICO A PERSONA NATURAL')
    return render(request,'datatable/table.html', {"persons":listadoAdjudicacion} )

def filter_interes1(request):
    listadoInteres=Person.objects.filter(rubro_pagado='INTERES TRIBUTARIO')
    data={
        "persons":listadoInteres
    }
    return render(request,'datatable/table.html',data)

def filter_patente1(request):
    data={
        'persons':Person.objects.filter(rubro_pagado='PATENTE ANUAL')
    }
    return render(request,'datatable/table.html',data)

def filter_adm_patente1(request):
    data={
        'persons':Person.objects.filter(rubro_pagado='SER. ADM. PATENTE')
    }
    return render(request,'datatable/table.html',data)

def filter_tercera_edad1(request):
    data={
        'persons':Person.objects.filter(rubro_pagado='TERCERA EDAD')
    }
    return render(request,'datatable/table.html',data)


from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('import/', import_files, name='import'),

    path('list_persons/', TemplateListPersons.as_view(), name='list_persons'),


    #   DOCUMENTS
    path('adjudicacion/', filter_adjudicacion, name='adjudicacion'),
    path('interes/', filter_interes, name='interes'),
    path('patente/', filter_patente, name='patente'),   
    path('adm_patente/', filter_adm_patente, name='adm_patente'),   
    path('tercera_edad/', filter_tercera_edad, name='tercera_edad'),   


    #   LIST DATA
    path('adjudicacion/adjudicacion_list/', filter_adjudicacion1, name='adjudicacion_list'),
    path('interes/interes_list/', filter_interes1, name='interes_list'),
    path('patente/patente_list/', filter_patente1, name='patente_list'),   
    path('adm/adm_patente_list/', filter_adm_patente1, name='adm_patente_list'),   
    path('tercera_edad/tercera_edad_list/', filter_tercera_edad1, name='tercera_edad_list'),  

      

]

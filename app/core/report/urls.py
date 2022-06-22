from django.urls import path, include
from .views import *

urlpatterns = [
    path('report/', viewData, name='report'),

]
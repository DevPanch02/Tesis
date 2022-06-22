from turtle import mode
from django.db import models

class Page(models.Model):
    image_page = models.ImageField(upload_to='start_page/%Y', null=True, blank=True, verbose_name="Imagen de portada")
    description=models.TextField(verbose_name="Descripcion de la institucion")
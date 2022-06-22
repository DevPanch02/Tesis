from django.shortcuts import render
from django.urls import reverse_lazy
from core.page.models import Page
from core.page.forms import PageForm
from django.views.generic import  CreateView, UpdateView,ListView
from django.views.generic.base import TemplateView

class TemplatePage(TemplateView):
    template_name="home.html"


class CreatePage(CreateView):
    model=Page
    template_name="create_page.html"
    form_class=PageForm
    success_url=reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['title']="PAGINA INICIO"
        return context


class ListPage(ListView):
    model=Page
    template_name="index.html"
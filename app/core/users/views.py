from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.users.mixins import ValidatePermissionRequiredMixin
from core.users.models import User
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from core.users.forms import UserForm
import json



class listarUsuarios(ListView):
    model = User
    template_name = 'list_user.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Usuarios'
        context['create_url'] = reverse_lazy('users:user_create')
        return context

class UserCreateView( CreateView):
    model = User
    template_name = 'create_user.html'
    form_class = UserForm
    success_url = reverse_lazy('users:user_list')
    permission_required = 'add_user'
    def validate_data(self):
            data = {'valid': True}
            try:
                type = self.request.POST['type']
                obj = self.request.POST['obj'].strip()
                if type == 'dni':
                    if User.objects.filter(dni=obj):
                        data['valid'] = False
                elif type == 'username':
                    if User.objects.filter(username__icontains=obj):
                        data['valid'] = False
                elif type == 'email':
                    if User.objects.filter(email=obj):
                        data['valid'] = False
            except:
                pass
            return JsonResponse(data)


    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        try:
            if action == 'add':
                data = self.get_form().save()
            elif action == 'validate_data':
                return self.validate_data()
            else:
                data['error'] = 'No ha seleccionado ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['list_url'] = self.success_url
        context['title'] = 'Nuevo registro de un Usuario'
        context['action'] = 'add'
        return context

class UserUpdateView(UpdateView):
    model = User
    template_name = 'create_user.html'
    form_class = UserForm
    success_url = reverse_lazy('users:user_list')
    permission_required = 'add_user'
    def validate_data(self):
            data = {'valid': True}
            try:
                type = self.request.POST['type']
                obj = self.request.POST['obj'].strip()
                if type == 'dni':
                    if User.objects.filter(dni=obj):
                        data['valid'] = False
                elif type == 'username':
                    if User.objects.filter(username__icontains=obj):
                        data['valid'] = False
                elif type == 'email':
                    if User.objects.filter(email=obj):
                        data['valid'] = False
            except:
                pass
            return JsonResponse(data)


    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        try:
            if action == 'add':
                data = self.get_form().save()
            elif action == 'validate_data':
                return self.validate_data()
            else:
                data['error'] = 'No ha seleccionado ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['list_url'] = self.success_url
        context['title'] = 'Nuevo registro de un Usuario'
        context['action'] = 'add'
        return context

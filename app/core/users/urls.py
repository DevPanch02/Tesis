from django.urls import path
from core.users.views import *

app_name = 'users'

urlpatterns = [
    # user

    path('list-user/', listarUsuarios.as_view(), name='user_list'),
    path('add-user/', UserCreateView.as_view(), name='user_create'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),


]
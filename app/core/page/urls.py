from django.urls import path
from core.page.views import *


urlpatterns = [
    # user

    path('start-page/', TemplatePage.as_view(), name='start_page'),
    path('create-page/', CreatePage.as_view(), name='page_create'),
    

    # path('add-user/', UserCreateView.as_view(), name='user_create'),


]
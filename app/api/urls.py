from .user.views import PersonViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()

router.register(r'Person', PersonViewSet, basename='Person')

urlpatterns = [

    path('', include(router.urls), name="ViewApi"),
]
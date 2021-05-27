from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='needToKnow'),
    path('<str:slug>', view_know, name="view_know"),
]

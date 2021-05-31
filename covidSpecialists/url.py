from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='covidSpecialists'),
    path('<str:slug>/', view_covid, name="view_covid"),
]
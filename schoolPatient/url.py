from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='schoolPatient'),
    path('sanatoriums/', sanatoriums, name='sanatoriums'),
    path('sanatoriums/<int:sanatorium_id>/', view_sanatorium, name="view_sanatorium"),

]
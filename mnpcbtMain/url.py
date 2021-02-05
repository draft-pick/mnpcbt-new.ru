from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='main'),
    path('/category/<str:slug>', get_category, name='category'),
]

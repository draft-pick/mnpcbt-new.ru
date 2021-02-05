from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='schoolNurses'),
    path('categories/<str:slug>', get_category_school_nurses, name="category_school_nurses"),
]

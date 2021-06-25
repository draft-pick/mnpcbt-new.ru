from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='schoolNurses'),
    path('categories/<str:slug>', get_category_school_nurses, name="category_school_nurses"),
    path('schoolNursesApp/periods/', periods_app, name="periods_app"),
    path('schoolNursesApp/period_detail/<int:period_app_id>', period_app_detail, name="period_app_detail"),
]

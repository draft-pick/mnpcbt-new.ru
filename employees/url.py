from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='employees'),
    path('<int:employee_id>/', view_employee, name="view_employee"),
]
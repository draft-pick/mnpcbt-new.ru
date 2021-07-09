from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='schoolNursesApp'),
    path('periods/<int:app_period_id>', app_period_view, name='app_period_view'),
    path('periods/<int:app_period_id>/<int:app_management_id>', app_management_view, name='app_management_view'),
]
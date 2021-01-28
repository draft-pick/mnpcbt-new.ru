from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('category/<str:slug>', get_category, name="category"),
]

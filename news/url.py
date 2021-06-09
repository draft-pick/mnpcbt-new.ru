from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='news'),
    path('<str:slug>', view_news, name="view_news"),
]

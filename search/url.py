from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.SearchView.as_view(), name='search'),
]
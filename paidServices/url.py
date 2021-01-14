from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='paidServices'),
    path('<int:pscategory_id>/', view_psupcat, name="view_psupcat"),
    path('<int:pscategory_id>/<int:service_id>/', view_service, name="view_service"),
]

from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='trainingNurses'),
    path('<int:contract_nurses_id>', contract_nurses_view, name='contract_nurses_view'),
    path('<int:contract_nurses_id>/<int:type_org>/<int:period_nurses_id>/<int:management_nurses_id>',
         management_nurses_view,
         name='management_nurses_view'),
    path('delete/<int:person_id>', delete_person, name='delete_person'),

    path('trainingNursesAdmin/', admin_index, name='admin_index'),
    path('trainingNursesAdmin/<int:period_nurses_id>', admin_period_view, name='admin_period_view'),
    path('trainingNursesAdmin/<int:period_nurses_id>/printList', list_credits, name='list_credits')
]

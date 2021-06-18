from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='regConf'),
    # path('management/', all_list, name='all_list'),
    # path('management/user/<int:reg_id>/', view_reg, name="view_reg"),
    # path('management/school_1/', school_1, name="school_1"),
    # path('management/school_2/', school_2, name="school_2"),
    # path('management/school_3/', school_3, name="school_3"),
    # path('management/school_4/', school_4, name="school_4"),
    # path('management/school_5/', school_5, name="school_5"),

]

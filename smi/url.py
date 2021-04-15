from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='smi'),
    path('article/', smi_article, name='smi_article'),
    # path('<int:news_id>/', view_news, name="view_news"),
]

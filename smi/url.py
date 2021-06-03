from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='smi'),
    path('article/', smi_article, name='smi_article'),
    path('videoclips/', smi_videoclips, name='smi_videoclips'),
    # path('<int:news_id>/', view_news, name="view_news"),
]

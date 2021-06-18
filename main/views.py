from django.shortcuts import render
from .models import *
from news.models import News, GalleryNews
from structure.models import Branches, GalleryBranches
from reviews.models import Reviews
from implink.models import ImpLink
from employees.models import Employees
from needToKnow.models import Know


def index(request):
    news = News.objects.order_by("-created_at")[1:6]
    news_last = News.objects.order_by("-created_at")[0:1]
    branches = Branches.objects.all()
    image_branches = Branches.objects.all()
    reviews = Reviews.objects.all()
    implinks = ImpLink.objects.all()
    employees = Employees.objects.all()
    degree_candidate = employees.filter(degree='Кандидат медицинских наук').count()
    degree_doctor = employees.filter(degree='Доктор медицинских наук').count()
    mos_doc = employees.filter(mos_doc="Московский врач").count()
    count_list = employees.count()
    need_to_know = Know.objects.filter(anons=1)
    context = {
        'news_last': news_last,
        'news': news,
        'branches': branches,
        'image_branches': image_branches,
        'reviews': reviews,
        'implinks': implinks,
        'employees': employees,
        'degree_candidate': degree_candidate,
        'degree_doctor': degree_doctor,
        'mos_doc': mos_doc,
        'count_list': count_list,
        'need_to_know': need_to_know,
        'title': 'Главная страница',
    }
    return render(request, 'main/index.html', context=context)

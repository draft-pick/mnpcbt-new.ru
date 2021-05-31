from .models import *
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    covid = Covid.objects.all()
    p = Paginator(covid, 10)
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    context = {
        'covid': page,
        'title': 'Специалистам COVID-19',
    }
    return render(request, 'covidSpecialists/index.html', context=context)


def view_covid(request, slug):
    covid_item = Covid.objects.get(slug=slug)
    context = {
        'title': covid_item.title,
        "covid_item": covid_item,
    }
    return render(request, 'covidSpecialists/view_covid.html', context=context)

from django.shortcuts import render
from .models import *


def index(request):
    # news = News.objects.order_by('-created_at')
    # image = GalleryNews.objects.all()
    context = {
        # 'news': news,
        # 'image': image,
        'title': 'Школа пациента',
    }
    return render(request, 'schoolPatient/index.html', context=context)


def sanatoriums(request):
    san = Sanatoriums.objects.all()
    context = {
        'san': san,
        'title': 'Противотуберкулезные санатории',
    }
    return render(request, 'schoolPatient/sanatoriums.html', context=context)


def view_sanatorium(request, sanatorium_id):
    san_item = Sanatoriums.objects.get(pk=sanatorium_id)
    context = {
        'title': san_item.title,
        "san_item": san_item,
    }
    return render(request, 'schoolPatient/view_sanatorium.html', context=context)

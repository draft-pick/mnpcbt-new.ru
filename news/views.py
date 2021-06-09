from django.shortcuts import render
from .models import *


def index(request):
    news = News.objects.order_by('-created_at')
    image = GalleryNews.objects.all()
    context = {
        'news': news,
        'image': image,
        'title': 'Наши новости',
    }
    return render(request, 'news/index.html', context=context)


def view_news(request, slug):
    news_item = News.objects.get(slug=slug)
    context = {
        'title': news_item.title,
        "news_item": news_item,
    }
    return render(request, 'news/view_news.html', context=context)

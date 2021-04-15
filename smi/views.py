from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    context = {
        'title': 'СМИ о нас',
    }
    return render(request, 'smi/index.html', context=context)


def smi_article(request):
    articles = smiArticles.objects.all().order_by('-created_at')
    p = Paginator(articles, 9)
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    # paginator = Paginator(articles, 1)
    # page = request.GET.get('page', 1)
    # try:
    #     posts = paginator.page(page)
    # except PageNotAnInteger:
    #     posts = paginator.page(1)
    # except EmptyPage:
    #     posts = paginator.page(paginator.num_pages)
    context = {
        'articles': page,
        # 'page': page,
        # 'posts': posts,
        'title': 'Статьи',
    }
    return render(request, 'smi/article.html', context=context)




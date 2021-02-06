from django.shortcuts import render
from .models import *


def index(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'title': 'Дополнительное образование для медицинских сестер',
    }
    return render(request, 'schoolNurses/index.html', context=context)


def get_category_school_nurses(request, slug):
    category = Category.objects.get(slug=slug)
    children = category.get_children()
    return render(request, "schoolNurses/category.html", {"category": category,
                                                          "children": children,
                                                          "title": category,
                                                          "categories": Category.objects.all()})

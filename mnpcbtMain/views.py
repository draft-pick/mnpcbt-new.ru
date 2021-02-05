from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import *
from news.models import News, GalleryNews
from structure.models import Branches, GalleryBranches
from reviews.models import Reviews
from implink.models import ImpLink


def index(request):
    return render(request, "mnpcbtMain/index.html", {'categories': Category.objects.all()})


def get_category(request, slug):
    category = Category.objects.get(slug=slug)
    return render(request, "mnpcbtMain/category.html", {"category": category, 'categories': Category.objects.all()})

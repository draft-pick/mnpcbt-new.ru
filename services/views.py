from django.shortcuts import render
from .models import Category, Services


def home(request):
    return render(request, "services/index.html", {'categories': Category.objects.all()})


def get_category(request, slug):
    category = Category.objects.get(slug=slug)
    ancestors = category.get_ancestors()
    descendants = category.get_descendants(include_self=False)
    children = category.get_children()

    services = Services.objects.filter(category__slug=slug)

    return render(request, "services/category.html", {"category": category,
                                                      "categories": Category.objects.all(),
                                                      "services": services,
                                                      "descendants": descendants,
                                                      "ancestors": ancestors,
                                                      "children": children})

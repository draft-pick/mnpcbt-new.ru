from django.shortcuts import render, HttpResponse
from .models import *
from .form import registrationForm, managementForm, periodsForm


def index(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'title': 'Дополнительное образование для медицинских сестер',
    }
    return render(request, 'schoolNurses/index.html', context=context)


def get_category_school_nurses(request, slug):
    category = Category.objects.get(slug=slug)
    return render(request, "schoolNurses/category.html", {"category": category,
                                                          "title": category,
                                                          "categories": Category.objects.all()})


def periods_app(request):
    all_periods = periods.objects.all()
    context = {
        'title': 'Периоды обучения',
        'all_periods': all_periods
    }
    return render(request, 'schoolNurses/app/index.html', context=context)


def period_app_detail(request, period_app_id):
    period_detail = periods.objects.get(pk=period_app_id)
    initial_dict = {
        "man_key_periods": period_app_id,
    }
    form_management = managementForm(request.POST or None, initial=initial_dict)
    if form_management.is_valid():
        form_management.save()
        return HttpResponse("Saved.")
    context = {
        'period_detail': period_detail,
        'form_management': form_management,
    }
    return render(request, 'schoolNurses/app/success.html', context=context)



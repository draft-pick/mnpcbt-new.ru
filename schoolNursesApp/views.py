from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from .models import periodsApp, contractsApp, managementApp
from .form import periodsAppForm, contractsAppForm, managementAppForm, otherAppForm


def index(request):
    all_periods = periodsApp.objects.all()
    context = {
        'title': 'Периоды обучения',
        'all_periods': all_periods
    }
    return render(request, 'schoolNursesApp/index.html', context=context)


def app_period_view(request, app_period_id):
    view_period = periodsApp.objects.get(pk=app_period_id)
    initial_dict = {
        'man_key_periods': app_period_id,
    }
    form_management = managementAppForm(request.POST or None, initial=initial_dict)
    if form_management.is_valid():
        form_management = form_management.save()
        app_management_id = form_management.pk
        return redirect('app_management_view', app_period_id, app_management_id)
    context = {
        'title': view_period.start_date - view_period.end_date,
        'view_period': view_period,
        'form_management': form_management
    }
    return render(request, 'schoolNursesApp/view_period.html', context=context)


def app_management_view(request, app_period_id, app_management_id):
    form_other = otherAppForm(request.POST or None)
    if form_other.is_valid():
        form_other.save()
        return redirect('app_management_view', app_period_id, app_management_id)
    context = {
        'form_other': form_other
    }
    return render(request, 'schoolNursesApp/registration.html', context=context)

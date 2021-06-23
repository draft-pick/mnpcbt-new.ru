from .models import *
from .form import regSurnameForm, regNameForm, regPatronymicForm, regOtherForm
from django.shortcuts import render
from django.db.models import F, Value
from django.db.models.functions import Concat


def index(request):
    if request.method == "GET":
        form_surname = regSurnameForm
        form_name = regNameForm
        form_patronymic = regPatronymicForm
        form_other = regOtherForm
        return render(request, 'regConf/index.html', {'form_surname': form_surname,
                                                      'form_name': form_name,
                                                      'form_patronymic': form_patronymic,
                                                      'form_other': form_other,
                                                      })
    elif request.method == "POST":
        form_surname = regSurnameForm(request.POST)
        form_name = regNameForm(request.POST)
        form_patronymic = regPatronymicForm(request.POST)
        form_other = regOtherForm(request.POST)
        if form_surname.is_valid() and form_name.is_valid() and form_patronymic.is_valid() and form_other.is_valid():
            form_surname = form_surname.save()
            form_name = form_name.save(commit=False)
            form_patronymic = form_patronymic.save(commit=False)
            form_other = form_other.save(commit=False)
            form_name.surname_key = form_surname
            form_name.save()

            form_patronymic.name_key = form_name
            form_patronymic.save()

            form_other.name_patronymic = form_patronymic
            form_other.save()

            user_name = form_name.name
            user_patronymic = form_patronymic.patronymic
            return render(request, 'regConf/success.html', {'user_name': user_name,
                                                            'user_patronymic': user_patronymic,
                                                            'form_surname': form_surname})


def all_list(request):
    school = schoolName.objects.all()
    surname = regSurname.objects.all()
    name = regName.objects.select_related().all()
    patronymic = regPatronymic.objects.select_related().all()
    other = regOther.objects.select_related().all()
    context = {
        'school': school,
        'surname': surname,
        'name': name,
        'patronymic': patronymic,
        'other': other
    }
    return render(request, 'regConf/all_list.html', context=context)


def view_school(request, school_id):
    school_item = schoolName.objects.get(pk=school_id)
    surname_item = regSurname.objects.filter(school_key=school_id)
    name_item = regName.objects.filter(surname_key__school_key=school_id)
    patronymic_item = regPatronymic.objects.filter(name_key__surname_key__school_key=school_id)
    qs = regSurname.objects.filter(school_key=school_id).annotate(
        full_name=Concat(F('surname'), Value(' '), F('regsurname__name'), Value(' '),
                         F('regsurname__patronymic__patronymic')))
    context = {
        'title': school_item.title,
        'school_item': school_item,
        'surname_item': surname_item,
        'name_item': name_item,
        'patronymic_item': patronymic_item,
        'qs': qs,
    }
    return render(request, 'regConf/view_school.html', context=context)

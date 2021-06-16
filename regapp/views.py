from .models import *
from .form import RegistrationForm
from django.shortcuts import render


def index(request):
    if request.method == "GET":
        form = RegistrationForm()
        return render(request, 'regapp/index.html', {'form': form})
    elif request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_name = user.name
            user_patronymic = user.patronymic
            user_school = user.school
            return render(request, 'regapp/success.html', {'user_name': user_name,
                                                           'user_patronymic': user_patronymic,
                                                           'user_school': user_school})
        return render(request, 'regapp/index.html', {'form': form,
                                                     'title': 'Отрыть новый период',
                                                     })


def all_list(request):
    users = Registration.objects.all()
    school_1 = Registration.objects.filter(school__contains='Без посещения')
    school_2 = Registration.objects.filter(
        school__contains='Перспективы лечения больных туберкулезом в ближайшие десятилетия')
    school_3 = Registration.objects.filter(
        school__contains='Современные методы этиологической диагностики микобактериальной инфекции')
    school_4 = Registration.objects.filter(
        school__contains='Особенности профилактики и лечения детского туберкулеза в мегаполисе')
    school_5 = Registration.objects.filter(
        school__contains='Организация работы среднего медицинского персонала в период пандемии')
    context = {
        'users': users,
        'school_1': school_1,
        'school_2': school_2,
        'school_3': school_3,
        'school_4': school_4,
        'school_5': school_5,
    }
    return render(request, 'regapp/management/all_list.html', context=context)


def view_reg(request, reg_id):
    user_item = Registration.objects.get(pk=reg_id)
    context = {
        'title': user_item.surname,
        'user_item': user_item,
    }
    return render(request, 'regapp/management/user_detail.html', context=context)


def school_1(request):
    school_1 = Registration.objects.filter(school__contains='Без посещения')
    return render(request, 'regapp/management/school_1.html', {'school_1': school_1})


def school_2(request):
    school_2 = Registration.objects.filter(
        school__contains='Перспективы лечения больных туберкулезом в ближайшие десятилетия')
    return render(request, 'regapp/management/school_2.html', {'school_2': school_2})


def school_3(request):
    school_3 = Registration.objects.filter(
        school__contains='Современные методы этиологической диагностики микобактериальной инфекции')
    return render(request, 'regapp/management/school_3.html', {'school_3': school_3})


def school_4(request):
    school_4 = Registration.objects.filter(
        school__contains='Особенности профилактики и лечения детского туберкулеза в мегаполисе')
    return render(request, 'regapp/management/school_4.html', {'school_4': school_4})


def school_5(request):
    school_5 = Registration.objects.filter(
        school__contains='Организация работы среднего медицинского персонала в период пандемии')
    return render(request, 'regapp/management/school_5.html', {'school_5': school_5})
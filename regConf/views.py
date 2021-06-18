from .models import *
from .form import regSurnameForm, regNameForm, regPatronymicForm
from django.shortcuts import render


def index(request):
    if request.method == "GET":
        form_surname = regSurnameForm
        form_name = regNameForm
        form_patronymic = regPatronymicForm
        return render(request, 'regConf/index.html', {'form_surname': form_surname,
                                                      'form_name': form_name,
                                                      'form_patronymic': form_patronymic,
                                                      })
    elif request.method == "POST":
        form_surname = regSurnameForm(request.POST)
        form_name = regNameForm(request.POST)
        form_patronymic = regPatronymicForm(request.POST)
        if form_surname.is_valid() and form_name.is_valid() and form_patronymic.is_valid():
            form_surname = form_surname.save()
            form_name = form_name.save(commit=False)
            form_patronymic = form_patronymic.save(commit=False)

            form_name.surname_key = form_surname
            form_name.save()

            form_patronymic.name_key = form_name
            form_patronymic.save()

            user_name = form_name.name
            user_patronymic = form_patronymic.patronymic
            return render(request, 'regConf/success.html', {'user_name': user_name,
                                                            'user_patronymic': user_patronymic,
                                                            'form_surname': form_surname})

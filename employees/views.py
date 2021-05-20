from django.db.models.query_utils import Q
from django.shortcuts import render

from .form import LocationChoiceField
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .utils import get_plot
from structure.models import Branches


def index(request):
    branches = Branches.objects.all()
    employees = Employees.objects.all()
    # x = [5]
    # y = [10]
    # chart = get_plot(x, y)
    p = Paginator(employees, 72)
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    degree_candidate = employees.filter(degree='Кандидат мед. наук').count()
    degree_doctor = employees.filter(degree='Доктор мед. наук').count()
    mos_doc = employees.filter(mos_doc="Московский врач")
    count_list = employees.count()
    context = {
        'employees': page,
        'title': 'Сотрудники',
        'degree_candidate': degree_candidate,
        'degree_doctor': degree_doctor,
        'mos_doc': mos_doc,
        'count_list': count_list,
        'branches': branches,
    }
    return render(request, 'employees/index.html', context=context)


def view_employee(request, employee_id):
    employee_item = Employees.objects.get(pk=employee_id)
    context = {
        'surname': employee_item.surname,
        'name': employee_item.name,
        'patronymic': employee_item.patronymic,
        "employee_item": employee_item,
    }
    return render(request, 'employees/detail.html', context=context)

from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import *
from .form import registrationForm, managementForm, periodsForm, contractsForm
from django.db.models import Count, Max
from docxtpl import DocxTemplate, Document
from django import forms


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
    contracts_list = contracts.objects.filter(key_periods=period_app_id)
    management_list = management.objects.filter(man_key_periods=period_app_id)
    reg_list = form_registration.objects.filter(reg_key_periods=period_app_id)

    initial_dict = {
        "man_key_periods": period_app_id,
        "reg_key_periods": period_app_id,
    }

    form_management = managementForm(request.POST or None, initial=initial_dict)
    form_reg = registrationForm(request.POST or None, initial=initial_dict)
    if form_reg.is_valid():
        form_management = form_management.save()
        form_reg = form_reg.save(commit=False)
        form_reg.reg_key_management = form_management
        form_reg.reg_key_periods = form_management.man_key_periods
        form_reg.reg_key_contract = form_management.man_key_contracts
        form_reg.save()
        return HttpResponse("Saved.")
    context = {
        'period_detail': period_detail,
        'form_management': form_management,
        'contracts_list': contracts_list,
        'management_list': management_list,
        'reg_list': reg_list,
        'form_reg': form_reg,
        'managementForm': managementForm,
    }
    return render(request, 'schoolNurses/app/period_detail.html', context=context)


def print_list(request, period_app_id):
    period_detail = periods.objects.filter(pk=period_app_id)
    management_item = management.objects.filter(man_key_periods=period_app_id)
    _management_item = dict()
    for item in management_item:
        if item.title not in _management_item:
            _management_item[item.title] = item
    management_item = _management_item.values()
    num_student = 0
    student_item = form_registration.objects.filter(reg_key_periods=period_app_id)
    management_set = management.objects.annotate(num_students=Count('reg_management_fk')).filter(
        man_key_periods=period_app_id)
    contract_set = contracts.objects.annotate(num_students=Count('reg_contract_fk')).filter(
        key_periods=period_app_id).distinct()
    doc = DocxTemplate("media/schoolNurses/whole_list.docx")
    for p in period_detail:
        start_date = p.start_date.strftime('%d.%m.%Y')
        end_date = p.end_date.strftime('%d.%m.%Y')
        context = {
            'student_item': student_item,
            'management_item': management_item,
            'management_set': management_set,
            'start_date': start_date,
            'end_date': end_date,
            'contract_set': contract_set,
            'num_student': num_student,
        }
        doc.render(context)
        doc.save("media/generated_whole_list.docx")
        return render(request, 'schoolNurses/app/success.html', context=context)

    # response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    # response['Content-Disposition'] = 'attachment; filename=media/generated_whole_list.docx'
    # doc.save(response)

from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from .models import *
from .form import *
from django.db.models import Q
from docxtpl import DocxTemplate, Document
from django.db.models import Count, Max


def index(request):
    search_query = request.GET.get('search', '')
    contracts = contractsNurses.objects.filter(Q(title__icontains=search_query))
    period_view = periodsNurses.objects.all()
    context = {
        'title': 'Школа медицинских сестер',
        'contracts': contracts,
        'search_query': search_query,
        'period_view': period_view,
    }
    return render(request, 'trainingNurses/index.html', context=context)


def contract_nurses_view(request, contract_nurses_id):
    contract_view = contractsNurses.objects.get(pk=contract_nurses_id)
    type_fiz = request.GET.get('fiz', '')
    type_org = request.GET.get('uch_org', '')
    initial_dict = {
        'man_key_contracts': contract_nurses_id,
        'per_key_contract': contract_nurses_id,
    }
    management_form = managementNursesForm(request.POST or None, initial=initial_dict)
    if management_form.is_valid():
        management_form = management_form.save()
        management_nurses_id = management_form.pk
        period_nurses_id = management_form.man_key_periods.pk
        return redirect('management_nurses_view', contract_nurses_id, type_org, period_nurses_id, management_nurses_id)

    person_form = personNursesForm(request.POST or None, initial=initial_dict)
    if person_form.is_valid():
        person_form = person_form.save()
        # name_pf = person_form.name
        # patronymic_pf = person_form.patronymic
        return HttpResponse('Saved')
    context = {
        'contract_view': contract_view,
        'type_fiz': type_fiz,
        'type_org': type_org,
        'management_form': management_form,
        'person_form': person_form,
    }
    return render(request, 'trainingNurses/test.html', context=context)


def management_nurses_view(request, contract_nurses_id, type_org, period_nurses_id, management_nurses_id):
    management_view = managementNurses.objects.get(pk=management_nurses_id)
    contract_view = contractsNurses.objects.get(pk=contract_nurses_id)
    period_view = periodsNurses.objects.get(pk=period_nurses_id)
    persons = personNurses.objects.filter(per_key_management=management_nurses_id)
    type_org = type_org
    initial_dict = {
        'per_key_period': period_nurses_id,
        'per_key_contract': contract_nurses_id,
        'per_key_management': management_nurses_id,
    }
    person_form = personNursesForm(request.POST or None, initial=initial_dict)
    if person_form.is_valid():
        person_form.save()
        return redirect('management_nurses_view', contract_nurses_id, type_org, period_nurses_id, management_nurses_id)
    return render(request, 'trainingNurses/person.html', {'person_form': person_form,
                                                          'persons': persons,
                                                          'management_view': management_view,
                                                          'contract_view': contract_view,
                                                          'period_view': period_view,
                                                          'type_org': type_org
                                                          })


def delete_person(request, person_id):
    person_del = personNurses.objects.get(pk=person_id)
    person_del.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def admin_index(request):
    period_view = periodsNurses.objects.all()
    return render(request, 'trainingNurses/admin/index.html', {'period_view': period_view})


def admin_period_view(request, period_nurses_id):
    period_view = periodsNurses.objects.get(pk=period_nurses_id)
    persons = personNurses.objects.filter(per_key_period=period_nurses_id)
    return render(request, 'trainingNurses/admin/period_view.html', {'period_view': period_view,
                                                                     'persons': persons, })


def list_credits(request, period_nurses_id):
    period_view = periodsNurses.objects.filter(pk=period_nurses_id)
    management_view = managementNurses.objects.filter(man_key_periods=period_nurses_id)
    person_view = personNurses.objects.filter(per_key_period=period_nurses_id)
    num_person = 0
    management_set = managementNurses.objects.annotate(num_students=Count('per_managementNurses_fk')).filter(
        man_key_periods=period_nurses_id)
    # contract_set = contracts.objects.annotate(num_students=Count('reg_contract_fk')).filter(
    #     key_periods=period_app_id).distinct()
    doc = DocxTemplate("media/schoolNurses/whole_list.docx")
    for p in period_view:
        start_date = p.start_date.strftime('%d.%m.%Y')
        end_date = p.end_date.strftime('%d.%m.%Y')
        context = {
            'start_date': start_date,
            'end_date': end_date,
            'management_view': management_view,
            'management_set': management_set,
            'person_view': person_view,
            'num_person': num_person,
        }
        doc.render(context)
        doc.save("media/generated_whole_list.docx")
        # return render(request, 'trainingNurses/admin/test.html', context=context)

        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        response['Content-Disposition'] = 'attachment; filename=media/generated_whole_list.docx'
        doc.save(response)
        return response


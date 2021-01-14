from django.shortcuts import render
from .models import *


def index(request):
    pscategory = PSCategory.objects.all()
    context = {
        'pscategory': pscategory,
        'title': 'Платные услуги'
    }
    return render(request, 'paidServices/index.html', context=context)


def view_psupcat(request, pscategory_id):
    pscat_item = PSCategory.objects.get(pk=pscategory_id)
    psupcat_item = PSunderCategory.objects.filter(keyNameC_id=pscategory_id)
    context = {
        'pscat_item': pscat_item,
        'psupcat_item': psupcat_item,
        'title': pscat_item.nameC
    }
    return render(request, 'paidServices/view_upcat.html', context=context)


def view_service(request, pscategory_id, service_id):
    pscat_item = PSCategory.objects.get(pk=pscategory_id)
    psupcat_item = PSunderCategory.objects.filter(keyNameC_id=pscategory_id)
    service_item = PSlist.objects.filter(keyNameCU_id=service_id)
    context = {
        'pscat_item': pscat_item,
        'psupcat_item': psupcat_item,
        'service_item': service_item,
        'title': pscat_item.nameC
    }
    return render(request, 'paidServices/view_service.html', context=context)

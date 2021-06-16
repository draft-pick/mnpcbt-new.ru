from django.contrib import admin
from .models import *


@admin.register(Registration)
class PeriodAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'patronymic')
    list_display_links = ('surname', 'name', 'patronymic')


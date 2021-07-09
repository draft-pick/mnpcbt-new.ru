from django.contrib import admin

from .models import *


class periodNursesAdmin(admin.ModelAdmin):
    list_display = ('start_date', 'end_date')
    list_display_links = ('start_date', 'end_date')
    search_fields = ('start_date', 'end_date')


admin.site.register(periodsNurses)


class contractsNursesAdmin(admin.ModelAdmin):
    list_display = ('title', 'contract_date')
    list_display_links = ('title', 'contract_date')
    search_fields = ('title', 'contract_date')


admin.site.register(contractsNurses)

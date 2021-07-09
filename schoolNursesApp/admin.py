from django.contrib import admin
from .models import periodsApp, contractsApp


class contractsAppInline(admin.TabularInline):
    key_periods = 'key_periods'
    model = contractsApp


@admin.register(periodsApp)
class PeriodAppAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date')
    list_display_links = ('title', 'start_date', 'end_date')
    inlines = [contractsAppInline]

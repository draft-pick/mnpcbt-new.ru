from django.contrib import admin

from .models import *


class PSunderCat(admin.TabularInline):
    key_pscategory = 'keyNameC'
    model = PSunderCategory


class PSservice(admin.TabularInline):
    key_psuncategory = 'keyNameCU'
    model = PSlist


@admin.register(PSCategory)
class PSCategoryAdmin(admin.ModelAdmin):
    inlines = [PSunderCat]


@admin.register(PSunderCategory)
class PSunderCategoryAdmin(admin.ModelAdmin):
    inlines = [PSservice]

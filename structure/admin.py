from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *


class GalleryInline(admin.TabularInline):
    fk_name = 'keyBranches'
    model = GalleryBranches


class SpecialistsInline(admin.TabularInline):
    br_name = 'keyBranches'
    model = Specialists
    list_display = ('name', 'surname')


@admin.register(Branches)
class BranchesAdmin(admin.ModelAdmin):
    inlines = [GalleryInline, SpecialistsInline]


# @admin.register(Specialists)
# class SpecialistsAdmin(admin.ModelAdmin):
#     list_display = ('surname', 'name', 'patronymic')
#     list_display_links = ('surname', 'name', 'patronymic')
#     search_fields = ('surname', 'name')


@admin.register(Specialists)
class SpecialistsAdmin(admin.ModelAdmin):
    list_display = ('keyBranches', 'surname', 'name', 'patronymic')
    list_display_links = ('keyBranches', 'surname', 'name', 'patronymic')
    search_fields = ('keyBranches', 'surname', 'name')




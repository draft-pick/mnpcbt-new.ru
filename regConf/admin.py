from django.contrib import admin
from .models import *


class SchoolInline(admin.TabularInline):
    conference_key = 'conference_key'
    model = schoolName


class regSurnameInline(admin.TabularInline):
    school_key = 'school_key'
    model = regSurname


@admin.register(conference)
class conferenceAdmin(admin.ModelAdmin):
    inlines = [SchoolInline]


@admin.register(schoolName)
class schoolNameAdmin(admin.ModelAdmin):
    inlines = [regSurnameInline]
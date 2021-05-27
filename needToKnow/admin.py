from django.contrib import admin

from .models import *


class KnowAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Know, KnowAdmin)

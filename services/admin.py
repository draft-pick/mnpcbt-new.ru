from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Category, Services


class CustomMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 20


class CategoryAdmin(CustomMPTTModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Services)

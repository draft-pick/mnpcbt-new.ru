from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Category, periods, contracts


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Category, CategoryAdmin)


class contractsInline(admin.TabularInline):
    key_periods = 'key_periods'
    model = contracts


@admin.register(periods)
class PeriodAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date')
    list_display_links = ('title', 'start_date', 'end_date')
    inlines = [contractsInline]

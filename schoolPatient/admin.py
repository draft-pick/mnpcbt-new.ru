from django.contrib import admin

from .models import *


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    search_fields = ('title',)


admin.site.register(Sanatoriums)

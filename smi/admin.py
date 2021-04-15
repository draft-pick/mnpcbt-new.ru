from django.contrib import admin

from .models import *


class smiArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    list_display_links = ('title', 'created_at')
    search_fields = ('title', 'created_at')


admin.site.register(smiArticles)


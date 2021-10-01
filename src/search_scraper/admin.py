from django.contrib import admin

from .models import SearchItem


class SearchItemAdmin(admin.ModelAdmin):
    list_display = [
        'source',
        'link',
        'title',
        'publish_date',
    ]


admin.site.register(SearchItem, SearchItemAdmin)

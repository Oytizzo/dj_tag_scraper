from django.contrib import admin

from .models import SearchItem, ScrapeRecord


class SearchItemAdmin(admin.ModelAdmin):
    list_display = [
        'source',
        'link',
        'title',
        'publish_date',
    ]


admin.site.register(SearchItem, SearchItemAdmin)
admin.site.register(ScrapeRecord)

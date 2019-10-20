from django.contrib import admin
from .models import Entry


class EntryAdmin(admin.ModelAdmin):
    list_display = ['content', 'creator', 'published']
    list_display_links = ['content']
    ordering = ['published']


admin.site.register(Entry, EntryAdmin)

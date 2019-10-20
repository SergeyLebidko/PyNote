from django.contrib import admin
from .models import Topic, Entry


class TopicAdmin(admin.ModelAdmin):
    list_display = ['title', 'creator', 'published']
    list_display_links = ['title']
    ordering = ['published']


class EntryAdmin(admin.ModelAdmin):
    list_display = ['topic', 'content', 'creator', 'published']
    list_display_links = ['content']
    ordering = ['published']


admin.site.register(Topic, TopicAdmin)
admin.site.register(Entry, EntryAdmin)

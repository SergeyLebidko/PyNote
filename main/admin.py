from django.contrib import admin
from .models import Topic


class TopicAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'creator', 'published']
    list_display_links = ['title', 'content']
    ordering = ['published']


admin.site.register(Topic, TopicAdmin)

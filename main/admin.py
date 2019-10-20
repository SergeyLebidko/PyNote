from django.contrib import admin
from .models import Topic


class TopicAdmin(admin.ModelAdmin):
    list_display = ['content', 'creator', 'published']
    list_display_links = ['content']
    ordering = ['published']


admin.site.register(Topic, TopicAdmin)

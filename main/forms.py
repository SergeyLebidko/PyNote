from django import forms
from .models import Topic


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'content']
        labels = {'title': 'Тема', 'content': 'Текст'}
        widgets = {'content': forms.Textarea(attrs={'rows': 3, 'cols': 60})}

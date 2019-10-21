from django import forms
from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title']
        labels = {'title': 'Тема'}
        # widgets = {'title': forms.CharField(attrs={'cols': 60})}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['content']
        labels = {'content': 'Текст'}
        widgets = {'content': forms.Textarea(attrs={'rows': 3, 'cols': 60})}

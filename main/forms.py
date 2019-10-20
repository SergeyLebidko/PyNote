from django import forms
from .models import Entry


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['content']
        labels = {'content': 'Текст'}
        widgets = {'content': forms.Textarea(attrs={'rows': 3, 'cols': 60})}

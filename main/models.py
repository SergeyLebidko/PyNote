from django.db import models
from django.db.models import TextField, DateTimeField, ForeignKey
from django.contrib.auth.models import User


class Entry(models.Model):
    content = TextField(max_length=2048, verbose_name='Текст')
    published = DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    creator = ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Опубликовал', null=True)

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        ordering = ['published']

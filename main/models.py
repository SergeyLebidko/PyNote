from django.db import models
from django.db.models import CharField, TextField, DateTimeField, ForeignKey
from django.contrib.auth.models import User


class Topic(models.Model):
    title = CharField(max_length=128, verbose_name='Тема')
    content = TextField(max_length=2048, verbose_name='Текст')
    published = DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    creator = ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Опубликовал', null=True)

    class Meta:
        verbose_name = 'Запись блога'
        verbose_name_plural = 'Записи блога'
        ordering = ['published']

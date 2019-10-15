from django.db import models
from django.db.models import CharField, TextField, DateTimeField


class Topic(models.Model):
    title = CharField(max_length=128, verbose_name='Тема')
    content = TextField(max_length=2048, verbose_name='Текст')
    published = DateTimeField(auto_now_add=True, verbose_name='Опубликовано')

    class Meta:
        verbose_name = 'Запись блога'
        verbose_name_plural = 'Записи блога'
        ordering = ['published']

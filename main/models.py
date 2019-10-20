from django.db import models
from django.db.models import CharField, TextField, DateTimeField, ForeignKey
from django.contrib.auth.models import User


class Topic(models.Model):
    title = CharField(max_length=128, verbose_name='Тема')
    published = DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    creator = ForeignKey(User, on_delete=models.CASCADE, verbose_name='Опубликовал')

    class Meta:
        verbose_name = 'Темы'
        verbose_name_plural = 'Темы'
        ordering = ['published']

    def __str__(self):
        return self.title


class Entry(models.Model):
    content = TextField(max_length=2048, verbose_name='Текст')
    published = DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    creator = ForeignKey(User, on_delete=models.CASCADE, verbose_name='Опубликовал')
    topic = ForeignKey(Topic, on_delete=models.CASCADE, verbose_name='Тема')

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        ordering = ['published']

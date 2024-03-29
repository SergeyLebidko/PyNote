# Generated by Django 2.2.6 on 2019-10-17 16:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ['published'], 'verbose_name': 'Запись блога', 'verbose_name_plural': 'Записи блога'},
        ),
        migrations.AddField(
            model_name='topic',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Опубликовал'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='content',
            field=models.TextField(max_length=2048, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='published',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='title',
            field=models.CharField(max_length=128, verbose_name='Тема'),
        ),
    ]

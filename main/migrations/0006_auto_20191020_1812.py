# Generated by Django 2.2.6 on 2019-10-20 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20191020_1810'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ['published'], 'verbose_name': 'Темы', 'verbose_name_plural': 'Темы'},
        ),
    ]
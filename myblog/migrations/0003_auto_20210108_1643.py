# Generated by Django 3.1.5 on 2021-01-08 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_auto_20210108_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(verbose_name='عنوان'),
        ),
    ]

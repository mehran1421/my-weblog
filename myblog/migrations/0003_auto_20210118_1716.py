# Generated by Django 3.1.5 on 2021-01-18 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_auto_20210118_1657'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='whyBack',
            new_name='whyback',
        ),
    ]
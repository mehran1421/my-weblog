# Generated by Django 3.1.5 on 2021-01-23 14:59

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='تایتل')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='توضیحات')),
                ('thumbnail', models.ImageField(upload_to='images', verbose_name='عکس')),
                ('uni', models.CharField(max_length=200, verbose_name='دانشگاه')),
                ('comp', models.CharField(default='دانشجو', max_length=200, verbose_name='شغل')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمل')),
                ('email2', models.EmailField(max_length=254, verbose_name='ایمل')),
                ('insta', models.CharField(max_length=200, verbose_name='لینک اینستاگرام')),
                ('github', models.CharField(max_length=200, verbose_name='لینک گیتهاب')),
                ('wat', models.CharField(max_length=200, verbose_name='لینک واتساپ')),
                ('tel', models.CharField(max_length=200, verbose_name='لینک تلگرام')),
                ('address', models.CharField(max_length=200, verbose_name='آدرس')),
            ],
            options={
                'verbose_name': 'سازنده',
                'verbose_name_plural': 'سازنده ها',
            },
        ),
    ]
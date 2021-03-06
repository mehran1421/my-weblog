# Generated by Django 3.1.5 on 2021-01-23 15:00

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import myblog.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='تایتل')),
                ('slug', models.SlugField(allow_unicode=True, blank=True, verbose_name='عنوان')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='توضیحات')),
                ('thumbnail', models.ImageField(upload_to=myblog.models.upload_image_path, verbose_name='عکس')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='ساخته ')),
                ('whyback', models.CharField(max_length=200, null=True, verbose_name='دلیل برگشت مقاله')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='آپدیت')),
                ('is_special', models.BooleanField(default=False, verbose_name='آیا مقاله ی ویژه باشد؟')),
                ('status', models.CharField(choices=[('d', 'پیشنویس'), ('p', 'منتشرشده'), ('i', 'درحال بررسی'), ('b', 'برگشت داده شده')], max_length=1, verbose_name='وضعیت')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='articles', to=settings.AUTH_USER_MODEL, verbose_name='نویسنده')),
            ],
            options={
                'verbose_name': 'مقاله',
                'verbose_name_plural': 'مقاله ها',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='IPAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField(verbose_name='ادرس آی پی')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان دسته بندی')),
                ('slug', models.SlugField(max_length=100, verbose_name='موضوع')),
                ('status', models.BooleanField(default=True, verbose_name='آیا نمایش داده شود؟')),
                ('position', models.IntegerField(verbose_name='پوزیشن')),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='myblog.category', verbose_name='زیردسته')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
                'ordering': ['position'],
            },
        ),
        migrations.CreateModel(
            name='ArticleHit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myblog.article')),
                ('ip_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myblog.ipaddress')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(related_name='articles', to='myblog.Category', verbose_name='دسته بندی'),
        ),
        migrations.AddField(
            model_name='article',
            name='hits',
            field=models.ManyToManyField(blank=True, related_name='hits', through='myblog.ArticleHit', to='myblog.IPAddress', verbose_name='بازدیدها'),
        ),
    ]

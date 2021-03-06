import os
import random
from django.db import models
from django.utils import timezone
from django.urls import reverse
from .utils import unique_slug_generator
from django.utils.html import format_html
from account.models import User
from extension.utils import jalaly_converter
from django.db.models.signals import pre_save
from django.template.defaultfilters import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment

# Create your models here.

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_name = random.randint(1, 27634723542)
    name, ext = get_filename_ext(filename)
    # final_name = f"{new_name}{ext}"
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/{final_name}"


class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')


class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)


class IPAddress(models.Model):
    ip_address=models.GenericIPAddressField(verbose_name='ادرس آی پی')

class Category(models.Model):
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL,
                               related_name="children", verbose_name="زیردسته")

    title = models.CharField(max_length=200, verbose_name="عنوان دسته بندی")
    slug = models.SlugField(max_length=100, verbose_name="موضوع")
    status = models.BooleanField(default=True, verbose_name="آیا نمایش داده شود؟")
    position = models.IntegerField(verbose_name="پوزیشن")

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
        ordering = ['position']

    def __str__(self):
        return self.title

    objects = CategoryManager()




class Article(models.Model):
    Status_Choise = (
        ('d', 'پیشنویس'),
        ('p', 'منتشرشده'),
        ('i', 'درحال بررسی'),
        ('b', 'برگشت داده شده'),
    )
    title = models.CharField(max_length=200, verbose_name="تایتل")
    slug = models.SlugField(blank=True, allow_unicode=True, verbose_name="عنوان")
    category = models.ManyToManyField(Category, verbose_name="دسته بندی", related_name="articles")
    author=models.ForeignKey(User,null=True,on_delete=models.SET_NULL,related_name="articles",verbose_name="نویسنده")
    description = RichTextUploadingField(verbose_name="توضیحات")
    thumbnail = models.ImageField(upload_to=upload_image_path, verbose_name="عکس")
    publish = models.DateTimeField(default=timezone.now, verbose_name="زمان")
    created = models.DateTimeField(auto_now_add=True, verbose_name="ساخته ")
    whyback=models.CharField(null=True,max_length=200,verbose_name='دلیل برگشت مقاله')
    updated = models.DateTimeField(auto_now=True, verbose_name="آپدیت")
    is_special = models.BooleanField(default=False, verbose_name="آیا مقاله ی ویژه باشد؟")
    status = models.CharField(max_length=1, choices=Status_Choise, verbose_name="وضعیت")
    comments = GenericRelation(Comment)
    #وقتی از through استفاده میکنیم یعنی میخواهیم علاوه بر اون فیلدها یه فیلد دیگری هم داشته باشیم
    hits=models.ManyToManyField(IPAddress,through='ArticleHit',blank=True,related_name='hits',verbose_name='بازدیدها')

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقاله ها"
        ordering = ['-created']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    def jpublish(self):
        return jalaly_converter(self.publish)

    jpublish.short_description = "زمان انتشار"

    def category_published(self):
        return self.category.filter(status=True)

    def category_to_string(self):
        return ", ".join([cat.title for cat in self.category_published()])

    category_to_string.short_description = "دسته بندی"

    def get_absolute_url(self):
        return reverse("account:home")

    def thumbnail_tag(self):
        return format_html("<img width=100 src='{}'>".format(self.thumbnail.url))

    thumbnail_tag.short_description = "عکس"

    def hit_count(self):
        return self.hits.count()

    objects = ArticleManager()


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_receiver, sender=Article)

class ArticleHit(models.Model):
    article=models.ForeignKey(Article,on_delete=models.CASCADE)
    ip_address=models.ForeignKey(IPAddress,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
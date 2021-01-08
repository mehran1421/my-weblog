import os
import random
from django.db import models
from django.utils import timezone
from .utils import unique_slug_generator
from django.db.models.signals import pre_save
from extension.utils import jalaly_converter
from django.template.defaultfilters import slugify
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

class Owner(models.Model):
    title = models.CharField(max_length=200, verbose_name="تایتل")
    description = models.TextField(verbose_name="توضیحات")
    more=models.TextField(default='',verbose_name="توضیحات بیشتر")
    thumbnail = models.ImageField(upload_to="images", verbose_name="عکس")
    uni=models.CharField(max_length=200,verbose_name="دانشگاه")
    comp=models.CharField(max_length=200,default='دانشجو', verbose_name="شغل")
    email=models.EmailField(verbose_name="ایمل")
    insta=models.CharField(max_length=200, verbose_name="لینک اینستاگرام")
    github=models.CharField(max_length=200, verbose_name="لینک گیتهاب")
    wat=models.CharField(max_length=200, verbose_name="لینک واتساپ")
    tel=models.CharField(max_length=200, verbose_name="لینک تلگرام")

    class Meta:
        verbose_name="سازنده"
        verbose_name_plural="سازنده ها"

    def __str__(self):
        return self.title

class Article(models.Model):
    Status_Choise=(
        ('d','پیشنویس'),
        ('p','منتشرشده')
    )
    title=models.CharField(max_length=200,verbose_name="تایتل")
    slug=models.SlugField(blank=True,allow_unicode=True,verbose_name="عنوان")
    # category=models.ManyToManyField(Category,verbose_name="دسته بندی",related_name="articles")
    # author=models.ForeignKey(User,null=True,on_delete=models.SET_NULL,related_name="articles",verbose_name="نویسنده")
    description=models.TextField(verbose_name="توضیحات")
    thumbnail=models.ImageField(upload_to=upload_image_path,verbose_name="عکس")
    publish=models.DateTimeField(default=timezone.now,verbose_name="زمان")
    created=models.DateTimeField(auto_now_add=True,verbose_name="ساخته ")
    updated=models.DateTimeField(auto_now=True,verbose_name="آپدیت")
    status=models.CharField(max_length=1,choices=Status_Choise,verbose_name="وضعیت")
    class Meta:
        verbose_name="مقاله"
        verbose_name_plural="مقاله ها"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    def jpublish(self):
        return jalaly_converter(self.publish)

    jpublish.short_description = "زمان انتشار"


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_receiver, sender=Article)




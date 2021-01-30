from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Owner(models.Model):
    title = models.CharField(max_length=200, verbose_name="تایتل")
    description = RichTextUploadingField(verbose_name="توضیحات")
    thumbnail = models.ImageField(upload_to="images", verbose_name="عکس")
    uni = models.CharField(max_length=200, verbose_name="دانشگاه")
    comp = models.CharField(max_length=200, default='دانشجو', verbose_name="شغل")
    email = models.EmailField(verbose_name="ایمل")
    email2 = models.EmailField(verbose_name="ایمل2")
    insta = models.CharField(max_length=200, verbose_name="لینک اینستاگرام")
    github = models.CharField(max_length=200, verbose_name="لینک گیتهاب")
    wat = models.CharField(max_length=200, verbose_name="لینک واتساپ")
    tel = models.CharField(max_length=200, verbose_name="لینک تلگرام")
    address=models.CharField(max_length=200, verbose_name="آدرس")

    class Meta:
        verbose_name = "سازنده"
        verbose_name_plural = "سازنده ها"

    def __str__(self):
        return self.title


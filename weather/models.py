from django.db import models

# Create your models here.
class City(models.Model):
    name=models.CharField(max_length=25,verbose_name='نام شهر')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='شهر'
        verbose_name_plural='شهرها'





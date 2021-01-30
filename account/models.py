from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Create your models here.
class User(AbstractUser):
	email = models.EmailField(unique=True, verbose_name='ایمیل')

	is_author = models.BooleanField(default=False, verbose_name="وضعیت نویسندگی")
	special_user = models.DateTimeField(default=timezone.now, verbose_name="کاربر ویژه تا")

	phone_regex=RegexValidator(regex=r'^[09]{1}([0-9]){9}$',message='شماره تلفن باید کامل همراه با صفر آغازین باشد مثال:09123456789')
	phone=models.CharField(validators=[phone_regex],max_length=11,unique=True,null=True,verbose_name='شماره تلفن')

	def is_special_user(self):
		if self.special_user > timezone.now():
			return True
		else:
			return False
	is_special_user.boolean = True
	is_special_user.short_description = "وضعیت کاربر ویژه"
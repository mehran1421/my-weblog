from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from django.utils.translation import ugettext_lazy as _


class RegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput())

    class Meta:
        model =User
        fields = ('username','email','first_name','last_name')
        labels = {
            'username': _('نام کاربری'),
            'email': _('ایمل'),
            'first_name': _('نام'),
            'last_name': _('فامیلی'),
        }
        help_texts = {
            'username': _('لطفا نام کاربری خودتان را وارد کنید'),
            'email': _('لطفا ایمیل خودتان را وارد کنید'),
            'password2': _('حتما هر دو گذرواژه یکتا باشند'),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("کلمه ی عبور نا هماهنگ هستند")
        return password2

    def clean_username(self):
        username = self.cleaned_data.get("username")
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("این نام کاربری از قبل موجود است")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            email = User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError("این ایمیل قبلا توسط شخص دیگری استفاده شده است")


class MyAuthForm(AuthenticationForm):
    error_messages = {
        'invalid_login': _('نام کاربری یا رمز عبور، صحیح نمی باشد'),
    }



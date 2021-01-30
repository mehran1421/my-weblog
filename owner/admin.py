from django.contrib import admin
from .models import Owner
# Register your models here.
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('title','description','uni','comp','email','email2','insta','github','wat','tel',)

admin.site.register(Owner, ContactUsAdmin)
from django.contrib import admin
from .models import Article,Owner,Category
# Register your models here.

def make_published(modeladmin,request,queryset):
    row_updated=queryset.update(status='p')
    if row_updated==1:
        message_bit="منتشر شد"
    else:
        message_bit="منتشر شدند"

    modeladmin.message_user(request,"{} مقاله {}".format(row_updated,message_bit))


make_published.short_description="انتشار مقاله"



def make_Draft(modeladmin,request,queryset):
    row_updated=queryset.update(status='d')
    if row_updated==1:
        message_bit="پیش نویس شد"
    else:
        message_bit="پیش نویس شدند"

    modeladmin.message_user(request,"{} مقاله {}".format(row_updated,message_bit))


make_Draft.short_description="پیش نویس مقاله"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'slug', 'parent', 'status')
    list_filter = (['status'])
    search_fields = ('title', 'slug')


admin.site.register(Category, CategoryAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','thumbnail_tag', 'slug','author', 'status','jpublish','category_to_string')
    list_filter = ('status', 'publish')
    search_fields = ('title', 'description')

    actions = [make_published, make_Draft]


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title', 'description')
    search_fields = ('title', 'description')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Owner, OwnerAdmin)
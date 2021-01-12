from django.contrib import admin
from .models import Article,Owner,Category
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'slug', 'parent', 'status')
    list_filter = (['status'])
    search_fields = ('title', 'slug')


admin.site.register(Category, CategoryAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','jpublish','category_to_string')
    list_filter = ('status', 'publish')
    search_fields = ('title', 'description')


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title', 'description')
    search_fields = ('title', 'description')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Owner, OwnerAdmin)
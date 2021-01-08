from django.contrib import admin
from .models import Article,Owner
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status')
    list_filter = ('status', 'publish')
    search_fields = ('title', 'description')

class OwnerAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title', 'description')
    search_fields = ('title', 'description')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Owner, OwnerAdmin)
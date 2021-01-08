from django.urls import re_path,path
from .views import ArticleList,ArticleDetail

app_name='blog'
urlpatterns = [
    path('blog/',ArticleList.as_view(),name='articleList'),
    path(r'blog/<int:page>',ArticleList.as_view(),name='articleList'),
    re_path(r'blog/(?P<slug>[-\w\d]+)/', ArticleDetail.as_view(), name="detail"),
]
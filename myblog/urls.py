from django.urls import re_path,path
from .views import ArticleList,ArticleDetail,CategoryList,AuthorList,ArticlePreview

app_name='blog'
urlpatterns = [
    path('blog/',ArticleList.as_view(),name='articleList'),
    path(r'blog/<int:page>',ArticleList.as_view(),name='articleList'),
    re_path(r'blog/(?P<slug>[-\w\d]+)/', ArticleDetail.as_view(), name="detail"),
    path('preview/<int:pk>', ArticlePreview.as_view(), name="preview"),
    path('category/<slug:slug>',CategoryList.as_view(),name="category"),
    path('category/<slug:slug>/page/<int:page>', CategoryList.as_view(), name="category"),
    path('author/<slug:username>', AuthorList.as_view(), name="author"),
    path('author/<slug:username>/page/<int:page>', AuthorList.as_view(), name="author"),
]
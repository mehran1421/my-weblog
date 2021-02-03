from django.urls import re_path,path
from myblog.api.views import ArticleListAPIView,ArticleDetailAPIView,ArticleDeleteAPIView,ArticleUpdateAPIView


app_name='blogAPI'
urlpatterns = [
    path('',ArticleListAPIView.as_view(),name='articleListAPI'),
    # path(r'blog/<int:page>',ArticleList.as_view(),name='articleList'),
    re_path(r'(?P<slug>[-\w\d]+)/', ArticleDetailAPIView.as_view(), name="detailAPI"),
    # path('preview/<int:pk>', ArticlePreview.as_view(), name="preview"),
    # path('category/<slug:slug>',CategoryList.as_view(),name="category"),
    # path('category/<slug:slug>/page/<int:page>', CategoryList.as_view(), name="category"),
    # path('author/<slug:username>', AuthorList.as_view(), name="author"),
    # path('author/<slug:username>/page/<int:page>', AuthorList.as_view(), name="author"),
    # path('search/', SearchList.as_view(), name="search"),
    # path('search/page/<int:page>', SearchList.as_view(), name="search"),
]
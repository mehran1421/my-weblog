from django.urls import path
from .views import ArticleList,ArticleDetail

app_name='blog'
urlpatterns = [
    path('blog/',ArticleList.as_view(),name='articleList'),
    path('blog/<int:page>',ArticleList.as_view(),name='articleList'),
    path('blog/<slug:slug>', ArticleDetail.as_view(), name="detail"),

]
from django.urls import path
from .views import ArticleUpdateAPIView,ArticleDeleteAPIView,ArticleCreateAPIView

app_name = 'accountAPI'
urlpatterns = [
    # path('', ArticleList.as_view(), name='home'),
    path('create', ArticleCreateAPIView.as_view(), name="article-createAPI"),
    path('update/<int:pk>', ArticleUpdateAPIView.as_view(), name="article-updateAPI"),
    # path('article/back/<int:pk>', WhyBackArticle.as_view(), name="article-back"),
    path('delete/<int:pk>', ArticleDeleteAPIView.as_view(), name="article-deleteAPI"),
    # path('profile/', Profile.as_view(), name="profile"),
]

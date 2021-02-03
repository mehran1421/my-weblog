from rest_framework.generics import UpdateAPIView,DestroyAPIView,CreateAPIView
from myblog.models import Article
from .serializers import ArticleCreateUpdateSerializer


class ArticleDeleteAPIView(DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleCreateUpdateSerializer


class ArticleUpdateAPIView(UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleCreateUpdateSerializer


class ArticleCreateAPIView(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleCreateUpdateSerializer
from rest_framework.generics import ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from myblog.models import Article
from .serializers import ArticleSerializer,ArticleDetailSerializer

class ArticleListAPIView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetailAPIView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    lookup_field = 'slug'

class ArticleDeleteAPIView(DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    lookup_field = 'slug'

class ArticleUpdateAPIView(UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    lookup_field = 'slug'
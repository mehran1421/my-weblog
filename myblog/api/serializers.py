from rest_framework.serializers import ModelSerializer
from myblog.models import Article


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'title',
            'pk',
            'slug',
            'thumbnail_tag',
            'author',
            'description',
            'created',
            'is_special',
            'status',
            'jpublish'
        ]


class ArticleDetailSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'title',
            'pk',
            'thumbnail_tag',
            'author',
            'category',
            'description',
            'created',
            'hit_count',
            'is_special',
            'status',
            'jpublish'
        ]

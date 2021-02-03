from rest_framework.serializers import ModelSerializer
from myblog.models import Article

class ArticleCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'title',
            'slug',
            'thumbnail',
            'author',
            'category',
            'description',
            'whyback',
            'created',
            'is_special',
            'status',
            'publish',
        ]
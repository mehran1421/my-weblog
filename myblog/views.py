from django.shortcuts import render
from .models import Article,Category
from django.views.generic import ListView
from django.shortcuts import get_object_or_404

# Create your views here.

class ArticleList(ListView):
    template_name="blog/article_list.html"
    queryset = Article.objects.filter(status='p').order_by('-created')
    paginate_by=9

class ArticleDetail(ListView):
    template_name="blog/article_detail.html"
    def get_queryset(self):
        global slug,article
        slug=self.kwargs.get('slug')
        article=Article.objects.filter(status='p').order_by('-created')
        return article

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['object']=get_object_or_404(article,slug=slug)
        context['res_articles']=article[:5]
        return context


class CategoryList(ListView):
    paginate_by=9
    template_name="blog/category.html"

    def get_queryset(self):
        global category
        slug=self.kwargs.get('slug')
        category=get_object_or_404(Category.objects.filter(status=True),slug=slug)
        return category.articles.all()

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['category']=category
        return context
from django.shortcuts import render
from .models import Article,Category
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

# Create your views here.

class ArticleList(ListView):
    template_name="blog/article_list.html"
    queryset = Article.objects.published()
    paginate_by=6

class ArticleDetail(ListView):
    template_name="blog/article_detail.html"
    def get_queryset(self):
        global slug,article
        slug=self.kwargs.get('slug')
        article=Article.objects.published()
        return article

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['object']=get_object_or_404(article,slug=slug)
        context['res_articles']=article[:5]
        return context


class CategoryList(ListView):
    paginate_by=6
    template_name="blog/category_list.html"

    def get_queryset(self):
        global category
        slug=self.kwargs.get('slug')
        category=get_object_or_404(Category.objects.active(),slug=slug)
        return category.articles.published()

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['category']=category
        return context

class AuthorList(ListView):
    paginate_by=6
    template_name="blog/author_list.html"

    def get_queryset(self):
        global author
        username=self.kwargs.get('username')
        author=get_object_or_404(User,username=username)
        return author.articles.published()

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['author']=author
        return context
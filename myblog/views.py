from django.shortcuts import render
from .models import Article,Category
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from account.models import User
from account.mixins import AuthorAccessMixin
from django.db.models import Count,Q

# Create your views here.

class ArticleList(ListView):
    template_name="blog/article_list.html"
    queryset = Article.objects.published()
    paginate_by=6

class ArticleDetail(ListView):
    template_name="blog/article_detail.html"

    def get_queryset(self):
        global slug,article_published,article
        slug=self.kwargs.get('slug')
        article_published=Article.objects.published().annotate(
            count=Count('hits')
        ).order_by('-count','publish')
        article=get_object_or_404(article_published,slug=slug)
        ip_address=self.request.user.ip_address
        if ip_address not in article.hits.all():
            article.hits.add(ip_address)
        return article_published

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['object']=article
        context['res_articles']=article_published[:5]
        return context


class ArticlePreview(AuthorAccessMixin,ListView):
    template_name="blog/article_detail.html"
    def get_queryset(self):
        global pk,article
        pk=self.kwargs.get('pk')
        article=Article.objects.all()
        return article

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['object']=get_object_or_404(article,pk=pk)
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

class SearchList(ListView):
    paginate_by=6
    template_name="blog/search_list.html"

    def get_queryset(self):
        global search
        search=self.request.GET.get('q')
        return Article.objects.filter(Q(description__icontains=search)|Q(title=search))

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['search']=search
        return context
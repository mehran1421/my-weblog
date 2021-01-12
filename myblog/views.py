from django.shortcuts import render
from .models import Article,Owner,Category
from django.views.generic import ListView
from django.shortcuts import render,get_object_or_404

# Create your views here.

class ArticleList(ListView):
    template_name="blog/article_list.html"
    queryset = Article.objects.filter(status='p').order_by('-created')
    paginate_by=9
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['owner']=Owner.objects.first()
        return context

class ArticleDetail(ListView):
    template_name="blog/article_detail.html"
    def get_queryset(self):
        global slug,article,category,count
        slug=self.kwargs.get('slug')
        article=Article.objects.filter(status='p').order_by('-created')
        return article

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['object']=get_object_or_404(article,slug=slug)
        context['owner']=Owner.objects.first()
        context['res_articles']=article[:5]
        return context


# class CategoryList(ListView):
#     paginate_by=3
#     template_name="blog/category.html"
#
#     def get_queryset(self):
#         global category
#         slug=self.kwargs.get('slug')
#         category=get_object_or_404(Category.objects.active(),slug=slug)
#         return category.articles.published()
#
#     def get_context_data(self,**kwargs):
#         context=super().get_context_data(**kwargs)
#         context['category']=category
#         return context
#

from django.shortcuts import render
from .models import Article,Owner
from django.views.generic import ListView,DetailView
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
    paginate_by=9
    template_name="blog/article_detail.html"
    def get_queryset(self):
        global slug
        slug=self.kwargs.get('slug')
        return Article.objects.filter(status='p')

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['object']=get_object_or_404(Article.objects.filter(status='p'),slug=slug)
        context['owner']=Owner.objects.first()
        return context

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from myblog.models import Article
from .forms import MyAuthForm


# Create your views here.

class ArticleList(LoginRequiredMixin, ListView):
    template_name = 'registration/home.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Article.objects.all()
        else:
            return Article.objects.filter(author=self.request.user)


class ArticleCreate(CreateView):
    model = Article
    fields = ['title','slug','category','author','description','thumbnail','publish','status']
    template_name = "registration/article-create-update.html"


class Login(LoginView):
    authentication_form = MyAuthForm

    def get_success_url(self):
        user = self.request.user
        if user.is_superuser:
            return reverse_lazy("account:home")
        else:
            return reverse_lazy("account:home")

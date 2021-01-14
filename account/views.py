from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from myblog.models import Article
from .forms import MyAuthForm

# Create your views here.

class ArticleList(LoginRequiredMixin,ListView):
    queryset = Article.objects.all()
    template_name = 'registration/home.html'


class Login(LoginView):
    authentication_form = MyAuthForm

    def get_success_url(self):
        user = self.request.user
        if user.is_superuser or user.is_author:
            return reverse_lazy("account:home")
        else:
            pass


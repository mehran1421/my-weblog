from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView,UpdateView,DeleteView,TemplateView
from django.urls import reverse_lazy
from django.shortcuts import render
from .forms import ProfileForm
from django.contrib.auth.views import LoginView,LogoutView
from .mixins import FieldsMixin,FormValidMixin,BackAccessMixin,AuthorAccessMixin,AuthorsAccessMixin,SuperUserAccessMixin
from myblog.models import Article
from .models import User

# Create your views here.

class ArticleList(LoginRequiredMixin, ListView):
    template_name = 'registration/home.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Article.objects.all()
        else:
            return Article.objects.filter(author=self.request.user)


class ArticleCreate(AuthorsAccessMixin,FormValidMixin,FieldsMixin,CreateView):
    model = Article
    template_name = "registration/article-create-update.html"


class ArticleUpdate(AuthorAccessMixin,FormValidMixin, FieldsMixin, UpdateView):
	model = Article
	template_name = "registration/article-create-update.html"


class ArticleDelete(SuperUserAccessMixin,DeleteView):
    model = Article
    template_name = 'registration/article_confirm_delete.html'
    success_url = reverse_lazy('account:home')


class WhyBackArticle(BackAccessMixin,TemplateView):
    def get(self,request,*args,**kwargs):
        article=Article.objects.filter(pk=self.kwargs['pk']).first()
        context={
            'why':article
        }
        return render(request,'registration/whyback.html',context)


class Profile(UpdateView):
    model = User
    form_class = ProfileForm
    template_name = "registration/profile.html"
    success_url = reverse_lazy("account:profile")

    def get_object(self, queryset=None):
        return User.objects.get(pk=self.request.user.pk)

    def get_form_kwargs(self):
        kwargs=super(Profile,self).get_form_kwargs()
        kwargs.update({
            'user':self.request.user
        })
        return kwargs


class Login(LoginView):
    def get_success_url(self):
        user = self.request.user
        if user.is_superuser:
            return reverse_lazy("account:home")
        else:
            return reverse_lazy("account:home")


class LogOut(LogoutView):
    pass


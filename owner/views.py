from django.views.generic import ListView
from .models import Owner


# Create your views here.
class CountactUs(ListView):
    queryset = Owner.objects.first()
    template_name = 'blog/contactus.html'



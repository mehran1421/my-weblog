from django.urls import path
from .views import CountactUs

app_name='contactUs'
urlpatterns = [
    path('', CountactUs.as_view(),name='contact')
]

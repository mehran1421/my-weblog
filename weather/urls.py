from django.urls import path
from .views import index,delete_city

app_name='weather'
urlpatterns = [
    path('', index,name='weather_home'),
    path('delete/<str:city_name>', delete_city,name='delete_city'),
]

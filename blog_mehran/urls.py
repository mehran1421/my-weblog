"""blog_mehran URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include, re_path
from account.views import Login, Register, activate
from blog_mehran import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('myblog.urls')),
    path('account/', include('account.urls')),
    path('comment/', include('comment.urls')),
    path('contact/', include('owner.urls')),
    path('weatherblog/', include('weather.urls')),

    # api
    path('api/posts/', include('myblog.api.urls')),
    path('api/account/', include('account.api.urls')),


    path('', include('django.contrib.auth.urls')),

    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,200})/$', activate,
            name='activate'),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    re_path(r'^ratings/', include('star_ratings.urls', namespace='ratings')),
    path('', include('social_django.urls', namespace='social')),
    path('api-auth/', include('rest_framework.urls'))
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

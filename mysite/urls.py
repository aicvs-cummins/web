"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include, re_path
from myapp import views as v 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
'''
to use static() and adding media url to url patterns add the next 2 lines of code
'''
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v.index),
    path('about/', v.about),
    path('contact/', v.contact),
    path('/blog/', include('blog.urls')),
    re_path(r'^about/$', v.about),
    re_path(r'^contact/$', v.contact),
    re_path(r'^blog/', include('blog.urls')),
    re_path(r'^tinymce/', include('tinymce.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()



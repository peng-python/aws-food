"""food URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
import xadmin

from food.settings import MEDIA_ROOT
from django.views.static import serve

from food_foods.views import IndexView

urlpatterns = [
    url(r'^admin00/xadmin/', xadmin.site.urls),
    url(r'^media/(?P<path>.*$)', serve, {'document_root': MEDIA_ROOT}),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^foods/', include('food_foods.urls', namespace='foods')),
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
]

handler404 = 'users.views.page_not_found'

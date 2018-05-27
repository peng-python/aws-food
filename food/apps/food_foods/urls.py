from django.conf.urls import url

from food_foods import views

urlpatterns = [
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^detail/(?P<blog_id>\d+)/$', views.detail, name='detail'),
    url(r'^comment/$', views.comment, name='comment'),
]
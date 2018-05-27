from django.conf.urls import url

from users import views

urlpatterns = [
    url(r'^register/$', views.register_user, name='register'),
    url(r'^login/$', views.login_user, name='login'),
]
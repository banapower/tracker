from django.conf.urls import include, url
from django.urls import path

from user import views

urlpatterns = [
    url(r'^singup/$', views.signup, name='signup'),
    url(r'^login/$', views.login_user, name='login'),
]
from django.conf.urls import url
from user import views

urlpatterns = [
    url(r'^singup/$', views.signup, name='signup'),
    url(r'^login/$', views.login_user, name='login'),
    url(r'^edit/$', views.edit, name='user-edit'),
]
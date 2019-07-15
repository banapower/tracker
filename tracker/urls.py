from os import path

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

from tracker import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^project/$', views.project_list, name='project-list'),
    url(r'^project/([\w\-\._]*)/$', views.project_show, name='project-show'),
    url(r'^project/edit/([\w\-\._]*)/$', views.project_edit, name='project-edit'),
    url(r'^project/task/([\w\-\._]*)/(\d+)/$', views.project_task_show, name='project-task-show'),
    url(r'^project/task/edit/([\w\-\._]*)/(\d+)/$', views.project_task_edit, name='project-task-edit'),
    url(r'^project/time_logging/edit/([\w\-\._]*)/(\d+)/$', views.time_logging_edit, name='time-logging-edit'),
    url('user/', include('user.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin

app_name = 'forums'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='topic'),
    url(r'^login/$', views.login_user, name='login_user'),
    url(r'^AddTopic/$', views.AddTopic.as_view(), name='AddTopic-add'),
]
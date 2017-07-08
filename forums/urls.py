from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib import admin

app_name = 'forums'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='topic'),
    url(r'^login/$', views.login_user, name='login_user'),
    # url(r'^AddTopic/$', views.AddTopic.as_view(), name='AddTopic-add'),
    url(r'^AddTopic/$', views.AddTopic, name='AddTopic'),
    url(r'^handlereply/$', views.handlereply, name='handlereply'),
    url(r'^handle/$', views.handle, name='handle'),
    url(r'^newpost/$', views.newpost, name='newpost'),
    url(r'^PostTopic/$', views.PostTopic.as_view(), name='PostTopic'),
    url(r'^logout/$', views.user_logout, name='user_logout'),
    url(r'^post/(?P<post_id>[0-9]+)/$', views.post, name='post'),
    url(r'^search/$', views.search, name='search'),
    url(r'^searchpostresults/$', views.searchpostresults, name='searchpostresults'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

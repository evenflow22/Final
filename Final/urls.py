from django.conf.urls import url, include
from django.contrib import admin

from forums import views

urlpatterns = [
    url(r'^forums/', include('forums.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
]

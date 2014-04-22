from django.conf.urls import patterns, include, url
from mysite.view import hello
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    ('^hello/$', hello),
)

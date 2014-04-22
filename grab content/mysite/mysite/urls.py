from django.conf.urls import patterns, include, url
from mysite.view import hello, current_datetime
from django.contrib import admin
import datetime
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    ('^hello/$', hello),
    #('^$', hello),
    ('^time/$', current_datetime),
)

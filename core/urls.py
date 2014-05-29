from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', '{{ project_name }}.views.home', name='home'),
    # url(r'^{{ project_name }}/', include('{{ project_name }}.foo.urls')),
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # url(r'^$', TemplateView.as_view(template_name='index.html')),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^$', 'pages.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'pages.views.pages', name='pages'),
    url(r'^weekly/', 'pages.views.weekly', name='weekly'),
    url(r'^pages/', 'pages.views.pages', name='pages'),
    url(r'^daily/', 'pages.views.daily', name='daily'),
    url(r'^monthly/', 'pages.views.monthly', name='monthly')
)
# ) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.conf.urls import patterns, include, url
from django.contrib import admin
from unsubscribe import urls as unsubscribe_urls
from unsubscribe.views import UnsubscribeHomeView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'test_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', UnsubscribeHomeView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^unsubscribe/', include(unsubscribe_urls, namespace='unsubscribe')),
)

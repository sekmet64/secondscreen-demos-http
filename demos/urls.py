from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'demos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'demos.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^demos$', 'demos.views.demos', name='demos'),
    url(r'^register-url', 'demos.views.registerurl', name='register-url'),
    url(r'^youtube-demo$', 'demos.views.youtubedemo', name='youtube-demo'),
    url(r'^(?P<uniqueId>\w+)$', 'demos.views.shorturl', name='youtube-remote'),
    url(r'^admin/', include(admin.site.urls)),
)

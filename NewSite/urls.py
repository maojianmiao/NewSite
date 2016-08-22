from django.conf.urls import patterns, include, url

from django.contrib import admin
from plus.views import home
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'NewSite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'home/$',home),
)

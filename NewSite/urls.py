from django.conf.urls import patterns, include, url

from django.contrib import admin
from plus.views import home
from django.contrib.auth.views import login, logout

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'NewSite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'home/$',home),
    url(r'^login/$',  login),
    url(r'^logout/$', logout),
    url(r'^user/',include('users.urls')),
)

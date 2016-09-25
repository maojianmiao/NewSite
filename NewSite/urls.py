from django.conf.urls import patterns, include, url

from django.contrib import admin
from plus.views import home

import plus.views
from django.contrib.auth.views import login, logout
import users.views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'NewSite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^user/',include('users.urls')),
    url(r'home/$',home),
    url(r'^login/$',  login),
    url(r'^logout/$', logout),
    url(r'^test/session/$',plus.views.testSession),
    url(r'^accounts/login/',users.views.login),
    url(r'^about/',plus.views.about),
    url(r'^test/',plus.views.dobject),
    url(r'^finance/',plus.views.finance),
    url(r'^tech/',plus.views.tech),

)

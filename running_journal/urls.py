from django.conf.urls import patterns, include, url
from django.contrib import admin

import journal.views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
	url(r'^journal/', include('journal.urls')),
	url(r'^accounts/', include('accounts.urls')),
)

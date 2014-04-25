from django.conf.urls import patterns, include, url
from django.contrib import admin

import journal.views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', journal.views.ListJournalView.as_view(), name='journal_list'),
	url(r'^journal/', include('journal.urls')),
)

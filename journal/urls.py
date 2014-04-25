from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import journal.views

urlpatterns = patterns('',
	url(r'^$', journal.views.ListJournalView.as_view(), name='journal_list'),
	url(r'^new/$', journal.views.CreateJournalView.as_view(), name='journal_new'),
	url(r'^edit/(?P<pk>\d+)/$', journal.views.UpdateJournalView.as_view(), name='journal_edit'),
	url(r'^delete/(?P<pk>\d+)/$', journal.views.DeleteJournalView.as_view(), name='journal_delete'),
)

urlpatterns += staticfiles_urlpatterns()

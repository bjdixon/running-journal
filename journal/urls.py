from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import journal.views

urlpatterns = patterns('',
	url(r'^$', journal.views.ListJournalEntriesView.as_view(), name='journal_entry_list'),
	url(r'^new/entry/$', journal.views.CreateJournalEntryView.as_view(), name='journal_entry_new'),
	url(r'^edit/entry/(?P<pk>\d+)/$', journal.views.UpdateJournalEntryView.as_view(), name='journal_entry_edit'),
	url(r'^delete/entry/(?P<pk>\d+)/$', journal.views.DeleteJournalEntryView.as_view(), name='journal_entry_delete'),
	url(r'^detail/entry/(?P<pk>\d+)/$', journal.views.DetailJournalEntryView.as_view(), name='journal_entry_detail'),
)

urlpatterns += staticfiles_urlpatterns()

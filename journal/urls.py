from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

import journal.views

urlpatterns = patterns('',
	url(r'^$', TemplateView.as_view(template_name='home.html')),
	url(r'^list/entries/(?P<pk>\d+)/$', journal.views.ListJournalEntriesView.as_view(), name='journal_entry_list'),
	url(r'^list/$', journal.views.JournalListView.as_view(), name='journal'),
	url(r'^create/$', journal.views.CreateJournalView.as_view(), name='journal_create'),
	url(r'^(?P<journal_id>\d+)/new/entry/$', journal.views.CreateJournalEntryView.as_view(), name='journal_entry_new'),
	url(r'^(?P<journal_id>\d+)/edit/entry/(?P<pk>\d+)/$', journal.views.UpdateJournalEntryView.as_view(), name='journal_entry_edit'),
	url(r'^(?P<journal_id>\d+)/delete/entry/(?P<pk>\d+)/$', journal.views.DeleteJournalEntryView.as_view(), name='journal_entry_delete'),
	url(r'^(?P<journal_id>\d+)/detail/entry/(?P<pk>\d+)/$', journal.views.DetailJournalEntryView.as_view(), name='journal_entry_detail'),
)

urlpatterns += staticfiles_urlpatterns()

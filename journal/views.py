from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.core.urlresolvers import reverse

from journal.models import Journal_Entry

class ListJournalEntriesView(ListView):
	
	model = Journal_Entry
	template_name = 'journal_entry_list.html'


class CreateJournalEntryView(CreateView):

	model = Journal_Entry
	template_name = 'edit_journal_entry.html'

	def get_success_url(self):
		return reverse('journal_entry_list')

	def get_context_data(self, **kwargs):
		context = super(CreateJournalEntryView, self).get_context_data(**kwargs)
		context['action'] = reverse('journal_entry_new')
		return context


class UpdateJournalEntryView(UpdateView):

	model = Journal_Entry
	template_name = 'edit_journal_entry.html'

	def get_success_url(self):
		return reverse('journal_entry_list')

	def get_context_data(self, **kwargs):
		context = super(UpdateJournalEntryView, self).get_context_data(**kwargs)
		context['action'] = reverse('journal_entry_edit', kwargs={'pk': self.get_object().id})
		return context


class DeleteJournalEntryView(DeleteView):

	model = Journal_Entry
	template_name = 'delete_journal_entry.html'

	def get_success_url(self):
		return reverse('journal_entry_list')


class DetailJournalEntryView(DetailView):

	model = Journal_Entry
	template_name = 'detail_journal_entry.html'



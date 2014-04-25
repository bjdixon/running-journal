from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.core.urlresolvers import reverse

from journal.models import Journal_Entry

class ListJournalView(ListView):
	
	model = Journal_Entry
	template_name = 'journal_list.html'


class CreateJournalView(CreateView):

	model = Journal_Entry
	template_name = 'edit_journal.html'

	def get_success_url(self):
		return reverse('journal_list')

	def get_context_data(self, **kwargs):
		context = super(CreateJournalView, self).get_context_data(**kwargs)
		context['action'] = reverse('journal_new')
		return context


class UpdateJournalView(UpdateView):

	model = Journal_Entry
	template_name = 'edit_journal.html'

	def get_success_url(self):
		return reverse('journal_list')

	def get_context_data(self, **kwargs):
		context = super(UpdateJournalView, self).get_context_data(**kwargs)
		context['action'] = reverse('journal_edit', kwargs={'pk': self.get_object().id})
		return context


class DeleteJournalView(DeleteView):

	model = Journal_Entry
	template_name = 'delete_journal.html'

	def get_success_url(self):
		return reverse('journal_list')


class DetailJournalView(DetailView):

	model = Journal_Entry
	template_name = 'detail_journal.html'



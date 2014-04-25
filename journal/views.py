from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse

from journal.models import Journal

class ListJournalView(ListView):
	
	model = Journal
	template_name = 'journal_list.html'


class CreateJournalView(CreateView):

	model = Journal
	template_name = 'edit_journal.html'

	def get_success_url(self):
		return reverse('journal_list')

	def get_context_data(self, **kwargs):
		context = super(CreateJournalView, self).get_context_data(**kwargs)
		context['action'] = reverse('journal_new')
		return context


class UpdateJournalView(UpdateView):

	model = Journal
	template_name = 'edit_journal.html'

	def get_success_url(self):
		return reverse('journal_list')

	def get_context_data(self, **kwargs):
		context = super(UpdateJournalView, self).get_context_data(**kwargs)
		context['action'] = reverse('journal_edit', kwargs={'pk': self.get_object().id})
		return context


class DeleteJournalView(DeleteView):

	model = Journal
	template_name = 'delete_journal.html'

	def get_success_url(self):
		return reverse('journal_list')


from django.http import HttpResponse
from django.views.generic import ListView, CreateView
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


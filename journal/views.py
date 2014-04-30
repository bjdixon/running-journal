from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from journal.models import Journal, Journal_Entry
from journal.forms import CreateJournalForm


class LoggedInMixin(object):

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(LoggedInMixin, self).dispatch(*args, **kwargs)


class JournalListView(LoggedInMixin, ListView):

	model = Journal
	template_name = 'journal.html'

	def get_queryset(self):
		return Journal.objects.filter(owner=self.request.user)


class CreateJournalView(LoggedInMixin, CreateView):
	
	form_class = CreateJournalForm
	template_name = 'journal_create.html'

	def form_valid(self, form):
		journal = form.save(commit=False)
		journal.owner = self.request.user
		journal.save()
		return HttpResponseRedirect(reverse('journal'))


class ListJournalEntriesView(ListView):
	
	model = Journal_Entry
	template_name = 'journal_entry_list.html'

	def get_queryset(self):
		return Journal_Entry.objects.filter(journal=self.kwargs['pk'])

	def get_context_data(self, **kwargs):
		context = super(ListJournalEntriesView, self).get_context_data(**kwargs)
		context['title'] = Journal.objects.get(id=self.kwargs['pk']).name
		context['journal_id'] = self.kwargs['pk']
		return context

class CreateJournalEntryView(CreateView):
	# TODO!
	# the journal id is being passed in as a kwarg['pk']
	# do ike CreateJournalView and use a custom form that excludes
	# journal_entry.journal and sets it using the kwarg['pk']
	# need a separate create and edit view now?

	model = Journal_Entry
	template_name = 'edit_journal_entry.html'

	def get_success_url(self):
		return reverse('journal_entry_list', kwargs={'pk': self.kwargs['journal_id']})

	def get_context_data(self, **kwargs):
		context = super(CreateJournalEntryView, self).get_context_data(**kwargs)
		context['action'] = reverse('journal_entry_new', kwargs={'journal_id': self.kwargs['journal_id']})
		context['journal_id'] = self.kwargs['journal_id']
		return context


class UpdateJournalEntryView(UpdateView):

	model = Journal_Entry
	template_name = 'edit_journal_entry.html'

	def get_success_url(self):
		return reverse('journal_entry_list', kwargs={'pk': self.kwargs['journal_id']})

	def get_context_data(self, **kwargs):
		context = super(UpdateJournalEntryView, self).get_context_data(**kwargs)
		context['action'] = reverse('journal_entry_edit', kwargs={'journal_id': self.kwargs['journal_id'], 'pk': self.get_object().id})
		context['journal_id'] = self.kwargs['journal_id']
		return context


class DeleteJournalEntryView(DeleteView):

	model = Journal_Entry
	template_name = 'delete_journal_entry.html'

	def get_success_url(self):
		return reverse('journal_entry_list', kwargs={'pk': self.kwargs['journal_id']})

	def get_context_data(self, **kwargs):
		context = super(DeleteJournalEntryView, self).get_context_data(**kwargs)
		context['journal_id'] = self.kwargs['journal_id']
		return context


class DetailJournalEntryView(DetailView):

	model = Journal_Entry
	template_name = 'detail_journal_entry.html'

	def get_context_data(self, **kwargs):
		context = super(DetailJournalEntryView, self).get_context_data(**kwargs)
		context['journal_id'] = self.kwargs['journal_id']
		return context



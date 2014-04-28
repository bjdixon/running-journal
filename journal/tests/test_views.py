from datetime import date

from django.test.client import Client, RequestFactory
from django.test import TestCase
from django.core.urlresolvers import reverse

from journal.views import *
from journal.tests.utils import create_journal_entry

class JournalEntryListViewTests(TestCase):
	"""Journal entry list view tests"""

	def test_journals_in_the_context(self):
		client = Client()
		response = client.get(reverse('journal_entry_list'))
		self.assertEqual(list(response.context['object_list']), [])

		Journal_Entry.objects.create(route='a path', distance_in_kilometers=10)
		response = client.get(reverse('journal_entry_list'))
		self.assertEqual(response.context['object_list'].count(), 1)

	def test_journals_in_the_context_request_factory(self):
		factory = RequestFactory()
		request = factory.get(reverse('journal_entry_list'))
		response = ListJournalEntriesView.as_view()(request)
		self.assertEqual(list(response.context_data['object_list']), [])

		Journal_Entry.objects.create(route='a path', distance_in_kilometers=10)
		response = ListJournalEntriesView.as_view()(request)
		self.assertEqual(response.context_data['object_list'].count(), 1)

	def test_uses_correct_template(self):
		response = self.client.get(reverse('journal_entry_list'))
		self.assertTemplateUsed(response, 'journal_entry_list.html')


class CreateJournalEntryViewTests(TestCase):
	""" Create journal entry view tests"""

	def test_creating_journal_entry(self):
		response = self.client.post(
			reverse('journal_entry_new'),	
			data={
				'route': 'route',
				'distance_in_kilometers': '10',
				'date': str(date.today()),
				'duration': '30',
			}
		)
		self.assertEqual(Journal_Entry.objects.all().count(), 1)
		entry = Journal_Entry.objects.all()[0]
		self.assertEqual(entry.route, 'route')

	def test_uses_correct_template(self):
		response = self.client.get(reverse('journal_entry_new'))
		self.assertTemplateUsed(response, 'edit_journal_entry.html')


class UpdateJournalEntryViewTests(TestCase):
	""" Update journal entry view tests"""

	def test_updating_journal_entry(self):
		create_journal_entry()
		self.assertEqual(Journal_Entry.objects.all().count(), 1)
		response = self.client.post(
			reverse('journal_entry_edit', kwargs={'pk': 1}),
			data={
				'route': 'new route',
				'distance_in_kilometers': 10,
				'date': str(date.today()),
				'duration': '30',
			}
		)
		self.assertEqual(Journal_Entry.objects.all().count(), 1)
		entry = Journal_Entry.objects.all()[0]
		self.assertEqual(entry.route, 'new route')

	def test_uses_correct_template(self):
		create_journal_entry()
		response = self.client.get(reverse('journal_entry_edit', kwargs={'pk': 1}))
		self.assertTemplateUsed(response, 'edit_journal_entry.html')


class DeleteJournalEntryViewTests(TestCase):
	"""Delete journal entry view tests"""

	def test_deleting_journal_entry(self):
		create_journal_entry()
		self.assertEqual(Journal_Entry.objects.all().count(), 1)
		response = self.client.post(
			reverse('journal_entry_delete', kwargs={'pk': 1}),
		)
		self.assertEqual(Journal_Entry.objects.all().count(), 0)

	def test_uses_correct_template(self):
		create_journal_entry()
		response = self.client.get(reverse('journal_entry_delete', kwargs={'pk': 1}))
		self.assertTemplateUsed(response, 'delete_journal_entry.html')

class DetailJournalEntryViewTests(TestCase):
	"""Journal entry details view tests"""

	def test_viewing_entry_details(self):
		journal_entry = create_journal_entry()
		journal_entry.notes = 'this is a note'
		journal_entry.save()
		response = self.client.get(reverse('journal_entry_detail', kwargs={'pk': 1}))
		self.assertEqual(
			response.context_data['journal_entry'].route,
			'route'
		)
		self.assertEqual(
			response.context_data['journal_entry'].distance_in_kilometers,
			10.0	
		)
		self.assertEqual(
			response.context_data['journal_entry'].date,
			date.today()
		)
		self.assertEqual(
			response.context_data['journal_entry'].duration,
			30
		)
		self.assertEqual(
			response.context_data['journal_entry'].notes,
			'this is a note'
		)

	def test_uses_correct_template(self):
		create_journal_entry()
		response = self.client.get(reverse('journal_entry_detail', kwargs={'pk': 1}))
		self.assertTemplateUsed(response, 'detail_journal_entry.html')


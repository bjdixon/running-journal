from datetime import date

from django.test.client import Client, RequestFactory
from django.test import TestCase

from journal.views import *


class JournalEntryListViewTests(TestCase):
	"""Journal entry list view tests"""

	def test_journals_in_the_context(self):
		client = Client()
		response = client.get('/journal/')
		self.assertEqual(list(response.context['object_list']), [])

		Journal_Entry.objects.create(route='a path', distance_in_kilometers=10)
		response = client.get('/journal/')
		self.assertEqual(response.context['object_list'].count(), 1)

	def test_journals_in_the_context_request_factory(self):
		factory = RequestFactory()
		request = factory.get('/journal/')
		response = ListJournalEntriesView.as_view()(request)
		self.assertEqual(list(response.context_data['object_list']), [])

		Journal_Entry.objects.create(route='a path', distance_in_kilometers=10)
		response = ListJournalEntriesView.as_view()(request)
		self.assertEqual(response.context_data['object_list'].count(), 1)

	def test_uses_correct_template(self):
		response = self.client.get('/journal/')
		self.assertTemplateUsed(response, 'journal_entry_list.html')


class CreateJournalEntryViewTests(TestCase):

	def test_creating_journal_entry(self):
		response = self.client.post(
			'/journal/new/entry/',
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
		response = self.client.get('/journal/new/entry/')
		self.assertTemplateUsed(response, 'edit_journal_entry.html')


class UpdateJournalEntryViewTests(TestCase):

	def test_updating_journal_entry(self):
		pass

	def test_uses_correct_template(self):
		Journal_Entry.objects.create(
			route='route',
			distance_in_kilometers=10,
			date=date.today(),
			duration=30
		)
		response = self.client.get('/journal/edit/entry/1/')
		self.assertTemplateUsed(response, 'edit_journal_entry.html')


class DeleteJournalEntryViewTests(TestCase):

	def test_deleting_journal_entry(self):
		pass

	def test_uses_correct_template(self):
		pass


class DetailJournalEntryViewTests(TestCase):

	def test_viewing_entry_details(self):
		pass

	def test_uses_correct_template(self):
		pass


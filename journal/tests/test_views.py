from datetime import date

from django.test.client import Client, RequestFactory
from django.test import TestCase
from unittest import skip
from django.core.urlresolvers import reverse
from django.http import HttpRequest

from journal.views import *
from journal.tests.utils import *


class LoggedInTests(TestCase):
	"""Users have to be logged in to do most things"""

	def test_user_cant_use_create_journal_view_unless_logged_in(self):
		pass

	def test_user_cant_use_journal_list_view_unless_logged_in(self):
		pass

	def test_user_cant_use_list_journal_entries_view_unless_logged_in(self):
		pass

	def test_user_cant_use_create_journal_entry_view_unless_logged_in(self):
		pass

	def test_user_cant_use_delete_journal_entry_view_unless_logged_in(self):
		pass

	def test_user_cant_use_journal_entry_detail_view_unless_logged_in(self):
		pass


class CreateJournalViewTests(TestCase):
	"""Create journal view tests"""

	def test_user_can_create_journal(self):
		user = create_user()
		response = self.client.post(
			reverse('journal_create'),	
			data={'name': 'test'}
		)
		self.assertEqual(Journal.objects.all().count(), 1)
		self.assertEqual(Journal.objects.all()[0].name, 'test')

	def test_journal_is_assigned_to_correct_user_as_owner(self):
		user = create_user()
		response = self.client.post(
			reverse('journal_create'),
			data={'name': 'test'}
		)
		self.assertEqual(Journal.objects.all()[0].owner, user)

	def test_uses_correct_template(self):
		user = create_user()
		response = self.client.get(reverse('journal_create'))
		self.assertTemplateUsed(response, 'journal_create.html')


class JournalListViewTests(TestCase):
	"""Journal list view tests"""

	def test_user_can_view_journals(self):
		create_journal(user=create_user())
		response = self.client.get(reverse('journal'))
		self.assertContains(response.content, 'journal (list)')

	def test_only_owner_can_see_their_journals(self):
		pass

	def test_correct_template(self):
		pass


class JournalEntryListViewTests(TestCase):
	"""Journal entry list view tests"""

	@skip
	def test_journals_in_the_context(self):
		client = Client()
		response = client.get(reverse('journal_entry_list'))
		self.assertEqual(list(response.context['object_list']), [])

		Journal_Entry.objects.create(route='a path', distance_in_kilometers=10)
		response = client.get(reverse('journal_entry_list'))
		self.assertEqual(response.context['object_list'].count(), 1)

	@skip
	def test_only_owner_can_see_their_journal_entry_lists(self):
		pass

	@skip
	def test_uses_correct_template(self):
		response = self.client.get(reverse('journal_entry_list'))
		self.assertTemplateUsed(response, 'journal_entry_list.html')


class CreateJournalEntryViewTests(TestCase):
	""" Create journal entry view tests"""

	@skip
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

	@skip
	def test_journal_entry_is_assigned_to_correnct_user_as_owner(self):
		pass

	@skip
	def test_uses_correct_template(self):
		response = self.client.get(reverse('journal_entry_new'))
		self.assertTemplateUsed(response, 'edit_journal_entry.html')


class UpdateJournalEntryViewTests(TestCase):
	""" Update journal entry view tests"""

	@skip
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

	@skip
	def test_only_owner_can_update_their_journal_entries(self):
		pass

	@skip
	def test_uses_correct_template(self):
		create_journal_entry()
		response = self.client.get(reverse('journal_entry_edit', kwargs={'pk': 1}))
		self.assertTemplateUsed(response, 'edit_journal_entry.html')


class DeleteJournalEntryViewTests(TestCase):
	"""Delete journal entry view tests"""

	@skip
	def test_deleting_journal_entry(self):
		create_journal_entry()
		self.assertEqual(Journal_Entry.objects.all().count(), 1)
		response = self.client.post(
			reverse('journal_entry_delete', kwargs={'pk': 1}),
		)
		self.assertEqual(Journal_Entry.objects.all().count(), 0)

	@skip
	def test_only_owner_can_delete_their_journal_entries(self):
		pass

	@skip
	def test_uses_correct_template(self):
		create_journal_entry()
		response = self.client.get(reverse('journal_entry_delete', kwargs={'pk': 1}))
		self.assertTemplateUsed(response, 'delete_journal_entry.html')

class DetailJournalEntryViewTests(TestCase):
	"""Journal entry details view tests"""

	@skip
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

	@skip
	def test_only_owner_can_see_their_journal_entry_details(self):
		pass

	@skip
	def test_uses_correct_template(self):
		create_journal_entry()
		response = self.client.get(reverse('journal_entry_detail', kwargs={'pk': 1}))
		self.assertTemplateUsed(response, 'detail_journal_entry.html')


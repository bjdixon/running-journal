from django.test.client import Client, RequestFactory
from django.test import TestCase

from journal.views import *


class JournalListViewTests(TestCase):
	"""Journal list view tests"""

	def test_journals_in_the_context(self):
		client = Client()
		response = client.get('/')
		self.assertEqual(list(response.context['object_list']), [])

		Journal_Entry.objects.create(route='a path', distance_in_kilometers=10)
		response = client.get('/')
		self.assertEqual(response.context['object_list'].count(), 1)

	def test_journals_in_the_context_request_factory(self):
		factory = RequestFactory()
		request = factory.get('/')
		response = ListJournalView.as_view()(request)
		self.assertEqual(list(response.context_data['object_list']), [])

		Journal_Entry.objects.create(route='a path', distance_in_kilometers=10)
		response = ListJournalView.as_view()(request)
		self.assertEqual(response.context_data['object_list'].count(), 1)



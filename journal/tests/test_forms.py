from django.test.client import Client, RequestFactory
from django.test import TestCase

from rebar.testing import flatten_to_dict

from journal.views import *
#from journal import forms


class EditJournalFormTests(TestCase):
	"""Test Journal edit form"""

	def test_journals_in_the_context(self):
		pass

from datetime import date
from django.test import TestCase

from journal.models import Journal_Entry


class JournalEntryTests(TestCase):
	"""Journal_Entry model tests"""

	def test_str(self):
		journal_entry = Journal_Entry(route='path', distance_in_kilometers=10)
		todays_date = str(date.today())
		self.assertEqual(str(journal_entry), 'path 10KM ' + todays_date)

	def test_get_absolute_url(self):
		pass


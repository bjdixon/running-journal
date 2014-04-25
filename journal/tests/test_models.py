from datetime import date
from django.test import TestCase

from journal.models import Journal_Entry


class JournalTests(TestCase):
	"""Journal model tests"""

	def test_str(self):
		journal_entry = Journal_Entry(route='path', distance_in_kilometers=10)
		todays_date = str(date.today())
		self.assertEqual(str(journal_entry), 'path 10KM ' + todays_date)


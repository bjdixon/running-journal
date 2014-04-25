from datetime import date
from django.test import TestCase

from journal.models import Journal


class JournalTests(TestCase):
	"""Journal model tests"""

	def test_str(self):
		journal = Journal(route='path', distance_in_kilometers=10)
		todays_date = str(date.today())
		self.assertEqual(str(journal), 'path 10KM ' + todays_date)


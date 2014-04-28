from datetime import date
from django.test import TestCase
from django.core.urlresolvers import reverse

from journal.models import Journal_Entry
from journal.tests.utils import create_journal_entry


class JournalEntryTests(TestCase):
	"""Journal_Entry model tests"""

	def test_str(self):
		journal_entry = create_journal_entry()
		todays_date = str(date.today())
		self.assertEqual(str(journal_entry), 'route 10KM ' + todays_date)

	def test_get_absolute_url(self):
		journal_entry = create_journal_entry()
		self.assertEqual(
			journal_entry.get_absolute_url(), 
			reverse('journal_entry_detail', kwargs={'pk': 1})
		)


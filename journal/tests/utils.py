from datetime import date

from journal.views import *

def create_journal_entry():
		return Journal_Entry.objects.create(
			route='route',
			distance_in_kilometers=10,
			date=date.today(),
			duration=30
		)



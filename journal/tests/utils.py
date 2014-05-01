from datetime import date
from django.http import HttpRequest
from django.contrib.auth import get_user_model
User = get_user_model()

from journal.views import *

def create_journal_entry(journal):
	return Journal_Entry.objects.create(
		route='route',
		distance_in_kilometers=10,
		date=date.today(),
		duration=30,
		journal=journal
	)

def create_journal(user):
	return Journal.objects.create(
		owner=user,
		name='journal'
	)

def create_user(request=HttpRequest(), email='user@email.com'):
	return User.objects.create(email=email)


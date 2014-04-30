from datetime import date

from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings


class Journal(models.Model):

	owner = models.ForeignKey(settings.AUTH_USER_MODEL)
	name = models.CharField(default='Running Journal', max_length=140) 


class Journal_Entry(models.Model):

	route = models.CharField(max_length=140)
	distance_in_kilometers = models.FloatField()
	notes = models.TextField(blank=True, null=True)
	date = models.DateField(default=date.today())
	duration = models.IntegerField(default=30)
	journal = models.ForeignKey(Journal, blank=True, null=True)
	
	def __str__(self):
		return ' '.join([
			self.route,
			str(self.distance_in_kilometers) + 'KM',
			str(self.date),
		])

	def get_absolute_url(self):
		return reverse('journal_entry_detail', kwargs={'journal_id': self.journal.id, 'pk': self.id})


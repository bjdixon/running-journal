from django.db import models
from datetime import date
from django.core.urlresolvers import reverse


class Journal_Entry(models.Model):

	route = models.CharField(max_length=140)
	distance_in_kilometers = models.FloatField()
	notes = models.TextField(blank=True, null=True)
	date = models.DateField(default=date.today())
	duration = models.IntegerField(default=30)
	
	def __str__(self):
		return ' '.join([
			self.route,
			str(self.distance_in_kilometers) + 'KM',
			str(self.date),
		])

	def get_absolute_url(self):
		return reverse('journal_entry_detail', kwargs={'pk': self.id})


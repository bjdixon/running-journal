from django.db import models
from datetime import date


class Journal(models.Model):

	route = models.CharField(max_length=140)
	distance_in_kilometers = models.FloatField()
	notes = models.TextField(blank=True, null=True)
	date = models.DateField(default=date.today())
	
	def __str__(self):
		return ' '.join([
			self.route,
			str(self.distance_in_kilometers) + 'KM',
			str(self.date),
		])


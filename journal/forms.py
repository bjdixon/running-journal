from django import forms

from journal.models import Journal


class CreateJournalForm(forms.models.ModelForm):
	
	class Meta:
		model = Journal
		exclude = ('owner',)


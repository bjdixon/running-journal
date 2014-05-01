from django import forms

from journal.models import Journal, Journal_Entry


class CreateJournalForm(forms.models.ModelForm):
	
	class Meta:
		model = Journal
		exclude = ('owner',)

class CreateJournalEntryForm(forms.models.ModelForm):

	class Meta:
		model = Journal_Entry
		exclude = ('journal',)

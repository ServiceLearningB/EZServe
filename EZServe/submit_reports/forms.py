from django import forms
from django.forms import Textarea, ModelForm, widgets
from .models import SubmitReport
from django.db import models
from django.contrib.admin.widgets import FilteredSelectMultiple

class SubmitReportForm(forms.ModelForm):
	class Meta:
		model = SubmitReport
		exclude = ['submitter']
		widgets = {
			#'courses': forms.SelectMultiple(),
			'summary': Textarea(attrs={'cols': 50, 'rows': 3}),
		}

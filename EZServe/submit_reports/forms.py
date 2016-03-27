from django import forms
from django.forms import Textarea, ModelForm, widgets
from .models import SubmitReport, Partner
from django.db import models
from django.contrib.admin.widgets import FilteredSelectMultiple

class SubmitReportForm(forms.ModelForm):
	class Meta:
		model = SubmitReport
		exclude = ['submitter', 'status']
		widgets = {
			#'courses': forms.SelectMultiple(),
			'summary': Textarea(attrs={'cols': 50, 'rows': 3}),
		}

class AddPartnerForm(forms.ModelForm):
	class Meta:
		model = Partner
		fields = ['name', 'is_active']



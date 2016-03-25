from django import forms
from .models import SubmitReport
from django.contrib.admin import widgets

class SubmitReportForm(forms.ModelForm):
	class Meta:
		model = SubmitReport
		fields = '__all__'

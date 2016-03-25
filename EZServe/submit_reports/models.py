from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Student(models.Model):
	username = models.CharField(max_length=100, null=False, blank=False)
	password = models.CharField(max_length=15, null=False, blank=False)

class SubmitReport(models.Model):
	start_time = models.TimeField(auto_now_add=False, auto_now=False)
	end_time = models.TimeField(auto_now_add=False, auto_now=False)
	#start_date = models.DateField(auto_now_add=False, auto_now=False)
	#end_date = models.DateField(auto_now_add=False, auto_now=False)
	summary = models.CharField(max_length=150, null=True, blank=True)
	submitter = models.ForeignKey(Student, blank=True, null=True)



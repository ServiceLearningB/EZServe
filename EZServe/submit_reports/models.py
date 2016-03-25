from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Student(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
	nuid = models.IntegerField(null=False, blank=False, default=0)

class SubmitReport(models.Model):
	start_time = models.TimeField(auto_now_add=False, auto_now=False)
	end_time = models.TimeField(auto_now_add=False, auto_now=False)
	#start_date = models.DateField(auto_now_add=False, auto_now=False)
	#end_date = models.DateField(auto_now_add=False, auto_now=False)
	summary = models.CharField(max_length=150, null=True, blank=True)
	submitter = models.ForeignKey(Student, blank=True, null=True)


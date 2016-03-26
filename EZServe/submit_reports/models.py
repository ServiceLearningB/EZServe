from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from datetime import date

# Create your models here.
class Student(models.Model):
	first_name = models.CharField(max_length=30, null=True)
	last_name = models.CharField(max_length=30, null=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
	nuid = models.IntegerField(null=False, blank=False, default=0)

	def __str__(self):
		return "%S %S" % (self.first_name, self.last_name)

class Faculty(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

class Course(models.Model):
	instructor = models.ForeignKey(Faculty, on_delete=models.CASCADE, null=True)


class Partner(models.Model):
	pass

class SubmitReport(models.Model):
	start_time = models.TimeField(auto_now_add=False, auto_now=False)
	end_time = models.TimeField(auto_now_add=False, auto_now=False)
	#start_date = models.DateField(auto_now_add=False, auto_now=False, default=date.today)
	#end_date = models.DateField(auto_now_add=False, auto_now=False, default=date.today)
	summary = models.CharField(max_length=150, null=True, blank=True)
	submitter = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
		


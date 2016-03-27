from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from datetime import date, time, datetime
from django.core.validators import RegexValidator

# Create your models here.

#list of all choices for colleges
College = (
		('CAMD', 'CAMD'),
		('CCIS', 'CCIS'),
		('COS', 'COS'),
		('CSSH', 'CSSH'),
		('BOUVE', 'BOUVE'),
		('DMSB', 'DMSB'),
		('COE', 'COE'),
		('LAW', 'LAW'),
		('CPS', 'CPS'),
		('PROVOST', 'PROVOST'),
	)

ApprovalStatus = (
		('PENDING', 'PENDING'),
		('APPROVED', 'APPROVED'),
		('REJECTED', 'REJECTED'),
	)

ServiceType = (
		('DIRECT_SERVICE', 'Direct Service'),
		('TRAINING', 'Training'),
		('IND_RESEARCH', 'Individual Research'),
		('TEAM_RESEARCH', 'Team Research'),
	)

# User Classes
####################################################

class Student(models.Model):
	numeric = RegexValidator(r'^[0-9]*$', 'only numbers allowed')

	user = models.OneToOneField(User, null=True)
	nuid = models.IntegerField(null=False, blank=False, default=0)
	courses = models.ManyToManyField('Course')
	grad_year = models.CharField(validators=[numeric], max_length=4, null=True)

	def __unicode__(self):
		return self.user.first_name + " " + self.user.last_name + " (" + str(self.nuid) + ")"

class Faculty(models.Model):
	user = models.OneToOneField(User, null=True)

	def __unicode__(self):
		return self.user.first_name + " " + self.user.last_name


class Staff(models.Model):
	user = models.OneToOneField(User, null=True)
	courses = models.ManyToManyField('Course')

	def __unicode__(self):
		return self.user.first_name + " " + self.user.last_name

class AdminStaff(models.Model):
	user = models.OneToOneField(User, null=True)

	def __unicode__(self):
		return self.user.first_name + " " + self.user.last_name

# Data Classes
######################################################

class SubmitReport(models.Model):

	start_time = models.DateTimeField(auto_now_add=False, auto_now=False, default=datetime.now)
	end_time = models.DateTimeField(auto_now_add=False, auto_now=False, default=datetime.now)
	courses = models.ManyToManyField('Course')
	service_type = models.CharField(max_length=14, null=True, blank=False)
	status = models.CharField(max_length=8, choices=ApprovalStatus, default='PENDING', null=False, blank=False)
	summary = models.CharField(max_length=150, null=True, blank=True)
	submitter = models.ForeignKey(Student, null=True)
		
	def __unicode__(self):
		return (self.submitter.__unicode__() + " start: " + self.start_time.strftime('%Y-%m-%d %H:%M') +
		" end: " + self.end_time.strftime('%Y-%m-%d %H:%M'))

class Course(models.Model):
	numeric = RegexValidator(r'^[0-9]*$', 'only numbers allowed')
	instructor = models.ForeignKey(Faculty, null=True, blank=False)
	college = models.CharField(choices=College, default='NONE', max_length=7)
	course_number = models.CharField(max_length=10, null=True)
	CRN = models.CharField(validators=[numeric], max_length=5)

	def __unicode__(self):
		return self.course_number + ": " + self.CRN


class Partner(models.Model):
	name = models.CharField(max_length=100, null=True, default='New Partner Organization')
	is_active = models.BooleanField(default=True, null=False)

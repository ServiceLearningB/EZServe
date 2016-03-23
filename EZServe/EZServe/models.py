from django.db import models
from datetime import datetime


class Report(models.Model):
	"""Represents an hours report"""
	def __init__(self, start_time, end_time, partner, course, student, nuid, service_type, approval_status):
		super(Report, self)
		self.start_time = start_time
		self.end_time = end_time
		self.partner = partner
		self.course = course
		self.student = student
		self.nuid = nuid
		self.service_type = service_type
		self.approval_status = approval_status
		

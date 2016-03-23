from django.db import models
from datetime import datetime
from enum import Enum


class College(Enum):
	"""Represents one of the colleges at Northeastern"""
	CCIS = 0
	COS = 1
	CSSH = 2
	BOUVE = 3
	DMSB = 4
	COE = 5
	LAW = 6
	CPS = 7
	PROVOST = 8
	#ERROR = -1 # in case we ever want to return colleges and there is an error

class ServiceType(Enum):
	"""Represents the types of service that may be reported to SL"""
	TRAINING = 0
	DIRECT_SERVICE = 1
	IND_RESEARCH = 2
	TEAM_RESEARCH = 3
	#ERROR = -1 # in case we ever want to return service types and there is an error

class ApprovalStatus(Enum):
	"""Represents the status of a report"""
	PENDING = 0
	APPROVED = 1
	REJECTED = 2
	SAVED = 3
	#ERROR = -1 # in case we ever want to return approval statuses and there is an error

class Report(models.Model):
	"""Represents an hours report"""
	def __init__(self, start_time, end_time, partner, course, student, nuid, service_type, approval_status):
		try:
			assert type(start_time) in (datetime)
			assert type(end_time) in (datetime)
			assert type(partner) in (Partner)
			assert type(course) in (Course)
			assert type(student) in (Student)
			assert type(nuid) in (int)
			assert type(service_type) in (ServiceType)
			assert type(approval_status) in (ApprovalStatus)
		except AssertionError:
			raise ValueError("Input not of proper type")
		try:
			assert start_time.year > 0
			assert end_time.year == start_time.year
			assert 0 <= end_time.month - start_time.month <= 1
			assert 0 <= end_time.month - start_time.month <= 1
			assert start_time < end_time


		except AssertionError:
			raise
		super(Report, self)
		self.start_time = start_time
		self.end_time = end_time
		self.partner = partner
		self.course = course
		self.student = student
		self.nuid = nuid
		self.service_type = service_type
		self.approval_status = approval_status
		
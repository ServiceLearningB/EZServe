# CS4500 Spring 2016
# Team-1 Service-Learning-B
# Basic Test Case for EZServe Project

from django.contrib.auth.models import User
from django.test import TestCase
from ezserve.models import Student, Faculty, Ta, Admin, User, Date, Partner, Course, ServiceType, ApprovalStatus
"""
def setUp(self):
	user_student = User.objects.create_user(
		username='jsmith', email='smith.j@husky.neu.edu', password='secret')
	user_student.save()
	user_admin = User.objects.create_user(
		username='admin', email='admin@email.com', password='secret')
	user_admin.is_superuser
	user_admin.save()
	user_TA = User.objects.create_user(
		username='ta', email = 'ta@email.com', password='secret')
	user_TA.is_staff
	user_TA.save()
	user_faculty = User.object.create_user(
		username='faculty', email='faculty@email.com', password='secret')
	user_faculty.is_staff
	user_faculty.save()

class StudentTestCase(TestCase):
	def action_test(self):
		self.assertEqual(student.pull('jsmith'), Student.objects.get(name="John Smith"))
		self.assertEqual(student.submit('jsmith'), Student.hours = )


class FacultyTestCase(TestCase):
	def action_test(self):
		self.assertEqual(faculty.pull("John Smith"), )
		

class TaTestCase(TestCase):
	def action_test(self):
		self.assertEqual(ta.pull())
		self.assertEqual(ta.approve())
		self.assertEqual(ta.reject())

class AdminTestCase(TestCase):
	def action_test(self):
		self.assertEqual(admin.pull())
		self.assertEqual(admin.approve())
		self.assertEqual(admin.reject())
		self.assertEqual(admin.addPartner())
		self.assertEqual(admin.setPartnerActivity())
		self.assertEqual(admin.addCourse())
		self.assertEqual(admin.addStudent())
		self.assertEqual(admin.giveTaPermission())
		self.assertEqual(admin.addTA())

class PermissionsTestCase(TestCase):
	def student_test(self):

	def faculty_test(self):

	def ta_test(self):

	def admin_test(self):

"""
		
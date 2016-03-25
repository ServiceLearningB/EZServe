from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from submit_reports.models import Student

class StudentUserTestCase(TestCase):
	fixtures = ['users.json', 'students.json']

	def testProperAssociation(self):
		manwich = User.objects.get(pk=2)
		manwich_student = Student.objects.get(pk=1)
		self.assertEqual(manwich.username, 'dummy')
		self.assertEqual(manwich_student.user, manwich)
		self.assertEqual(manwich.student, manwich_student)
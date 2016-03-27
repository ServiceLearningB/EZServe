from django.shortcuts import render, render_to_response, RequestContext
from .forms import SubmitReportForm, AddPartnerForm
from .models import SubmitReport, Student, Faculty, Staff
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.views.generic.list import ListView
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required,user_passes_test, permission_required
from django.contrib.auth.mixins import UserPassesTestMixin
# Create your views here.

@login_required
def submit_page(request):
	'''Page for submitting records, accessible to student users'''
	student = Student.objects.get(user=request.user)
	form = SubmitReportForm(request.POST or None)
	if form.is_valid():
		save_form = form.save(commit=False)
		save_form.submitter=student
		save_form.save()
		save_form.save_m2m()
		return HttpResponseRedirect('/accounts/loggedin')
	return render_to_response("submit_report.html",
		locals(),
		context_instance=RequestContext(request))


class FacultyView(UserPassesTestMixin, ListView):
	"""Page for faculty to view student records"""
	model = Faculty
	#form = FacultyQueryForm(request.POST or None)

	def get_queryset(self):
		if form.is_valid():
			return SubmitReport.objects.filter()

	def test_func(self):
		return self.request.user.is_superuser or self.request.user.faculty is not None


def login_view(request):
	"""Page for logging in"""
	c = {}
	c.update(csrf(request))
	return render_to_response('login.html', c)


def auth_view(request):
	"""Redirects users after login, or if login fails"""
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)
	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/accounts/loggedin')
	else:
		return HttpResponseRedirect('/accounts/invalid')


def logout_view(request):
	"""Page for users which have just logged out"""
	auth.logout(request)
	return render_to_response('logout.html')


@user_passes_test(lambda u: u.is_superuser or u.student is not None)
def student_logged_in_view(request):
	"""Homepage for logged in users"""
	return render_to_response('loggedin.html',
		{'username': request.user.username})


def invalid_login_view(request):
	"""Page for users who have not successfully logged in"""
	return render_to_response('invalid_login.html')


@user_passes_test(lambda u: u.is_superuser or u.adminstaff is not None)
def admin_home_view(request):
	"""Homepage for logged in admin"""
	return render_to_response('admin_loggedin.html',
		{'username': request.user.username})

@user_passes_test(lambda u: u.is_superuser or u.adminstaff is not None)
def add_partners_view(request):
	'''Page for adding partners'''
	form = AddPartnerForm(request.POST or None)
	if form.is_valid():
		save_form = form.save(commit=False)
		save_form.save()
		if '_add_another' in request.POST:
			return HttpResponseRedirect('/admin/add_partner')
		return HttpResponseRedirect('/admin/home')
	return render_to_response("add_partner.html",
		locals(),
		context_instance=RequestContext(request))
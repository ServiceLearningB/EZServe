from django.shortcuts import render, render_to_response, RequestContext
from .forms import SubmitReportForm
from .models import SubmitReport, Student
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
# Create your views here.

def submit_page(request):
	student = Student.objects.filter(nuid=nuid)
	form = SubmitReportForm(request.POST or None)
	if form.is_valid():
		save_form = form.save(commit=False)
		save_form.save()
	return render_to_response("submit_report.html",
		locals(),
		context_instance=RequestContext(request))

def login_view(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('login.html')
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)

		else:
			error = u'account disabled'
			return errorHandle(error)

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)
	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/accounts/loggedin')
	else:
		return HttpResponseRedirect('/accounts/invalid')

def logout_view(request):
	auth.logout(request)
	return render_to_response('logout.html')

def logged_in_view():
	return render_to_response('loggedin.html',
		{'username': request.user.username})

def invalid_login_view(request):
	return render_to_response('invalid_login.html')
from django.shortcuts import render, render_to_response, RequestContext
from .forms import SubmitReportForm
from .models import SubmitReport
from django.views.generic.list import ListView
# Create your views here.

def submit_page(request):
	form = SubmitReportForm(request.POST or None)
	if form.is_valid():
		save_form = form.save(commit=False)
		save_form.save()
	return render_to_response("submit_report.html",
		locals(),
		context_instance=RequestContext(request))

class StudentListView(ListView):

	model = SubmitReport

	def get_context_data(self, **kwargs):
		context = super(StudentListView, self).get_context_data(**kwargs)
		return context
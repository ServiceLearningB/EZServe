from django.contrib import admin

# Register your models here.
from .models import SubmitReport, Student

class SubmitReportAdmin(admin.ModelAdmin):
	class Meta:
		model = SubmitReport

class StudentAdmin(admin.ModelAdmin):
	class Meta:
		model = Student

admin.site.register(SubmitReport, SubmitReportAdmin)
admin.site.register(Student, StudentAdmin)
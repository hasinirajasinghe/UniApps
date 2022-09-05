from django.contrib import admin
from .models import Counselor, Applicant, Application

class CounselorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'password', 'university')
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'major', 'enrollment_status')

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('applicant','academic_year', 'intended_start', 'intended_major', 'status', 'last_updated', 'school_last_attended', 'gpa')

# Register your models here.
admin.site.register(Counselor, CounselorAdmin)
admin.site.register(Applicant, ApplicantAdmin)
admin.site.register(Application, ApplicationAdmin)
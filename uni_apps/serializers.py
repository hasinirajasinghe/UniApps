from calendar import c
from dataclasses import fields
from rest_framework import serializers
from .models import Counselor, Applicant, Application

class CounselorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counselor
        fields = ('name', 'email', 'password', 'university')

class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = ('name', 'email', 'phone_number', 'major', 'enrollment_status')

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('applicant','academic_year', 'intended_start', 'intended_major', 'status', 'last_updated', 'school_last_attended', 'gpa')
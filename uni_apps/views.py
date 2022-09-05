from django.shortcuts import render
from rest_framework import generics
from .serializers import CounselorSerializer, ApplicantSerializer, ApplicationSerializer
from .models import Counselor, Applicant, Application

# Create your views here.
class ApplicantList(generics.ListCreateAPIView):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer

class ApplicantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Applicant.objects.all()
    lookup_url_kwarg = 'id'
    serializer_class = ApplicantSerializer

class ApplicationList(generics.ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

class ApplicationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Application.objects.all()
    lookup_url_kwarg = 'id'
    serializer_class = ApplicantSerializer
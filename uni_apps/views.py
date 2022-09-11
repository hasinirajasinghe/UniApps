from os import major
from django.shortcuts import render
from rest_framework import generics
from .serializers import ApplicantSerializer, ApplicationSerializer
from .models import Applicant, Application
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth import get_user_model
from django.conf import settings
from rest_framework.permissions import IsAuthenticated
import jwt
from .serializers import UserSerializer
from django.http import JsonResponse
User = get_user_model()

# Create your views here.

def get_all_enrollment_status(request):
    enrollment_statuses = Applicant._meta.get_field('enrollment_status').choices
    response = {}
    for status in enrollment_statuses:
        statusKey = status[0]
        statusValue = status[1]
        response[statusKey] = statusValue
    return JsonResponse(response, safe=False)

def get_all_majors(request):
    majors = Applicant._meta.get_field('major').choices
    response = {}
    for major in majors:
        majorKey = major[0]
        majorValue = major[1]
        response[majorKey] = majorValue
    return JsonResponse(response, safe=False)

def get_all_terms(request):
    terms = Application._meta.get_field('intended_start').choices
    response = {}
    for term in terms:
        termKey = term[0]
        termValue = term[1]
        response[termKey] = termValue
    return JsonResponse(response, safe=False)

def get_all_application_status(request):
    application_statuses = Application._meta.get_field('status').choices
    response = {}
    for status in application_statuses:
        statusKey = status[0]
        statusValue = status[1]
        response[statusKey] = statusValue
    return JsonResponse(response, safe=False)
class ApplicantList(generics.ListCreateAPIView):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer
    # permission_classes = [IsAuthenticated]

class ApplicantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Applicant.objects.all()
    lookup_url_kwarg = 'id'
    serializer_class = ApplicantSerializer
    # permission_classes = [IsAuthenticated]

class ApplicationList(generics.ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    # permission_classes = [IsAuthenticated]

class ApplicationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Application.objects.all()
    lookup_url_kwarg = 'id'
    serializer_class = ApplicationSerializer
    # permission_classes = [IsAuthenticated]

class CheckToken(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response('success')

class RegisterView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Registration successful'})

        return Response(serializer.errors, status=422)


class LoginView(APIView):

    def get_user(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            raise PermissionDenied({'message': 'Invalid credentials'})

    def post(self, request):

        email = request.data.get('email')
        password = request.data.get('password')

        user = self.get_user(email)
        if not user.check_password(password):
            raise PermissionDenied({'message': 'Invalid credentials'})

        token = jwt.encode({'sub': user.id}, settings.SECRET_KEY, algorithm='HS256')
        return Response({'token': token, 'message': f'Welcome back {user.username}!'})
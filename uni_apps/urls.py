from django.urls import path
from . import views

urlpatterns = [
    path('applicants/', views.ApplicantList.as_view(), name='applicant_list'),
    path('applicants/<int:id>/', views.ApplicantDetail.as_view(), name='applicant_detail')
]

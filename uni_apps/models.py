from random import choices
from secrets import choice
from django.db import models

# Create your models here.

COMPUTER_SCIENCE = 'CSCI'
CHEMISTRY = 'CHEM'
ENGINEERING = 'ENGI'
BIOLOGY = 'BIOL'
PHYSICS = 'PHYS'
MATHEMATICS = 'MATH'
INFORMATION_TECHNOLOGY = 'ITEC'
BUSINESS_MANAGEMENT = 'BMAN'
FINANCE_AND_ACCOUNTING = 'FIAC'
EDUCATION = 'EDUC'
KINESIOLOGY_AND_PHYSICAL_THERAPY = 'KNPT'
ENVIRONMENTAL_SCIENCE = 'ESCI'
FOREIGN_LANGUAGES = 'FOLA'
DANCE = 'DANC'
MUSIC = 'MUSI'
PERFORMING_ARTS = 'PRAR'
AGRICULTURAL_SCIENCES = 'AGSC'
CULINARY_ARTS = 'CUAR'
FILM_AND_PHOTOGRAPHY = 'FIPH'
FOOD_AND_NUTRITION = 'FDNU'
UNDECIDED = 'UNDC'
MAJOR_CHOICES = [
    (COMPUTER_SCIENCE, 'Computer Science'),
    (CHEMISTRY, 'Chemistry'),
    (ENGINEERING, 'Engineering'),
    (BIOLOGY, 'Biology'),
    (PHYSICS, 'Physics'),
    (MATHEMATICS, 'Mathematics'),
    (INFORMATION_TECHNOLOGY, 'Information Technology'),
    (BUSINESS_MANAGEMENT, 'Business Management'),
    (FINANCE_AND_ACCOUNTING, 'Finance and Accounting'),
    (EDUCATION, 'Education'),
    (KINESIOLOGY_AND_PHYSICAL_THERAPY, 'Kinesiology and Physical Therapy'),
    (ENVIRONMENTAL_SCIENCE, 'Environmental Science'),
    (FOREIGN_LANGUAGES, 'Foreign Languages'),
    (DANCE, 'Dance'),
    (MUSIC, 'Music'),
    (PERFORMING_ARTS, 'Performing Arts'),
    (AGRICULTURAL_SCIENCES, 'Agricultural Sciences'),
    (CULINARY_ARTS, 'Culinary Arts'),
    (FILM_AND_PHOTOGRAPHY, 'Film and Photography'),
    (FOOD_AND_NUTRITION, 'Food and Nutrition'),
    (UNDECIDED, 'Undecided')
]   
class Applicant(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    major = models.CharField(
        max_length=4,
        choices=MAJOR_CHOICES,
        default=UNDECIDED,
    )

    INQUIRY = 'IN'
    ENROLLED = 'EN'
    DEFERRED = 'DF'
    ENROLLEMENT_STATUS_CHOICES = [
        (INQUIRY, 'Inquiry'),
        (ENROLLED, 'Enrolled'),
        (DEFERRED, 'Deferred'),
    ]
    enrollment_status = models.CharField(
        max_length=2,
        choices=ENROLLEMENT_STATUS_CHOICES,
        default=INQUIRY,
    )

    def __str__(self):
        return f"{self.name}"

class Application(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    academic_year = models.CharField(max_length=10)

    FALL = 'FA'
    SPRING = 'SP'
    SUMMER = 'SU'
    INTENDED_START_CHOICES = [
        (FALL, 'Fall'),
        (SPRING, 'Spring'),
        (SUMMER, 'Summer'),
    ]
    intended_start = models.CharField(
        max_length=2,
        choices=INTENDED_START_CHOICES, 
        default=FALL,
    )    
    intended_major = models.CharField(
        max_length=4,
        choices=MAJOR_CHOICES,
        default=UNDECIDED,
    )
    
    IN_PROGRESS = 'IP'
    APPLIED = 'AP'
    PROCESSED = 'PR'
    ACCEPTED = 'AC'
    DEPOSITED = 'DP'
    DENIED = 'DN'
    WAITLISTED = 'WL'
    WITHDRAWN = 'WI'
    STATUS_CHOICES = [
        (IN_PROGRESS, 'In Progress'),
        (APPLIED, 'Applied'),
        (PROCESSED, 'Processed'),
        (ACCEPTED, 'Accepted'),
        (DEPOSITED, 'Deposited'),
        (DENIED, 'Denied'),
        (WAITLISTED, 'Waitlisted'),
        (WITHDRAWN, 'Withdrawn'),
    ]
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES, 
    )

    last_updated = models.DateField()
    school_last_attended = models.CharField(max_length=100)
    gpa = models.DecimalField(max_digits=5, decimal_places=3)

    def __str__(self):
        return f"{self.applicant}, {self.status}"
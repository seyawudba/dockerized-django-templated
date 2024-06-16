from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
# Create your models here.

class CertificateType(models.Model):
    name=models.CharField(max_length=40)
    abbreviation=models.CharField(max_length=5)

class ModeOfTeaching(models.TextChoices):
    FACE_TO_FACE="FF",_("Face-to-face")
    ONLINE="OL",_("Online")
    BLENDER_LEARNING="BL",_("Blender Learning")

class TimeOfStudy(models.TextChoices):
    FULL_TIME="FT",_("Full Time")
    WEEKEND_ONLY="WO",_("Weekend Only")
    MORNING_ONLY="MO",_("Morning Only")
    AFTERNOON_ONLY="AO",_("Afternoon Only")
    EVENING_ONLY="EO",_("Evening Only")
    ONLINE_ONLY="OL",_("Online Only")

class RegionChoices(models.TextChoices):
    GREATER_ACCRA="GA",_("Greater Accra")
    NORTHERN="NR",_("Northern")
    ASHANTI="AS",_("Ashanti")
    WESTERN="WR",_("Western")
    VOLTA="VR",_("Volta")
    EASTERN="ER",_("Eastern")
    UPPER_WEST="UW",_("Upper West")
    UPPER_EAST="UE",_("Upper East")
    SAVANNAH="SR",_("Savannah")
    NORTH_EAST="NE",_("North East")
    BONO_EAST="BE",_("Bono East")
    OTI="OR",_("Oti")
    AHAFO="AR",_("Ahafo")
    BONO="BR",_("Bono")
    WESTERN_NORTH="WN",_("Western North")

class Institution(models.Model):
    class InstitutionType(models.TextChoices):
        UNIVERSITY="UN",_("University")
        TECHNICAL_UNIVERSITY="TU",_("Technical University")
        NON_TERTIARY="NT",_("Non-tertiary")
        VOCATIONAL="VT",_("Vocation/Technical Institution")
        PROFESSIONAL_INSTITUTE="PI",_("Professional Institute (Chartered bodies)")
        SHORT_COURSES="SC",_("Short Courses (CPD)")
    class OwnershipType(models.TextChoices):
        PUBLIC="PB",_("Public")
        PRIVATE="PV",_("PRIVATE")
    name=models.CharField(max_length=100)
    institution_type=models.CharField(choices=InstitutionType,max_length=2,default=InstitutionType.UNIVERSITY)
    ownership_type=models.CharField(choices=OwnershipType,default=OwnershipType.PUBLIC)
    enable=models.BooleanField(default=False)
    owner=models.ForeignKey(User,models.SET_NULL,blank=True,null=True,)

    
class Course(models.Model):
    name=models.CharField(max_length=100)

class Campus(models.Model):
    institution=models.ForeignKey(Institution,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)
    admission_start_date=models.DateField(blank=True,null=True)
    admission_end_date=models.DateField(blank=True,null=True)
    region=models.CharField(choices=RegionChoices)

class CourseProfile(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    profile=models.TextField(blank=True)
    domestic_fee=models.DecimalField(max_digits=7,decimal_places=2)
    international_fee=models.DecimalField(max_digits=7,decimal_places=2)
    campus=models.ForeignKey(Campus,on_delete=models.CASCADE)
    certificates=models.ManyToManyField(CertificateType)
    mode_of_teaching=models.CharField(choices=ModeOfTeaching)
    time_of_study=models.CharField(choices=TimeOfStudy)
    duration_of_study=models.DurationField()
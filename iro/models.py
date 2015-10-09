from django.db import models

# Create your models here.

class Applicant(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=40)
    applicant_name = models.CharField(max_length=200)
    applicant_email = models.EmailField()
    date_of_birth = models.DateField()

    mentors = models.ForeignKey(Mentor)
    possible_pis = models.ForeignKey(Faculty)


class Mentor(models.Model):
    mentor_name = models.CharField(max_length=200)

class Faculty(models.Model):
    faculty_name = models.CharField(max_length=200)
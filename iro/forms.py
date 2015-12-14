__author__ = 'Jacob Bieker'

from registration.forms import RegistrationForm
from django import forms
from iro.models import Institute, Faculty, Applicant, Mentor

class MentorRegistrationForm(RegistrationForm):
    mentor_name = forms.CharField(max_length=200)
    professor = forms.CharField(max_length=200)

class FacultyRegistrationForm(RegistrationForm):
    faculty_name = forms.CharField(max_length=200)
    institute = forms.ModelChoiceField(queryset=Institute.objects.all())

class InternRegistrationForm(RegistrationForm):
    application = forms.ModelChoiceField(queryset=Applicant.objects.all())
    institute = forms.ModelChoiceField(queryset=Institute.objects.all(), required=False)
    professor = forms.ModelChoiceField(queryset=Faculty.objects.all(), required=False)
    mentors = forms.ModelMultipleChoiceField(queryset=Mentor.objects.all(), required=False)
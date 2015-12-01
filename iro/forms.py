__author__ = 'Jacob Bieker'

from registration.forms import RegistrationForm
from django import forms
from iro.models import Institute, Faculty

class MentorRegistrationForm(RegistrationForm):
    mentor_name = forms.CharField(max_length=200)
    professor = forms.CharField(max_length=200)

class FacultyRegistrationForm(RegistrationForm):
    faculty_name = forms.CharField(max_length=200)
    institute = forms.ModelChoiceField(queryset=Institute.objects.all())

class InternRegistrationForm(RegistrationForm):
    institute = forms.ModelChoiceField(queryset=Institute.objects.all())
    professor = forms.ModelChoiceField(queryset=Faculty.objects.all())
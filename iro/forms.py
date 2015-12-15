__author__ = 'Jacob Bieker'

from registration.forms import RegistrationForm
from django import forms
from iro.models import Institute, Faculty, Applicant, Mentor, ReferenceLetter, ProgressReport, PISurvey, Abstract
from django.forms import ModelForm

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

# Model Forms

class ReferenceLetterForm(ModelForm):
    class Meta:
        model = ReferenceLetter
        fields = ['letter', 'applicant']

class ProgressReportForm(ModelForm):
    class Meta:
        model = ProgressReport
        fields = ['content', 'week']

class PISurveryForm(ModelForm):
    model = PISurvey
    fields = ["intern", "comments"]

class ApplicantForm(ModelForm):
    class Meta:
        model = Applicant
        # Exclude the administrative fields
        exclude = ['mentors', 'possible_pis', 'triage', 'ranking',
                   'likely_institute', 'decision_action', 'comments',
                   'application_completeness', 'correspondence', 'year_created',
                   'short_list', 'transcript']

class FacultyForm(ModelForm):
    class Meta:
        model = Faculty
        fields = ['faculty_name', 'institute']

class MentorForm(ModelForm):
    class Meta:
        model = Mentor
        fields = ['mentor_name', 'professor']

class AbstractForm(ModelForm):
    class Meta:
        model = Abstract
        fields = ['title', 'content']

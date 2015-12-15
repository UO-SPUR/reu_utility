__author__ = 'Jacob Bieker'

from registration.forms import RegistrationForm
from django import forms
from iro.models import Institute, Faculty, Applicant, Mentor, Intern, ReferenceLetter, ProgressReport, PISurvey, Abstract
from django.forms import ModelForm

# Registration Forms
class MentorRegistrationForm(RegistrationForm):
    mentor_name = forms.CharField(max_length=200)
    professor = forms.ModelMultipleChoiceField(queryset=Faculty.objects.all(), required=False)

class FacultyRegistrationForm(RegistrationForm):
    faculty_name = forms.CharField(max_length=200)
    institute = forms.ModelChoiceField(queryset=Institute.objects.all())

class InternRegistrationForm(RegistrationForm):
    application = forms.ModelChoiceField(queryset=Applicant.objects.all())
    institute = forms.ModelChoiceField(queryset=Institute.objects.all(), required=False)
    professor = forms.ModelChoiceField(queryset=Faculty.objects.all(), required=False)
    mentors = forms.ModelMultipleChoiceField(queryset=Mentor.objects.all(), required=False)

# Overview forms, for general editing of own user profile

class FacultyOverviewForm(ModelForm):
    class Meta:
        model = Faculty
        fields = ['faculty_name', 'email_template', 'institute']

# Mentor Overview form handled already by MentorForm

class InternOverviewForm(ModelForm):
    class Meta:
        model = Intern

    def __init__(self, *args, **kwargs):
        super(InternOverviewForm, self).__init__(*args, **kwargs)
        uneditable_fields = ['application', 'user', 'name', 'program', 'student_id', 'institute', 'professor',
                             'mentors', 'arrival_date', 'departure_date', 'symposium_session']
        for field in uneditable_fields:
            self.fields[field].widget.attrs['readonly'] = 'true'
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
                   'short_list', 'transcript', 'uuid']

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

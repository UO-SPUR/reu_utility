__author__ = 'Jacob Bieker'

from registration.forms import RegistrationForm
from django import forms
from iro.models import Institute, Faculty, Applicant, Mentor, Intern, ReferenceLetter, ProgressReport, PISurvey, Abstract
from django.forms import ModelForm
from betterforms.multiform import MultiModelForm

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
        fields = ['application', 'user', 'name', 'program', 'student_id', 'institute', 'professor',
                  'mentors', 'arrival_date', 'departure_date', 'symposium_session', 'picture', 'abstract',
                  'presentation_oral', 'presentation_poster']

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
        fields = ['letter']

class ReferenceLetterRequestForm(ModelForm):
    class Meta:
        model = ReferenceLetter
        fields = ['name', 'email', 'institution', 'department']

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

# MultiForms

class ApplicationMultiForm(MultiModelForm):
    form_classes = {
        'application': ApplicantForm,
        'reference_one': ReferenceLetterForm,
        'reference_two': ReferenceLetterForm,
        'reference_three': ReferenceLetterForm,
    }

    def save(self, commit=True):
        objects = super(ApplicationMultiForm, self).save(commit=False)

        if commit:
            applicant = objects['application']
            applicant.save()
            reference_one = objects['reference_one']
            reference_one.applicant = applicant
            reference_one.save()
            reference_two = objects['reference_two']
            reference_two.applicant = applicant
            reference_two.save()
            reference_three = objects['reference_three']
            reference_three.applicant = applicant
            reference_three.save()

        return objects

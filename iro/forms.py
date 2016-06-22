__author__ = 'Jacob Bieker'

from registration.forms import RegistrationForm
from django import forms
from iro.models import Institute, Faculty, Applicant, Mentor, Intern, ReferenceLetter, ProgressReport, PISurvey, \
    MentorSurvey, InternSurvey, Abstract, FacultyFeedback
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
        fields = ['application', 'user', 'name', 'program', 'student_id', 'institute', 'professor',
                  'mentors', 'arrival_date', 'departure_date', 'symposium_session', 'picture', 'abstract',
                  'presentation_oral', 'presentation_poster']

    def __init__(self, *args, **kwargs):
        super(InternOverviewForm, self).__init__(*args, **kwargs)
        uneditable_fields = ['application', 'user', 'name', 'program', 'student_id', 'institute', 'professor',
                             'mentors', 'arrival_date', 'departure_date', 'symposium_session', 'picture']
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


class PISurveyForm(ModelForm):
    model = PISurvey
    fields = ["intern", "evaluator" "comments"]


class MentorSurveyForm(ModelForm):
    model = MentorSurvey
    fields = ["intern", "evaluator", "comments"]


class InternSurveyForm(ModelForm):
    model = InternSurvey
    fields = ["evaluator", "comments"]


class FacultyFeedbackForm(ModelForm):
    class Meta:
        model = FacultyFeedback
        fields = ["applicant_rating", "feedback"]


class ApplicantForm(ModelForm):
    class Meta:
        model = Applicant
        # Exclude the administrative fields
        exclude = ['mentors', 'possible_pis', 'triage', 'ranking',
                   'likely_institute', 'decision_action', 'comments',
                   'application_completeness', 'correspondence', 'year_created',
                   'short_list', 'uuid', 'show_preferences']

    def __init__(self, *args, **kwargs):
        super(ApplicantForm, self).__init__(*args, **kwargs)
        self.fields['sex'].required = False
        self.fields['ethnic_background'].required = False
        self.fields['ethnic_background_other'].required = False
        self.fields['disadvantaged'].required = False
        self.fields['disadvantaged_other'].required = False
        self.fields['transfer'].required = False
        self.fields['relevant_coursework'].required = False
        self.fields['previous_program_other'].required = False
        self.fields['date_of_test'].required = False
        self.fields['advanced_degree_other'].required = False
        self.fields['other_choice'].required = False
        self.fields['details'].required = False
        self.fields['lab_preferences'].required = False
        self.fields['outside_interests'].required = False
        self.fields['grades'].required = False
        self.fields['transcript'].required = False


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

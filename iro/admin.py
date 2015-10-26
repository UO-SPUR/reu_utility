from django.contrib import admin
from tabbed_admin import TabbedModelAdmin

# Register your models here.
from .models import *

# Inline models here

class LetterInline(admin.StackedInline):
    model = ReferenceLetter
    extra = 3

class InternInline(admin.StackedInline):
    model = Intern
    extra = 1

class AddressInline(admin.StackedInline):
    model = Address
    extra = 1
# Defining ModelAdmin here.

@admin.register(Applicant)
class ApplicantAdmin(TabbedModelAdmin):
    tab_admin = (
        ('Course Work', {
            'fields': (('gpa', 'stem_gpa'), 'grades')
        }),
        ('Application Status', {
            'fields': (('triage', 'short_list'), ('ranking', 'likely_institute'), ('possible_pis', 'decision_action'))
        }),
        LetterInline,
        ('Admin', {
            'fields': ('comments', 'application_completeness', 'correspondence')
        })
    )
    tab_application = (
        ('Basic Information', {
            'fields': (('first_name', 'last_name'), ('applicant_email', 'applicant_name'), ('cell_phone_number', 'phone_number'))
        }),
        ('College', {
            'fields': (('college', 'college_class'), ('expected_graduation', 'major'), 'transfer', ('gpa', 'stem_gpa'), ('program', 'available'))
        }),
        ('Demographic Information', {
            'fields': (('date_of_birth', 'citizenship'), 'sex', ('ethnic_background', 'ethnic_background_other'), ('disadvantaged', 'disadvantaged_other'))
        }),
        ('Survey Questions', {
            'fields': (('learned_of', 'previous_program'), ('marc_current', 'marc_past'), ('advanced_degree', 'advanced_degree_other'), ('research_career', 'gre_mcat'), 'date_of_test')
        }),
        ('Application Questions', {
            'fields': ('background', 'goals', ('first_choice', 'first_choice_importance'), ('second_choice', 'second_choice_importance'), ('third_choice', 'third_choice_importance'), 'other_choice', 'details', 'lab_preferences', 'outside_interests', 'transcript')
        }),
        ('Faculty', {
            'fields': (('faculty_reference_one', 'faculty_reference_one_email'), ('faculty_reference_two', 'faculty_reference_two_email'), ('faculty_reference_three', 'faculty_reference_three_email'))
        })
    )
    tab_intern = (
        InternInline,
    )
    tab_possible_pis = (
        
    )

    tabs = [
        ('Admin', tab_admin),
        ('Application', tab_application),
        ('Intern Profile', tab_intern)
    ]

admin.site.register(Faculty)
admin.site.register(Mentor)
admin.site.register(Intern)
admin.site.register(Abstract)
admin.site.register(ReferenceLetter)
admin.site.register(ProgressReport)
admin.site.register(PISurvey)
admin.site.register(InternSurvey)
admin.site.register(MentorSurvey)
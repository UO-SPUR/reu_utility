from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from tabbed_admin import TabbedModelAdmin

# Register your models here.
from .models import *


# Inline models here

class FacultyInline(admin.StackedInline):
    model = Faculty
    can_delete = False
    verbose_name_plural = "Faculty"


class MentorInline(admin.StackedInline):
    model = Mentor
    can_delete = False
    verbose_name_plural = "Mentors"


class LetterInline(admin.StackedInline):
    model = ReferenceLetter
    extra = 3
    max_num = 3


class InternInline(admin.StackedInline):
    model = Intern
    can_delete = False
    extra = 1


class AbstractInline(admin.StackedInline):
    model = Abstract
    can_delete = False
    extra = 1


class ApplicantInline(admin.StackedInline):
    model = Applicant
    can_delete = False
    extra = 1
# Defining ModelAdmin here.

@admin.register(Applicant)
class ApplicantAdmin(TabbedModelAdmin):
    list_display = ('applicant_name', 'gpa', 'stem_gpa', 'decision_action', 'disadvantaged', 'first_choice',
                    'second_choice', 'third_choice', 'short_list', 'ranking',
                    'available_start', 'available_end', 'show_preferences')
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
        }),
        ('Addresses', {
            'fields': (('street', 'city', 'state', 'zipcode'),
                       ('perm_street', 'perm_city', 'perm_state', 'perm_zipcode'))
        })
    )
    tab_application = (
        ('Basic Information', {
            'fields': (
            ('first_name', 'last_name'), ('applicant_email', 'applicant_name'), ('cell_phone_number', 'phone_number'))
        }),
        ('College', {
            'fields': (('college', 'college_class'), ('expected_graduation', 'major'), 'transfer', ('gpa', 'stem_gpa'),
                       ('program', 'available_start', 'available_end'))
        }),
        ('Demographic Information', {
            'fields': (('date_of_birth', 'citizenship'), 'sex', ('ethnic_background', 'ethnic_background_other'),
                       ('disadvantaged', 'disadvantaged_other'))
        }),
        ('Survey Questions', {
            'fields': (('learned_of', 'previous_program'), ('marc_current', 'marc_past'),
                       ('advanced_degree', 'advanced_degree_other'), ('research_career', 'gre_mcat'), 'date_of_test')
        }),
        ('Application Questions', {
            'fields': ('background', 'goals', ('first_choice', 'first_choice_importance'),
                       ('second_choice', 'second_choice_importance'), ('third_choice', 'third_choice_importance'),
                       'other_choice', 'details', 'lab_preferences', 'outside_interests', 'transcript')
        }),
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


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('faculty_name', 'institute')


@admin.register(Intern)
class InternAdmin(TabbedModelAdmin):
    list_display = ('name', 'institute', 'professor', 'program')
    tab_admin = (
        ('Overview', {
            'fields': ('program', 'institute')
        }),
        FacultyInline,
        ('Presentation', {
            'fields': ('symposium_session', ('presentation_oral', 'presentation_poster'))
        }),
        AbstractInline,
        ('Admin', {
            'fields': ('student_id', ('arrival_date', 'departure_date'))
        }),
    )
    tab_application = (
        ApplicantInline,
    )

    tabs = [
        ('Overview', tab_admin),
        ('Application', tab_application)
    ]


class UserAdmin(UserAdmin):
    inlines = (FacultyInline, MentorInline, InternInline)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# admin.site.register(Faculty)
admin.site.register(Mentor)
# admin.site.register(Intern)
admin.site.register(Abstract)
admin.site.register(ReferenceLetter)
admin.site.register(ProgressReport)
admin.site.register(Institute)
admin.site.register(IroSetup)
admin.site.register(PISurvey)
admin.site.register(InternSurvey)
admin.site.register(MentorSurvey)
admin.site.register(Configuration)

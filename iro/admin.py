from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from tabbed_admin import TabbedModelAdmin
from django.core.mail import send_mail

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

    send_mail('Subject here', 'Here is the message.', 'from@example.com',
              ['to@example.com'], fail_silently=False)

class InternInline(admin.StackedInline):
    model = Intern
    can_delete = False
    extra = 1


# Defining ModelAdmin here.
class ReferenceLetterAdmin(admin.ModelAdmin):
    list_display = ['status', 'letter', 'comments']
    actions = [send_request_email]

    def send_request_email(self, request, queryset):
        queryset

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
        }),
        ('Addresses', {
            'fields': (('street', 'city', 'state', 'zipcode'),
                       ('perm_street', 'perm_city', 'perm_state', 'perm_zipcode'))
        })
    )
    tab_application = (
        ('Basic Information', {
            'fields': (('first_name', 'last_name'), ('applicant_email', 'applicant_name'), ('cell_phone_number', 'phone_number'))
        }),
        ('College', {
            'fields': (('college', 'college_class'), ('expected_graduation', 'major'), 'transfer', ('gpa', 'stem_gpa'), ('program', 'available_start', 'available_end'))
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

class UserAdmin(UserAdmin):
    inlines = (FacultyInline, MentorInline, InternInline)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Faculty)
admin.site.register(Mentor)
admin.site.register(Intern)
admin.site.register(Abstract)
admin.site.register(ReferenceLetter)
admin.site.register(ProgressReport)
admin.site.register(Institute)
admin.site.register(IroSetup)
admin.site.register(PISurvey)
admin.site.register(InternSurvey)
admin.site.register(MentorSurvey)
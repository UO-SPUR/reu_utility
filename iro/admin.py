from django.contrib import admin
from tabbed_admin import TabbedModelAdmin

# Register your models here.
from .models import *

# Inline models here

class LetterInline(admin.StackedInline):
    model = ReferenceLetter

class InternInline(admin.StackedInline):
    model = Intern

class AddressInline(admin.StackedInline):
    model = Address
# Defining ModelAdmin here.
class ApplicantAdmin(TabbedModelAdmin):
    tab_admin = (
        ('Course Work', {
            'fields': (('gpa', 'stem_gpa'), 'relevant_coursework')
        }),
        ('Application Status', {
            'fields': (('triage', 'short_list'), ('ranking', 'likely_institute'), ('possible_pis', 'decision_action'))
        }),
        ('Letters of Recommendation', {
            LetterInline,
        }),
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
        ('Addresses', {
            AddressInline,
            AddressInline
        })

    )
    tab_intern = (
        InternInline
    )

admin.site.register(Applicant)
admin.site.register(Faculty)
admin.site.register(Mentor)
admin.site.register(Intern)
admin.site.register(Abstract)
admin.site.register(ReferenceLetter)
admin.site.register(ProgressReport)
admin.site.register(PISurvey)
admin.site.register(InternSurvey)
admin.site.register(MentorSurvey)
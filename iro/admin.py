from django.contrib import admin

# Register your models here.
from .models import *

# Defining ModelAdmin here.

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
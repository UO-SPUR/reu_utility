__author__ = 'Jacob Bieker'

from registration.backends.default.views import RegistrationView
from reu_utility.settings import *
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from iro.forms import FacultyRegistrationForm, InternRegistrationForm, MentorRegistrationForm
from iro.models import Faculty, Intern, Mentor

intern_group = Group.objects.get_or_create(name=INTERN_GROUP_NAME)
faculty_group = Group.objects.get_or_create(name=FACULTY_GROUP_NAME)
mentor_group = Group.objects.get_or_create(name=MENTOR_GROUP_NAME)

class FacultyRegistrationView(RegistrationView):

    form_class = FacultyRegistrationForm

    def register(self, request, form_class):
        new_user = super(FacultyRegistrationView, self).register(request, form_class)
        user_profile = Faculty()
        user_profile.user = new_user
        user_profile.faculty_name = form_class.cleaned_data['faculty_name']
        user_profile.institute = form_class.cleaned_data['institute']
        user_profile.save()
        return user_profile

class MentorRegistrationView(RegistrationView):

    form_class = MentorRegistrationForm

    def register(self, request, form_class):
        new_user = super(MentorRegistrationView, self).register(request, form_class)
        user_profile = Mentor()
        user_profile.user = new_user
        user_profile.mentor_name = form_class.cleaned_data['mentor_name']
        user_profile.professor = form_class.cleaned_data['professor']
        user_profile.save()
        return user_profile

class InternRegistrationView(RegistrationView):

    form_class = InternRegistrationForm

    def register(self, request, form_class):
        new_user = super(InternRegistrationView, self).register(request, form_class)
        user_profile = Intern()
        user_profile.user = new_user
        user_profile.application = form_class.cleaned_data['application']
        user_profile.institute = form_class.cleaned_data['institute']
        user_profile.professor = form_class.cleaned_data['professor']
        user_profile.mentors = form_class.cleaned_data['mentors']
        # Now try to take the data from Application to fill out rest of form
        user_profile.name = user_profile.application.applicant_name
        user_profile.program = user_profile.application.program
        user_profile.arrival_date = user_profile.application.available_start
        user_profile.departure_date = user_profile.application.available_end
        # End taking things from application
        user_profile.save()
        return user_profile

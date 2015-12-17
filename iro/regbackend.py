__author__ = 'Jacob Bieker'

from registration.backends.default.views import RegistrationView
from iro.forms import FacultyRegistrationForm, InternRegistrationForm, MentorRegistrationForm
from iro.models import Faculty, Intern, Mentor
from iro.groups_permissions import add_user_to_faculty_group, add_user_to_intern_group, add_user_to_mentor_group
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

class FacultyRegistrationView(RegistrationView):

    form_class = FacultyRegistrationForm

    def register(self, request, form_class):
        new_user = super(FacultyRegistrationView, self).register(request, form_class)
        user_profile = Faculty()
        user_profile.user = new_user
        user_profile.faculty_name = form_class.cleaned_data['faculty_name']
        user_profile.institute = form_class.cleaned_data['institute']
        user_profile.correspondence = "None"
        user_profile.email_template = "Insert Template Here"
        user_profile.save()
        return user_profile

    #post_save.connect(add_user_to_faculty_group, sender=User, dispatch_uid="iro.regbackend.facultyRegistration")

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

    #post_save.connect(add_user_to_mentor_group, sender=User, dispatch_uid="iro.regbackend.mentorRegistration")

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
        user_profile.student_id = "Enter ID Here"
        # Now try to take the data from Application to fill out rest of form
        user_profile.name = user_profile.application.applicant_name
        user_profile.program = user_profile.application.program
        user_profile.arrival_date = user_profile.application.available_start
        user_profile.departure_date = user_profile.application.available_end
        # End taking things from application
        user_profile.save()
        return user_profile

    #post_save.connect(add_user_to_intern_group, sender=User, dispatch_uid="iro.regbackend.internRegistration")

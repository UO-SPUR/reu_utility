__author__ = 'Jacob Bieker'

from registration.backends.default.views import RegistrationView
from iro.forms import FacultyRegistrationForm, InternRegistrationForm, MentorRegistrationForm
from iro.models import Faculty, Intern, Mentor

class FacultyRegistrationView(RegistrationView):

    form_class = FacultyRegistrationForm

    def register(self, request, form_class):
        new_user = super(FacultyRegistrationView, self).register(request, form_class)
        user_profile = Faculty()
        user_profile.user = new_user
        user_profile.field = form_class.cleaned_data['field']
        user_profile.save()
        return user_profile

class MentorRegistrationView(RegistrationView):

    form_class = MentorRegistrationForm

    def register(self, request, form_class):
        new_user = super(MentorRegistrationView, self).register(request, form_class)
        user_profile = Mentor()
        user_profile.user = new_user
        user_profile.field = form_class.cleaned_data['field']
        user_profile.save()
        return user_profile

class InternRegistrationView(RegistrationView):

    form_class = InternRegistrationForm

    def register(self, request, form_class):
        new_user = super(InternRegistrationView, self).register(request, form_class)
        user_profile = Intern()
        user_profile.user = new_user
        user_profile.field = form_class.cleaned_data['field']
        user_profile.save()
        return user_profile

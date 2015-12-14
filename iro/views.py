from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from iro.models import ApplicantForm, FacultyForm, MentorForm
from django.contrib.auth.decorators import login_required, user_passes_test
from iro.choices import INTERN_GROUP_NAME, FACULTY_GROUP_NAME, MENTOR_GROUP_NAME

# Create your views here.

def get_application(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ApplicantForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ApplicantForm()

    return render(request, 'application.html', {'application_form': form})

def get_faculty(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FacultyForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FacultyForm()

    return render(request, 'faculty-sign-up.html', {'faculty_form': form})

def get_mentor(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MentorForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = MentorForm()

    return render(request, 'mentor-sign-up.html', {'mentor_form': form})

################################### Creation of Users Below #####################################################
class FacultyCreate(UserCreationForm):

    #this one is called when a user has been created successfully
    def get_success_url(self):
        g = Group.objects.get(name='faculty') # assuming you have a group 'test' created already. check the auth_user_group table in your DB
        g.user_set.add(self.object)
        return reverse('faculty')



class MentorCreate(CreateView):
    model = User
    fields = ['username'] #only expose the username field for the sake of simplicity add more fields as you need

    #this one is called when a user has been created successfully
    def get_success_url(self):
        g = Group.objects.get(name='mentors') # assuming you have a group 'test' created already. check the auth_user_group table in your DB
        g.user_set.add(self.object)
        return reverse('mentors')

class InternCreate(CreateView):
    model = User
    fields = ['username'] #only expose the username field for the sake of simplicity add more fields as you need

    #this one is called when a user has been created successfully
    def get_success_url(self):
        g = Group.objects.get(name='interns') # assuming you have a group 'test' created already. check the auth_user_group table in your DB
        g.user_set.add(self.object)
        return reverse('interns')

# Views that are restricted based on group user is in

# Tests for the different groups

def not_in_intern_group(user):
    if user:
        return user.groups.filter(name=INTERN_GROUP_NAME).count() == 0
    return False


@login_required
@user_passes_test(not_in_intern_group, login_url='/')
def intern_view(request):
    return reverse('interns')
from django.shortcuts import render
from django.http import HttpResponseRedirect
from iro.models import ApplicantForm, FacultyForm, MentorForm
from django.contrib.auth.decorators import user_passes_test
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

def thanks(request):
    # Redirection page to say sign up was succesful
    return render(request, 'thanks.html')

# Views that are restricted based on group user is in

# Tests for the different groups

# Checks Intern:
def is_intern(function=None):
    """Use this decorator to restrict access to
    authenticated users who are in the "Intern" group."""
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated() and u.groups.filter(name=INTERN_GROUP_NAME).exists()
    )
    return actual_decorator(function)

def is_mentor(function=None):
    """Use this decorator to restrict access to
    authenticated users who are in the "Mentor" group."""
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated() and u.groups.filter(name=MENTOR_GROUP_NAME).exists()
    )
    return actual_decorator(function)

def is_faculty(function=None):
    """Use this decorator to restrict access to
    authenticated users who are in the "Faculty" group."""
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated() and u.groups.filter(name=FACULTY_GROUP_NAME).exists()
    )
    return actual_decorator(function)

# Checks for User is part of Intern
@is_intern
def intern_view(request):
    return render(request, 'intern.html')

@is_intern
def intern_overview(request):
    return render(request, 'intern-overview.html')

# Checks for User is part of Mentor
@is_mentor
def mentor_view(request):
    return render(request, 'mentor.html')

@is_mentor
def mentor_overview(request):
    return render(request, 'mentor-overview.html')

# Checks for User is part of Faculty
@is_faculty
def faculty_view(request):
    return render(request, 'faculty.html')

@is_faculty
def faculty_overview(request):
    return render(request, 'faculty-overview.html')
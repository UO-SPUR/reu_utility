from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, QueryDict
from iro.forms import *
from django.contrib.auth.decorators import user_passes_test, login_required, permission_required
from iro.choices import INTERN_GROUP_NAME, FACULTY_GROUP_NAME, MENTOR_GROUP_NAME
#from weasyprint import HTML, CSS
from django.template.loader import get_template
from django.template import RequestContext
from django.core.mail import send_mail, EmailMultiAlternatives
from reu_utility.settings import EMAIL_HOST_USER
from iro.choices import *

# Create your views here.

def get_application(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ApplicationMultiForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...

            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ApplicationMultiForm()

    return render(request, 'application-improved.html', {'input_form': form})

def get_reference(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ReferenceLetterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ReferenceLetterForm()

    return render(request, 'reference-letter-upload.html', {'input_form': form})


def thanks(request):
    # Redirection page to say sign up was successful
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

def is_faculty_mentor(function=None):
    """Use this decorator to restrict access to
    authenticated users who are in the "Faculty" group."""
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated() and (u.groups.filter(name=FACULTY_GROUP_NAME).exists() or u.groups.filter(name=MENTOR_GROUP_NAME).exists())
    )
    return actual_decorator(function)

# Checks for User is part of Intern
@is_intern
def intern_view(request):
    return render(request, 'intern.html')


@is_intern
def intern_survey(request):
    return render(request, 'intern-survey.html')


@is_intern
def progress_report_add(request):
    current_intern = request.user.intern
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProgressReportForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProgressReportForm()

    return render(request, 'progress-report.html', {'input_form': form})


@is_intern
def intern_abstract_edit(request):
    current_intern = request.user.intern
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AbstractForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AbstractForm(instance=current_intern.abstract)

    return render(request, 'intern-abstract.html', {'input_form': form})


@is_intern
def intern_overview(request):
    current_intern = request.user.intern
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = InternOverviewForm(request.POST, instance=current_intern)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            form.save()
            # redirect to a new URL:
            return render(request, 'intern-overview.html', {'input_form': form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = InternOverviewForm(instance=current_intern)

    return render(request, 'intern-overview.html', {'input_form': form})


# Checks for User is part of Mentor
@is_mentor
def mentor_view(request):
    return render(request, 'mentor.html')


@is_mentor
def mentor_survey(request):
    return render(request, 'mentor-survey.html')


@is_mentor
def mentor_overview(request):
    current_mentor = request.user.mentor
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MentorForm(request.POST, instance=current_mentor)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            form.save()
            # redirect to a new URL:
            return render(request, 'mentor-overview.html', {'input_form': form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = MentorForm(instance=current_mentor)

    return render(request, 'mentor-overview.html', {'input_form': form})


# Checks for User is part of Faculty
@is_faculty
def faculty_view(request):
    return render(request, 'faculty.html')


@is_faculty
def faculty_survey(request):
    return render(request, 'faculty-survey.html')


@is_faculty
def faculty_overview(request):
    current_faculty = request.user.faculty
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FacultyOverviewForm(request.POST, instance=current_faculty)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            form.save()
            # redirect to a new URL:
            return render(request, 'faculty-overview.html', {'input_form': form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FacultyOverviewForm(instance=current_faculty)

    return render(request, 'faculty-overview.html', {'input_form': form})


@is_faculty
def faculty_application_overview(request):
    current_faculty = request.user.faculty
    assigned_applications = current_faculty.applicant_set.all()
    # TODO: List applications, with the links being to another view that generates the PDFs of application/ Reference Letters
    return render(request, 'faculty_overview.html')

'''
@is_faculty
def faculty_application_pdfs(request, applicant):
    # Get information from applicant
    filename = applicant.applicant_name + '.pdf'

    html_template = get_template('templates/applicant_pdf.html')

    rendered_html = html_template.render(RequestContext(request, {'application': applicant})).encode(encoding="UTF-8")

    pdf_file = HTML(string=rendered_html).write_pdf()

    http_response = HttpResponse(pdf_file, content_type='application/pdf')
    http_response['Content-Disposition'] = 'filename=' + filename

    return http_response
'''

# Faculty and Mentor views

# Non-PDF Applicant Info
@is_faculty_mentor
def application_view_html(request):

    uuid = request.GET['uuid']
    applicant = Applicant.objects.get(uuid=uuid)

    html_template = get_template('templates/applicant_pdf.html')

    rendered_html = html_template.render(RequestContext(request, {'application': applicant})).encode(encoding="UTF-8")
    http_response = HttpResponse(rendered_html)

    return http_response


# Admin Views

@permission_required('is_superuser')
def admin_reference_letter_view(request):

    uuid = request.GET['uuid']
    applicant = Applicant.objects.get(uuid=uuid)

    html_template = get_template('templates/admin-reference-letters.html')

    rendered_html = html_template.render(RequestContext(request, {'application': applicant})).encode(encoding="UTF-8")
    http_response = HttpResponse(rendered_html)

    return http_response

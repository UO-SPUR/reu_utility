from django.test import TestCase
from django.utils import timezone
from iro.models import *

# Create your tests here.

class ApplicantTestCase(TestCase):
    def setUp(self):
        Applicant.objects.create(first_name="Jacob", last_name="Bieker",
                                 applicant_name="Jacob Bieker", date_of_birth="01/01/1996",
                                 sex="Male", ethnic_background="White", disadvantaged="No",
                                 citizenship="U.S. Citizen", college="University of Oregon",
                                 college_class="Sophomore")

class FacultyTestCase(TestCase):
    def setUp(self):
        Faculty.objects.create()

class MentorTestCase(TestCase):
    def setUp(self):
        Mentor.objects.create()

class InstituteTestCase(TestCase):
    def setUp(self):
        Institute.objects.create()

class AbstractTestCase(TestCase):
    def setUp(self):
        Abstract.objects.create()

class InternTestCase(TestCase):
    def setUp(self):
        Intern.objects.create()

class ProgressReportTestCase(TestCase):
    def setUp(self):
        ProgressReport.objects.create()

class IroSetupTestCase(TestCase):
    def setUp(self):
        IroSetup.objects.create()
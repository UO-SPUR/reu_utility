from django.test import TestCase
from iro.models import *

# Create your tests here.

class ApplicantTestCase(TestCase):
    def setUp(self):
        Applicant.objects.create()

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
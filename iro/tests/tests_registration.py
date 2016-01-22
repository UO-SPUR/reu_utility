__author__ = 'jacob'
from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from iro.models import *
from iro.choices import *


class FacultyTestCase(TestCase):
    def setUp(self):
        Institute.objects.create(name="Bieker Institute of Technology",
                                 street="Einstein Blvd",
                                 city="Geneva",
                                 state="Switzerland",
                                 zipcode="97412",
                                 discipline="High-Energy Physics")
        User.objects.create()
        Faculty.objects.create(faculty_name="Robert Benolken",
                               institute=)


class MentorTestCase(TestCase):
    def setUp(self):
        Mentor.objects.create()

class InternTestCase(TestCase):
    def setUp(self):
        Intern.objects.create()
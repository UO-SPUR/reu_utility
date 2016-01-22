__author__ = 'jacob'
from django.test import TestCase
from django.utils import timezone
from iro.models import *
from iro.choices import *


class FacultyTestCase(TestCase):
    def setUp(self):
        Faculty.objects.create()


class MentorTestCase(TestCase):
    def setUp(self):
        Mentor.objects.create()

class InternTestCase(TestCase):
    def setUp(self):
        Intern.objects.create()
__author__ = 'jacob'

from django.test import TestCase
from django.utils import timezone
from iro.models import *
from iro.choices import *

class AbstractTestCase(TestCase):
    def setUp(self):
        Abstract.objects.create()


class ProgressReportTestCase(TestCase):
    def setUp(self):
        ProgressReport.objects.create()
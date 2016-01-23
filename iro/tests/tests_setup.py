__author__ = 'jacob'

from django.test import TestCase
from django.utils import timezone
from iro.models import *
from iro.choices import *

class InstituteTestCase(TestCase):
    def setUp(self):
        Institute.objects.create()

class IroSetupTestCase(TestCase):
    def setUp(self):
        IroSetup.objects.create()
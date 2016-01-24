__author__ = 'jacob'

from django.test import TestCase
from django.utils import timezone
from iro.models import *
from iro.choices import *


class InstituteTestCase(TestCase):
    def setUp(self):
        Institute.objects.create()


class IroSetupTestCase(TestCase):
    def test_setup_creation(self):
        setup = IroSetup.objects.create(program_name="Summer Program For Undergraduate Research",
                                        acronym="SPUR",
                                        base_url="spur.uoregon.edu",
                                        university_name="University of Oregon",
                                        program_email="summerpgms@uoregon.edu",
                                        program_director="Jacob Bieker",
                                        program_phone_number=5552221111)

        self.assertEqual(setup.acronym, "SPUR")
        self.assertEqual(setup.program_phone_number, 5552221111)

        self.assertEqual(IroSetup.objects.create(program_name="Summer Program For Undergraduate Research",
                                                 acronym="SPUR",
                                                 base_url="spur.uoregon.edu",
                                                 university_name="University of Oregon",
                                                 program_email="summerpgms@uoregon.edu",
                                                 program_director="Jacob Bieker",
                                                 program_phone_number=5552221111), ValidationError)


__author__ = 'jacob'

from django.test import TestCase
from django.utils import timezone
from iro.models import *
from iro.choices import *


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


class ConfigurationTestCase(TestCase):
    def test_configuration_creation(self):
        configuration = Configuration.objects.create(email_use_ssl=True,
                                                     email_host="uoregon.edu",
                                                     email_host_user="summerpgms",
                                                     email_host_password="123456",
                                                     email_port=465,
                                                     email_username="summerpgms",
                                                     fail_silently=True)

        self.assertEqual(configuration.email_use_ssl, True)
        self.assertEqual(configuration.email_host, "uoregon.edu")

        self.assertEqual(Configuration.objects.create(email_use_ssl=True,
                                                      email_host="uoregon.edu",
                                                      email_host_user="summerpgms",
                                                      email_host_password="123456",
                                                      email_port=465,
                                                      email_username="summerpgms",
                                                      fail_silently=True), ValidationError)

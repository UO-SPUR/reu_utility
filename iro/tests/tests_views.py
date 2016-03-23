__author__ = 'jacob'
from django.test import TestCase, RequestFactory
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User, Group, AnonymousUser
from iro.views import *
from iro.models import *
from unittest.mock import patch, MagicMock
from iro.choices import *


class GetApplicationViewTest(TestCase):
    """
    Test Application View
    """

    def setUp(self):
        self.factory = RequestFactory()
        self.user = AnonymousUser()

    def test_get(self):
        """
        Test GET Requests
        """
        request = self.factory.get(reverse('application'))
        request.user = self.user
        response = get_application(request)
        self.assertEqual(response.status_code, 200)

    @patch('iro.models.Applicant.save', MagicMock(name="save"))
    def test_pot(self):
        """
        Test POST Request
        """
        # Get data for POST
        data = {
            'app-first_name': "Jacob", 'app-last_name': "Bieker",
            'app-applicant_name': "Jacob Bieker",
            'app-date_of_birth': "1996-01-01",
            'app-sex': MALE,
            'app-ethnic_background': WHITE,
            'app-disadvantaged': NO,
            'app-citizenship': AMERICAN,
            'app-college': "University of Oregon",
            'app-college_class': SOPHMORE,
            'app-expected_graduation': "2018-06-02",
            'app-transfer': "Johns Hopkins University",
            'app-gpa': 3.70,
            'app-stem_gpa': 3.87,
            'app-major': "Physics/Computer and Information Science",
            'app-program': PROGRAM_1,
            'app-available_start': "2016-06-20",
            'app-available_end': "2016-08-20",
            'app-relevant_coursework': "Physics 251-3, Physics 351-3, CIS 313-5, CIS 330, PHYS 391",
            'app-learned_of': INTERNET,
            'app-previous_program': True,
            'app-previous_program_other': "Oregon Health and Science University QBB Program",
            'app-marc_current': False,
            'app-marc_past': False,
            'app-research_career': PHD,
            'app-gre_mcat': NO,
            'app-advanced_degree': MASTERS,
            'app-phone_number': 15037544585,
            'app-cell_phone_number': 5037544585,
            'app-applicant_email': "jacob@bieker.tech",
            'app-street': "1234 SE Orchard Ave",
            'app-city': "Eugene",
            'app-state': "Oregon",
            'app-zipcode': "97403",
            'app-perm_street': "4321 NW Apple Ct",
            'app-perm_city': "Portland",
            'app-perm_state': "Maine",
            'app-perm_zipcode': "97086",
            'app-background': "This is my background in research.",
            'app-goals': "I hope to get papers published from this, such as in Science or Nature! :)",
            'app-first_choice': CHOICE_1,
            'app-first_choice_importance': HIGH,
            'app-second_choice': CHOICE_2,
            'app-second_choice_importance': MEDIUM,
            'app-third_choice': CHOICE_3,
            'app-third_choice_importance': LOW,
            'app-details': "I'm into computational astrophysics, observational astronomy, "
                           "supercomputing research, and high energy physics.",
            'app-lab_preferences': "Imamura Lab, FisherGroup, Torrence Lab, and O'Day Lab.",
            'app-outside_interests': "Hiking, photography, SCUBA, skiing, backpacking, skydiving",
            'app-grades': "PHYS 353, CIS 330, HC 222H, MATH 281",
            'ref1-name': 'Jacob',
            'ref1-email': 'jacob@bieker.tech',
            'ref1-department': 'Theoretical Science',
            'ref1-institution': 'Oregon',
            'ref2-name': 'Joe',
            'ref2-email': 'joe@bieker.tech',
            'ref2-department': 'Practical Science',
            'ref2-institution': 'Oregon State',
            'ref3-name': 'Jingle',
            'ref3-email': 'jingle@bieker.tech',
            'ref3-department': 'Other Science',
            'ref3-institution': 'Oregon University',
        }
        request = self.factory.post(reverse('application'), data)
        request.user = self.user
        # Get the response
        response = get_application(request)
        self.assertEqual(response.status_code, 302)
        # Check save was called
        self.assertTrue(Applicant.save.called)
        self.assertEqual(Applicant.save.call_count, 1)

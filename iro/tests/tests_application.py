__author__ = 'jacob'

from django.test import TestCase, RequestFactory
from django.utils import timezone
from iro.models import *
from iro.choices import *
from django.contrib.auth.models import AnonymousUser, User
from iro.views import *
from django.core import mail


class ApplicantTestCase(TestCase):
    def setUp(self):
        Applicant.objects.create(first_name="Jacob", last_name="Bieker",
                                 applicant_name="Jacob Bieker",
                                 date_of_birth="1996-01-01",
                                 sex=MALE,
                                 ethnic_background=WHITE,
                                 disadvantaged=NO,
                                 citizenship=AMERICAN,
                                 college="University of Oregon",
                                 college_class=SOPHMORE,
                                 expected_graduation="2018-06-20",
                                 transfer="Johns Hopkins University",
                                 gpa=3.70,
                                 stem_gpa=3.87,
                                 major="Physics/Computer and Information Science",
                                 program=PROGRAM_1,
                                 available_start="2016-06-20",
                                 available_end="2016-08-20",
                                 relevant_coursework="Physics 251-3, Physics 351-3, CIS 313-5, CIS 330, PHYS 391",
                                 learned_of=INTERNET,
                                 previous_program=True,
                                 previous_program_other="Oregon Health and Science University QBB Program",
                                 marc_current=False,
                                 marc_past=False,
                                 research_career=PHD,
                                 gre_mcat=NO,
                                 advanced_degree=MASTERS,
                                 phone_number=15037544585,
                                 cell_phone_number=5037544585,
                                 applicant_email="jacob@bieker.tech",
                                 street="1234 SE Orchard Ave",
                                 city="Eugene",
                                 state="Oregon",
                                 zipcode="97403",
                                 perm_street="4321 NW Apple Ct",
                                 perm_city="Portland",
                                 perm_state="Maine",
                                 perm_zipcode="97086",
                                 background="This is my background in research.",
                                 goals="I hope to get papers published from this, such as in Science or Nature! :)",
                                 first_choice=CHOICE_1,
                                 first_choice_importance=HIGH,
                                 second_choice=CHOICE_2,
                                 second_choice_importance=MEDIUM,
                                 third_choice=CHOICE_3,
                                 third_choice_importance=LOW,
                                 details="I'm into computational astrophysics, observational astronomy, "
                                         "supercomputing research, and high energy physics.",
                                 lab_preferences="Imamura Lab, FisherGroup, Torrence Lab, and O'Day Lab.",
                                 outside_interests="Hiking, photography, SCUBA, skiing, backpacking, skydiving",
                                 grades="PHYS 353, CIS 330, HC 222H, MATH 281"
                                 )

    def test_applicant_exists(self):
        applicant = Applicant.objects.get(first_name="Jacob")
        self.assertEqual(applicant.state, "Oregon")
        self.assertEqual(applicant.disadvantaged_other, "")
        self.assertEqual(applicant.phone_number, 15037544585)


class ReferenceLetterTestCase(TestCase):
    def setUp(self):
        Applicant.objects.create(first_name="Jacob", last_name="Bieker",
                                 applicant_name="Jacob Bieker",
                                 date_of_birth="1996-01-01",
                                 sex=MALE,
                                 ethnic_background=WHITE,
                                 disadvantaged=NO,
                                 citizenship=AMERICAN,
                                 college="University of Oregon",
                                 college_class=SOPHMORE,
                                 expected_graduation="2018-06-20",
                                 transfer="Johns Hopkins University",
                                 gpa=3.70,
                                 stem_gpa=3.87,
                                 major="Physics/Computer and Information Science",
                                 program=PROGRAM_1,
                                 available_start="2016-06-20",
                                 available_end="2016-08-20",
                                 relevant_coursework="Physics 251-3, Physics 351-3, CIS 313-5, CIS 330, PHYS 391",
                                 learned_of=INTERNET,
                                 previous_program=True,
                                 previous_program_other="Oregon Health and Science University QBB Program",
                                 marc_current=False,
                                 marc_past=False,
                                 research_career=PHD,
                                 gre_mcat=NO,
                                 advanced_degree=MASTERS,
                                 phone_number=+15037544585,
                                 cell_phone_number=5037544585,
                                 applicant_email="jacob@bieker.tech",
                                 street="1234 SE Orchard Ave",
                                 city="Eugene",
                                 state="Oregon",
                                 zipcode="97403",
                                 perm_street="4321 NW Apple Ct",
                                 perm_city="Portland",
                                 perm_state="Maine",
                                 perm_zipcode="97086",
                                 background="This is my background in research.",
                                 goals="I hope to get papers published from this, such as in Science or Nature! :)",
                                 first_choice=CHOICE_1,
                                 first_choice_importance=HIGH,
                                 second_choice=CHOICE_2,
                                 second_choice_importance=MEDIUM,
                                 third_choice=CHOICE_3,
                                 third_choice_importance=LOW,
                                 details="I'm into computational astrophysics, observational astronomy, "
                                         "supercomputing research, and high energy physics.",
                                 lab_preferences="Imamura Lab, FisherGroup, Torrence Lab, and O'Day Lab.",
                                 outside_interests="Hiking, photography, SCUBA, skiing, backpacking, skydiving",
                                 grades="PHYS 353, CIS 330, HC 222H, MATH 281"
                                 )
        ReferenceLetter.objects.create(name="Jacob Bieker",
                                       email="jacob@bieker.tech",
                                       institution="Bieker University",
                                       department="Institute of Theoretical Science",
                                       status=WAITING_LETTER)
        ReferenceLetter.objects.create(name="Martha Bieker",
                                       email="jacob@bieker.tech",
                                       institution="OHSU",
                                       department="Primate Research Lab",
                                       status=WAITING_LETTER)
        ReferenceLetter.objects.create(name="Robert Benolken",
                                       email="jacob@bieker.tech",
                                       institution="Bieker University",
                                       department="Institute of Biology",
                                       status=WAITING_LETTER)

    def test_sending_reference_letter(self):
        letter_one = ReferenceLetter.objects.get(name="Jacob Bieker")

        letter_one.status = REQUESTED_LETTER
        letter_one.save()

        # Test that one message has been sent.
        self.assertEqual(len(mail.outbox), 1)

        print("Create this")


class ApplicationTestCase(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_application(self):
        # Create an instance of a GET request.
        request = self.factory.get('/iro/application')

        # Or you can simulate an anonymous user by setting request.user to
        # an AnonymousUser instance.
        request.user = AnonymousUser()

        # Test my_view() as if it were deployed at /customer/details
        response = get_application(request)
        self.assertEqual(response.status_code, 200)

        # Create an instance of a POST request

        post = self.factory.post("/iro/application/", {'first_name': 'Jacob', 'last_name': 'Bieker',
                                                       'applicant_name': 'Jacob Bieker', 'date_of_birth': '1996-01-01',
                                                       'sex': MALE, 'ethnic_background': WHITE, 'disadvantaged': NO,
                                                       'citizenship': AMERICAN, 'college': 'University of Oregon',
                                                       'college_class': SOPHMORE, 'expected_graduation': '2018-06-20',
                                                       'gpa': 3.81, 'stem_gpa': 4.00, 'major': 'Physics',
                                                       'program': PROGRAM_1, 'available_start': '2018-06-20',
                                                       'available_end': '2018-08-20',
                                                       'relevant_coursework': 'Physics 251-3',
                                                       'learned_of': INTERNET, 'previous_program': False,
                                                       'marc_current': False, 'marc_past': False,
                                                       'research_career': PHD, 'gre_mcat': NO,
                                                       'advanced_degree': MASTERS, 'phone_number': 15554443322,
                                                       'cell_phone_number': 5554443322,
                                                       'applicant_email': 'jacob@bieker.tech',
                                                       'street': '1234 Orchard Ave', 'city': 'Eugene',
                                                       'state': 'Oregon', 'zipcode': '97403',
                                                       'perm_street': '4321 NW Apple Ct', 'perm_city': 'Portland',
                                                       'perm_state': 'Maine', 'perm_zipcode': '97086',
                                                       'background': 'This is my background in research',
                                                       'goals': 'Hope to get this published',
                                                       'first_choice': CHOICE_1, 'first_choice_importance': HIGH,
                                                       'second_choice': CHOICE_2, 'second_choice_importance': MEDIUM,
                                                       'third_choice': CHOICE_3, 'third_choice_importance': LOW,
                                                       'details': 'I am into computational physics',
                                                       'lab_preferences': 'Imamura Lab, CDUX, O\'Day Lab, FisherGroup',
                                                       'outside_interests': 'SCUBA, hiking, skiing, photography',
                                                       'grades': 'PHYS 391, A'})

        post.user = AnonymousUser()

        # Test if the POST works
        post_response = get_application(post)
        self.assertEqual(post_response.status_code, 200)

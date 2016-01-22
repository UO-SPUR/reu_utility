__author__ = 'jacob'

from django.test import TestCase
from django.utils import timezone
from iro.models import *
from iro.choices import *

class ApplicantTestCase(TestCase):
    def setUp(self):
        Applicant.objects.create(first_name="Jacob", last_name="Bieker",
                                 applicant_name="Jacob Bieker",
                                 date_of_birth="01/01/1996",
                                 sex=MALE,
                                 ethnic_background=WHITE,
                                 disadvantaged=NO,
                                 citizenship=AMERICAN,
                                 college="University of Oregon",
                                 college_class=SOPHMORE,
                                 expected_graduation="06/12/2018",
                                 transfer="Johns Hopkins University",
                                 gpa=3.70,
                                 stem_gpa=3.87,
                                 major="Physics/Computer and Information Science",
                                 program=PROGRAM_1,
                                 available_start="06/20/2016",
                                 available_end="08/20/2016",
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


class ReferenceLetterTestCase(TestCase):
    def setUp(self):
        Applicant.objects.create(first_name="Jacob", last_name="Bieker",
                                 applicant_name="Jacob Bieker",
                                 date_of_birth="01/01/1996",
                                 sex=MALE,
                                 ethnic_background=WHITE,
                                 disadvantaged=NO,
                                 citizenship=AMERICAN,
                                 college="University of Oregon",
                                 college_class=SOPHMORE,
                                 expected_graduation="06/12/2018",
                                 transfer="Johns Hopkins University",
                                 gpa=3.70,
                                 stem_gpa=3.87,
                                 major="Physics/Computer and Information Science",
                                 program=PROGRAM_1,
                                 available_start="06/20/2016",
                                 available_end="08/20/2016",
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


class ApplicationTestCase(TestCase):
    def setUp(self):
        Applicant.objects.create()
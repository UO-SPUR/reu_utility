__author__ = 'jacob'

from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User, Group
from iro.models import *
from iro.choices import *

class AbstractTestCase(TestCase):
    def setUp(self):
        Group.objects.create(name=INTERN_GROUP_NAME)
        Group.objects.create(name=FACULTY_GROUP_NAME)
        Group.objects.create(name=MENTOR_GROUP_NAME)
        Applicant.objects.create(first_name="Jacob", last_name="Bieker",
                                 applicant_name="Jacob Bieker",
                                 date_of_birth="1996-01-01",
                                 sex=MALE,
                                 ethnic_background=WHITE,
                                 disadvantaged=NO,
                                 citizenship=AMERICAN,
                                 college="University of Oregon",
                                 college_class=SOPHMORE,
                                 expected_graduation="2018-06-02",
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
        Institute.objects.create(name="Bieker Institute of Technology",
                                 street="Einstein Blvd",
                                 city="Geneva",
                                 state="Switzerland",
                                 zipcode="97412",
                                 discipline="High-Energy Physics")
        ######## Create Faculty User nad Object ############
        User.objects.create(username="iroUtility",
                            email="no-reply@example.com",
                            password="123456",
                            groups=Group.objects.get(name=FACULTY_GROUP_NAME)
                            )
        Faculty.objects.create(user=User.objects.get(username="iroUtility"),
                               faculty_name="Robert Benolken",
                               institute=Institute.objects.get(city="Geneva"))
        ######### Create Mentor User and Object ##############
        User.objects.create(username="iroMentor",
                            email="no-reply@example.com",
                            password="123456",
                            groups=Group.objects.get(name=MENTOR_GROUP_NAME),
                            )
        Mentor.objects.create(user=User.objects.get(username="iroMentor"),
                              mentor_name="Mentor One",
                              professor=Faculty.objects.get(faculty_name="Robert Benolken"))
        ######### Create Intern User and Object ###############
        User.objects.create(username="iroIntern",
                            email="no-reply@example.com",
                            password="123456",
                            groups=Group.objects.get(name=INTERN_GROUP_NAME))
        Intern.objects.create(user=User.objects.get(username="iroIntern"),
                              name=Applicant.objects.get(applicant_name="Jacob Bieker"),
                              professor=Faculty.objects.get(faculty_name="Robert Benolken"),
                              mentors=Mentor.objects.get(mentor_name="Mentor One"))

    def test_abstract_creation(self):
        intern = Intern.objects.get(user=User.objects.get(applicant_name="Jacob Bieker"))

        abstract = Abstract.objects.create(title="Jacob's Ladder",
                                           content="In this project, we looked at the world changing features of "
                                                   "the Jacob's Ladder system.")

        self.assertEqual(abstract.title, "Jacob's Ladder")
        self.assertEqual(abstract.content, "In this project, we looked at the world changing features of "
                                           "the Jacob's Ladder system.")

    def test_abstract_change(self):
        intern = Intern.objects.get(user=User.objects.get(applicant_name="Jacob Bieker"))

        abstract = Abstract.objects.create(title="Jacob's Ladder",
                                           content="In this project, we looked at the world changing features of "
                                                   "the Jacob's Ladder system.")

        abstract.content = "Jacob's Ladder System is amazing."

        self.assertEqual(abstract.content, "Jacob's Ladder System is amazing.")

        abstract.title = "Ladder of Jacob"

        self.assertEqual(abstract.title, "Ladder of Jacob")

    def test_abstract_to_intern(self):
        intern = Intern.objects.get(user=User.objects.get(applicant_name="Jacob Bieker"))

        abstract = Abstract.objects.create(title="Jacob's Ladder",
                                           content="In this project, we looked at the world changing features of "
                                                   "the Jacob's Ladder system.")

        intern.abstract = abstract

        self.assertEqual(intern.abstract.title, "Jacob's Ladder")
        self.assertEqual(intern.abstract.content, "In this project, we looked at the world changing features of "
                                                  "the Jacob's Ladder system.")



class ProgressReportTestCase(TestCase):
    def setUp(self):
        Group.objects.create(name=INTERN_GROUP_NAME)
        Group.objects.create(name=FACULTY_GROUP_NAME)
        Group.objects.create(name=MENTOR_GROUP_NAME)
        Applicant.objects.create(first_name="Jacob", last_name="Bieker",
                                 applicant_name="Jacob Bieker",
                                 date_of_birth="1996-01-01",
                                 sex=MALE,
                                 ethnic_background=WHITE,
                                 disadvantaged=NO,
                                 citizenship=AMERICAN,
                                 college="University of Oregon",
                                 college_class=SOPHMORE,
                                 expected_graduation="2018-06-02",
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
        Institute.objects.create(name="Bieker Institute of Technology",
                                 street="Einstein Blvd",
                                 city="Geneva",
                                 state="Switzerland",
                                 zipcode="97412",
                                 discipline="High-Energy Physics")
        ######## Create Faculty User nad Object ############
        User.objects.create(username="iroUtility",
                            email="no-reply@example.com",
                            password="123456",
                            groups=Group.objects.get(name=FACULTY_GROUP_NAME)
                            )
        Faculty.objects.create(user=User.objects.get(username="iroUtility"),
                               faculty_name="Robert Benolken",
                               institute=Institute.objects.get(city="Geneva"))
        ######### Create Mentor User and Object ##############
        User.objects.create(username="iroMentor",
                            email="no-reply@example.com",
                            password="123456",
                            groups=Group.objects.get(name=MENTOR_GROUP_NAME),
                            )
        Mentor.objects.create(user=User.objects.get(username="iroMentor"),
                              mentor_name="Mentor One",
                              professor=Faculty.objects.get(faculty_name="Robert Benolken"))
        ######### Create Intern User and Object ###############
        User.objects.create(username="iroIntern",
                            email="no-reply@example.com",
                            password="123456",
                            groups=Group.objects.get(name=INTERN_GROUP_NAME))
        Intern.objects.create(user=User.objects.get(username="iroIntern"),
                              name=Applicant.objects.get(applicant_name="Jacob Bieker").name(),
                              professor=Faculty.objects.get(faculty_name="Robert Benolken"),
                              mentors=Mentor.objects.get(mentor_name="Mentor One"))
        ProgressReport.objects.create(intern=Intern.objects.get(professor=Faculty.objects
                                                                .get(faculty_name="Robert Benolken")),
                                      week=10,
                                      content="This is a sample progress report.")

    def test_progress_existence(self):
        report = ProgressReport.objects.get(week=10)

        self.assertEqual(report.content(), "This is a sample progress report.")

    def test_change_progress_report(self):
        report = ProgressReport.objects.get(week=10)

        report.week = 5

        self.assertEqual(report.week, 5)
        self.assertEqual(report.content(), "This is a sample progress report.")
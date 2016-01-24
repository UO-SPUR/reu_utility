__author__ = 'jacob'
from django.test import TestCase
from django.contrib.auth.models import User, Group
from django.utils import timezone
from iro.models import *
from iro.choices import *


class FacultyTestCase(TestCase):
    def setUp(self):
        Group.objects.create(name=FACULTY_GROUP_NAME)
        Institute.objects.create(name="Bieker Institute of Technology",
                                 street="Einstein Blvd",
                                 city="Geneva",
                                 state="Switzerland",
                                 zipcode="97412",
                                 discipline="High-Energy Physics")
        User.objects.create(username="iroUtility",
                            email="no-reply@example.com",
                            password="123456",
                            groups=Group.objects.get(name=FACULTY_GROUP_NAME)
                            )
        Faculty.objects.create(user=User.objects.get(username="iroUtility"),
                               faculty_name="Robert Benolken",
                               institute=Institute.objects.get(city="Geneva"))

    def test_faculty_exists(self):
        faculty = Faculty.objects.get(faculty_name="Robert Benolken")
        self.assertEqual(faculty.institute(), Institute.objects.get(city="Geneva"))
        self.assertEqual(faculty.user(), User.objects.get(username="iroUtility"))
        self.assertEqual(faculty.user.groups.filter(name=FACULTY_GROUP_NAME).exists(), True)


class MentorTestCase(TestCase):
    def setUp(self):
        Group.objects.create(name=FACULTY_GROUP_NAME)
        Group.objects.create(name=MENTOR_GROUP_NAME)
        Institute.objects.create(name="Bieker Institute of Technology",
                                 street="Einstein Blvd",
                                 city="Geneva",
                                 state="Switzerland",
                                 zipcode="97412",
                                 discipline="High-Energy Physics")
        User.objects.create(username="iroUtility",
                            email="no-reply@example.com",
                            password="123456",
                            groups=Group.objects.get(name=FACULTY_GROUP_NAME)
                            )
        Faculty.objects.create(user=User.objects.get(username="iroUtility"),
                               faculty_name="Robert Benolken",
                               institute=Institute.objects.get(city="Geneva"))
        User.objects.create(username="iroMentor",
                            email="no-reply@example.com",
                            password="123456",
                            groups=Group.objects.get(name=MENTOR_GROUP_NAME),
                            )
        Mentor.objects.create(user=User.objects.get(username="iroMentor"),
                              mentor_name="Mentor One",
                              professor=Faculty.objects.get(faculty_name="Robert Benolken"))

    def test_mentor_exists(self):
        faculty = Faculty.objects.get(faculty_name="Robert Benolken")
        mentor = Mentor.objects.get(mentor_name="Mentor One")
        self.assertEqual(faculty.institute(), Institute.objects.get(city="Geneva"))
        self.assertEqual(faculty.user(), User.objects.get(username="iroUtility"))
        self.assertEqual(faculty.user.groups.filter(name=FACULTY_GROUP_NAME).exists(), True)

        self.assertEqual(mentor.user(), User.objects.get(username="iroMentor"))
        self.assertEqual(mentor.professor(), Faculty.objects.get(faculty_name="Robert Benolken"))
        self.assertEqual(mentor.mentor_name(), "Mentor One")
        self.assertEqual(mentor.user.groups.filter(name=MENTOR_GROUP_NAME).exists(), True)


class InternTestCase(TestCase):
    def setUp(self):
        Group.objects.create(name=INTERN_GROUP_NAME)
        Group.objects.create(name=FACULTY_GROUP_NAME)
        Group.objects.create(name=MENTOR_GROUP_NAME)
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

    def test_intern_exists(self):
        faculty = Faculty.objects.get(faculty_name="Robert Benolken")
        mentor = Mentor.objects.get(mentor_name="Mentor One")
        intern = Intern.objects.get(applicant_name="Jacob Bieker")
        self.assertEqual(faculty.institute(), Institute.objects.get(city="Geneva"))
        self.assertEqual(faculty.user(), User.objects.get(username="iroUtility"))
        self.assertEqual(faculty.user.groups.filter(name=FACULTY_GROUP_NAME).exists(), True)

        self.assertEqual(mentor.user(), User.objects.get(username="iroMentor"))
        self.assertEqual(mentor.professor(), Faculty.objects.get(faculty_name="Robert Benolken"))
        self.assertEqual(mentor.mentor_name(), "Mentor One")
        self.assertEqual(mentor.user.groups.filter(name=MENTOR_GROUP_NAME).exists(), True)

        self.assertEqual(intern.user(), User.objects.get(username="iroMentor"))
        self.assertEqual(intern.professor(), Faculty.objects.get(faculty_name="Robert Benolken"))
        self.assertEqual(intern.mentors(), Mentor.objects.get(mentor_name="Mentor One"))
        self.assertEqual(intern.name(), "Jacob Bieker")
        self.assertEqual(intern.user.groups.filter(name=INTERN_GROUP_NAME).exists(), True)

    def test_intern_urls(self):
        intern = Intern.objects.get(applicant_name="Jacob Bieker")

        intern.presentation_oral = "https://www.google.com"
        intern.presentation_poster = "https://www.google.com"

        self.assertEqual(intern.presentation_poster, "https://www.google.com")
        self.assertEqual(intern.presentation_oral, "https://www.google.com")

    def test_intern_foreign_keys(self):
        intern = Intern.objects.get(applicant_name="Jacob Bieker")

        intern.institute = Institute.objects.get(city="Geneva")
        self.assertEqual(intern.institute, Institute.objects.get(city="Geneva"))

        #TODO test many to many mentor field

    def test_intern_files(self):
        intern = Intern.objects.get(applicant_name="Jacob Bieker")

        #TODO uploading a picture file to the image field
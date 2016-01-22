__author__ = 'jacob'
from django.test import TestCase
from django.contrib.auth.models import User, Group
from django.utils import timezone
from iro.models import *
from iro.choices import *


class FacultyTestCase(TestCase):
    def setUp(self):
        Institute.objects.create(name="Bieker Institute of Technology",
                                 street="Einstein Blvd",
                                 city="Geneva",
                                 state="Switzerland",
                                 zipcode="97412",
                                 discipline="High-Energy Physics")
        User.objects.create(username="iroUtility",
                            email="no-reply@example.com",
                            password="123456",
                            groups=Group.objects.get(name="Faculty")
                            )
        Faculty.objects.create(user=User.objects.get(username="iroUtility"),
                               faculty_name="Robert Benolken",
                               institute=Institute.objects.get(city="Geneva"))

    def test_faculty_exists(self):
        faculty = Faculty.objects.get(faculty_name="Robert Benolken")
        self.assertEqual(faculty.institute(), Institute.objects.get(city="Geneva"))
        self.assertEqual(faculty.user(), User.objects.get(username="iroUtility"))
        self.assertEqual(faculty.user.groups.filter(name="Faculty").exists(), True)


class MentorTestCase(TestCase):
    def setUp(self):
        Institute.objects.create(name="Bieker Institute of Technology",
                                 street="Einstein Blvd",
                                 city="Geneva",
                                 state="Switzerland",
                                 zipcode="97412",
                                 discipline="High-Energy Physics")
        User.objects.create(username="iroUtility",
                            email="no-reply@example.com",
                            password="123456",
                            groups=Group.objects.get(name="Faculty")
                            )
        Faculty.objects.create(user=User.objects.get(username="iroUtility"),
                               faculty_name="Robert Benolken",
                               institute=Institute.objects.get(city="Geneva"))
        User.objects.create(username="iroMentor",
                            email="no-reply@example.com",
                            password="123456",
                            groups=Group.objects.get(name="Mentor"),
                            )
        Mentor.objects.create(user=User.objects.get(username="iroMentor"),
                              mentor_name="Mentor One",
                              professor=Faculty.objects.get(faculty_name="Robert Benolken"))

    def test_mentor_exists(self):
        faculty = Faculty.objects.get(faculty_name="Robert Benolken")
        mentor = Mentor.objects.get(mentor_name="Mentor One")
        self.assertEqual(faculty.institute(), Institute.objects.get(city="Geneva"))
        self.assertEqual(faculty.user(), User.objects.get(username="iroUtility"))
        self.assertEqual(faculty.user.groups.filter(name="Faculty").exists(), True)

        self.assertEqual(mentor.user(), User.objects.get(username="iroMentor"))
        self.assertEqual(mentor.professor(), Faculty.objects.get(faculty_name="Robert Benolken"))
        self.assertEqual(mentor.mentor_name(), "Mentor One")
        self.assertEqual(mentor.user.groups.filter(name="Mentor").exists(), True)


class InternTestCase(TestCase):
    def setUp(self):
        Intern.objects.create()

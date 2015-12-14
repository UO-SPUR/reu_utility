__author__ = 'jacob'

from reu_utility.settings import *
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from iro.models import Faculty, Intern, Mentor

Intern_group, intern_group_created = Group.objects.get_or_create(name=INTERN_GROUP_NAME)
Faculty_group, faculty_group_created = Group.objects.get_or_create(name=FACULTY_GROUP_NAME)
Mentor_group, mentor_group_created = Group.objects.get_or_create(name=MENTOR_GROUP_NAME)

# Code to add permission to group
faculty_ct = ContentType.objects.get_for_model(Faculty)
intern_ct = ContentType.objects.get_for_model(Intern)
mentor_ct = ContentType.objects.get_for_model(Mentor)

# Getting the relevant Permissions to be assigned later

# Intern Permissions
permission = Permission.objects.create(codename='can_add_project',
                                       name='Can add project',
                                       content_type=ct)

# Faculty Permissions

# Mentor Permissions
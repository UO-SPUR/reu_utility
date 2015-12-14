__author__ = 'jacob'

from iro.choices import INTERN_GROUP_NAME, FACULTY_GROUP_NAME, MENTOR_GROUP_NAME
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

# Faculty Permissions

# Mentor Permissions


# Adding to group ones


def add_user_to_intern_group(sender, instance, created, **kwargs):
    """Post-create user signal that adds the user to everyone group."""

    try:
        if created:
            instance.groups.add(Group.objects.get(name=INTERN_GROUP_NAME))
    except Group.DoesNotExist:
        pass


def add_user_to_mentor_group(sender, instance, created, **kwargs):
    """Post-create user signal that adds the user to everyone group."""

    try:
        if created:
            instance.groups.add(Group.objects.get(name=MENTOR_GROUP_NAME))
    except Group.DoesNotExist:
        pass


def add_user_to_faculty_group(sender, instance, created, **kwargs):
    """Post-create user signal that adds the user to everyone group."""

    try:
        if created:
            instance.groups.add(Group.objects.get(name=FACULTY_GROUP_NAME))
    except Group.DoesNotExist:
        pass
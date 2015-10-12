from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Applicant(models.Model):
    ############## Basic Info ###############################
    first_name = models.CharField("Applicant First Name", help_text="Enter your first name", max_length=20)
    last_name = models.CharField("Applicant Last Name", help_text="Enter your last name", max_length=40)
    applicant_name = models.CharField("Applicant Full Name", help_text="Enter your full name", max_length=200)
    date_of_birth = models.DateField("Applicant Date of Birth", help_text="Please choose date of birth")
    gender = models.TextField("Applicant Gender", help_text="Please enter your preferred gender")
    ethnic_background = models.TextField("Ethnic Background", help_text="Please enter your ethnic background") #TODO create a choices list for this

    ############## End Basic Info ###########################
    ########Contact Info ########################################
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField("Applicant Phone Number", validators=[phone_regex], blank=True) # validators should be a list
    applicant_email = models.EmailField("Applicant Email", help_text="Enter your email address")
    address = models.ForeignKey(Address, verbose_name="Applicant Address")
    permanent_address = models.ForeignKey(Address, verbose_name="Permanent Address")

    ####### End Contact Info ####################################
    ########### Degree section of application model ##############
    HIGH_SCHOOL = 'High School'
    ASSOCIATES = 'Associates'
    BACHELOR = 'Bachelors'
    MASTERS = 'Masters'
    PHD = 'PhD'
    ADVANCED_DEGREE_CHOICES = (
        (HIGH_SCHOOL, 'High School'),
        (ASSOCIATES, 'Associates'),
        (BACHELOR, 'Bachelors'),
        (MASTERS, 'Masters'),
        (PHD, 'Ph.D')
    )

    advanced_degree = models.CharField("Adanced Degree", max_length=11,
                                       choices=ADVANCED_DEGREE_CHOICES,
                                       default=HIGH_SCHOOL)
    advanced_degree_other = models.CharField("Other Advanced Degree", max_length=11,
                                             choices=ADVANCED_DEGREE_CHOICES,
                                             default=HIGH_SCHOOL)
    ########## End Degree Section ###################################

    mentors = models.ForeignKey(Mentor, verbose_name="Possible Mentors")
    possible_pis = models.ForeignKey(Faculty, verbose_name="Possible PIs")


class Mentor(models.Model):
    mentor_name = models.CharField(max_length=200)

class Faculty(models.Model):
    faculty_name = models.CharField(max_length=200)

######################### Models for use in above Models ################################
class Address(models.Model):
    street = models.TextField()
    city = models.TextField()
    province = models.TextField()
    code = models.TextField()
    country = models.TextField()
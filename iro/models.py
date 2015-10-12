from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Mentor(models.Model):
    mentor_name = models.CharField(max_length=200)

class Faculty(models.Model):
    faculty_name = models.CharField(max_length=200)

class Address(models.Model):
    street = models.TextField("Street", help_text="Enter street name")
    city = models.TextField("City", help_text="Enter your city's name")
    state = models.TextField("State", help_text="Enter your state")
    zipcode = models.TextField("Zip Code", help_text="Enter ZIP Code")


class Applicant(models.Model):
    ############## Basic Info ###############################
    first_name = models.CharField("Applicant First Name", help_text="Enter your first name", max_length=20)
    last_name = models.CharField("Applicant Last Name", help_text="Enter your last name", max_length=40)
    applicant_name = models.CharField("Applicant Full Name", help_text="Enter your full name", max_length=200)
    date_of_birth = models.DateField("Applicant Date of Birth", help_text="Please choose date of birth")
    gender = models.TextField("Applicant Gender", help_text="Please enter your preferred gender") #TODO Create a Male / Female Choise list
    ethnic_background = models.TextField("Ethnic Background", help_text="Please enter your ethnic background",
                                         max_length=300)
    disadvantaged = models.TextField("Disadvantaged Status", help_text="Disadvanted in any way?")
    citizenship = models.CharField("Citizenship", help_text="Enter your citizenship", max_length=100)

    ##### College Info #####
    college = models.CharField("College", help_text="Enter the name of your college or university", max_length=70)
    expected_graduation = models.DateField("Expected Graduation", help_text="Choose your expected graduation time")
    transfer = models.CharField("Transfer?", help_text="Did you transfer from any other school or university? If so, "
                                                       "write that here.", max_length=100)
    gpa = models.FloatField("GPA", help_text="Please type your current GPA.")
    stem_gpa = models.FloatField("STEM GPA", help_text="Please enter your current STEM (Science, Technology, Engineerin"
                                                       "g, Math) GPA")
    major = models.CharField("Major", help_text="Please enter your major", max_length=100)
    program = models.CharField("Program Applied To", help_text="What program are you applying to?", max_length=20) #TODO create a choice list for this
    available = models.DurationField("Available Dates", help_text="Choose what date range you are available")

    ###### End College Info ####

    ###### Misc Info ########
    learned_of = models.CharField("Learned of Program", help_text="How did you learn about this program?", max_length=50)
    previous_program = models.BooleanField("Previous Program?", help_text="Did you participate in this program before?")
    marc_current = models.BooleanField("MARC?", help_text="Are you currently part of MARC?")
    marc_past = models.BooleanField("MARC (past)?", help_text="Did you used to be part of MARC?")
    research_career = models.CharField("Research Career?", help_text="Do you want to pursue a career in research?", max_length=6) #TODO create a choice list for this
    gre_mcat = models.CharField("GRE/MCAT", help_text="What are your GRE/MCAT scores (if taken)?", max_length=20)
    date_of_test = models.DateField("GRE/MCAT Date", help_text="When did you take the GRE/MCAT (if applicable)?", null=True)

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

    ###### End Misc Info ####

    ############## End Basic Info ###########################

    ########Contact Info ########################################
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField("Applicant Phone Number", validators=[phone_regex], blank=True, max_length=15) # validators should be a list
    cell_phone_number = models.CharField("Applicant Cell Phone Number", validators=[phone_regex], blank=True, max_length=15) # validators should be a list
    applicant_email = models.EmailField("Applicant Email", help_text="Enter your email address")
    address = models.ForeignKey(Address, verbose_name="Applicant Address", related_name="applicant_address")
    permanent_address = models.ForeignKey(Address, verbose_name="Permanent Address", related_name="applicant_perm_address")

    ####### End Contact Info ####################################

    ########## Question Fields and preferences ############################################

    background = models.TextField("Background", help_text="Please enter your background.")
    goals = models.TextField("Goals", help_text="What are your goals?")
    first_choice = models.CharField("1st Choice", help_text="Write your first choice for this program.", max_length=50)
    #TODO Write a choice list for the importance part
    first_choice_importance = models.CharField("1st Importance", help_text="How important is this choice?", max_length=12)
    second_choice = models.CharField("2nd Choice", help_text="Write your second choice for this program.", max_length=50)
    second_choice_importance = models.CharField("2nd Importance", help_text="How important is this choice?", max_length=12)
    third_choice = models.CharField("3rd Choice", help_text="Write your third choice for this program.", max_length=50)
    third_choice_importance = models.CharField("3rd Importance", help_text="How important is this choice?", max_length=12)

    mentors = models.ForeignKey(Mentor, verbose_name="Possible Mentors")
    possible_pis = models.ForeignKey(Faculty, verbose_name="Possible PIs")

    ########## Question Fields and preferences ############################################
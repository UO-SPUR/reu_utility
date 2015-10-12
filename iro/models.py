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
                                         max_length=300) # TODO Create a choice list for this: (African American, Alaska Native,
                                         #TODO Asian, Hispanic, Native american, Pacific Islander, White, Multiracial, Other, Decline Response
    ethnic_background_other = models.CharField("Ethinc Background Other", help_text="If 'Multiracial' or 'Other', please explain", max_length=100)
    disadvantaged = models.TextField("Disadvantaged Status", help_text="Do you claim Disadvantaged Status?")
    #TODO create choice list for this: No, First generation to attend College, Low Income, Other or multiple - Please explain
    disadvantaged_other = models.CharField("Disadvantaged Other", help_text="If 'Other or multiple', please explain", max_length=200)
    citizenship = models.CharField("Citizenship", help_text="Enter your citizenship", max_length=100)

    ##### College Info #####
    college = models.CharField("College", help_text="Enter the name of your college or university", max_length=70)
    expected_graduation = models.DateField("Expected Graduation", help_text="Choose your expected graduation time")
    transfer = models.CharField("Transfer?", help_text="If you transferred from another institution, please list.", max_length=100)
    gpa = models.FloatField("GPA", help_text="Please type your current GPA.")
    stem_gpa = models.FloatField("STEM GPA", help_text="Please enter your current STEM (Science, Technology, Engineerin"
                                                       "g, Math) GPA")
    major = models.CharField("Major", help_text="Please enter your major", max_length=100)
    program = models.CharField("Program Applied To", help_text="What program are you applying to?", max_length=20) #TODO create a choice list for this
    available = models.DurationField("Available Dates", help_text="Choose what date range you are available")

    ###### End College Info ####

    ###### Misc Info ########
    learned_of = models.CharField("Learned of Program", help_text="How did you learn about this program?", max_length=50)
    #TODO Create choice list for this: Internet Search, ABRCMS meeting, SACNAS meeting, AISES meeting, College Advisor, Mailing or poster, other
    previous_program = models.BooleanField("Previous Program?", help_text="Have you participated previously in a summer undergraduate research program at another institution?")
    previous_program_other = models.CharField("Previous Program Other", help_text="If so, list name of the Program and Institution")
    marc_current = models.BooleanField("MARC?", help_text="Are you currently a MARC Scholar?")
    marc_past = models.BooleanField("MARC (past)?", help_text="Did you used to be a MARC Scholar?")
    research_career = models.CharField("Research Career?", help_text="Do you want to pursue a career in research?", max_length=6) #TODO create a choice list for this
    gre_mcat = models.CharField("GRE/MCAT", help_text="Do you plan to take the GRE, MCAT or other graduate/professional school admissions standardized exam?", max_length=20)
    #TODO Create choice list for gre_mcat with: No, GRE, MCAT, DAT, VCAT, LSAT, GMAT, Other
    date_of_test = models.DateField("GRE/MCAT Date", help_text="When did you take the GRE/MCAT (if applicable)?", null=True)

    ########### Degree section of application model ##############
    #TODO Add more, such as MD, 'Other Professional Degree, e.g. DDS, DVM, etc.', Unsure, possibly PhD, PhD and MD, Unsure, No
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
    advanced_degree_other = models.CharField("Other Advanced Degree", help_text="If 'Other', please specify", max_length=20)
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

    background = models.TextField("Background", help_text="Describe your academic background, scientific interests, "
                                                          "goals, and past research experience (if any). "
                                                          "Include significant science courses you have taken and"
                                                          " specific laboratory techniques you may have used. (Note: "
                                                          "prior research experience is not required)")
    goals = models.TextField("Goals", help_text="Why do you want to participate in a Summer research experience? "
                                                "Explain what you hope to gain from the Summer experience and how it "
                                                "will help you pursue your career and personal goals.")
    first_choice = models.CharField("1st Choice", help_text="Write your first choice for this program.", max_length=50)
    #TODO Write a choice list for the importance part: High, Medium, Low
    #TODO Write a choice list for choices, not sure how to make it super general though
    first_choice_importance = models.CharField("1st Importance", help_text="How important is this choice?", max_length=12)
    second_choice = models.CharField("2nd Choice", help_text="Write your second choice for this program.", max_length=50)
    second_choice_importance = models.CharField("2nd Importance", help_text="How important is this choice?", max_length=12)
    third_choice = models.CharField("3rd Choice", help_text="Write your third choice for this program.", max_length=50)
    third_choice_importance = models.CharField("3rd Importance", help_text="How important is this choice?", max_length=12)
    other_choice = models.CharField("Other Choice", help_text="Others?", max_length=100, null=True)
    details = models.TextField("Details", help_text="(Optional) Please give a more detailed description of your "
                                                    "research interests: Are your interests broad? Have you "
                                                    "narrowed them down? Do you have defined interests in "
                                                    "several areas?", null=True)
    lab_preferences = models.TextField("Lab Preferences", help_text="After viewing the participating laboratories, "
                                                                    "please list a few laboratories for which you "
                                                                    "might have a preference (if any).", null=True)
    outside_interests = models.TextField("Outside Activites", help_text="(Optional) Describe your outside interests "
                                                                        "and activities.", null=True)
    grades = models.TextField("Grades/Classes", help_text="Paste or type your classes and grades here -- (as neatly "
                                                          "as possible; no official transcripts or images; please "
                                                          "include courses you are currently taking)")
    faculty_reference_one = models.CharField("Faculty 1", help_text="Name; Department; Institution", max_length=100)
    faculty_reference_one_email = models.EmailField("Faculty 1 Email", help_text="Email")
    faculty_reference_two = models.CharField("Faculty 2", help_text="Name; Department; Institution", max_length=100)
    faculty_reference_two_email = models.EmailField("Faculty 2 Email", help_text="Email")
    faculty_reference_three = models.CharField("Faculty 3", help_text="Name; Department; Institution", max_length=100)
    faculty_reference_three_email = models.EmailField("Faculty 3 Email", help_text="Email")
    ########## End Question Fields and preferences ############################################

    ######### Administrative fields ###########################################################
    mentors = models.ForeignKey(Mentor, verbose_name="Possible Mentors")
    possible_pis = models.ForeignKey(Faculty, verbose_name="Possible PIs")
    triage = models.CharField("Triage", max_length=10) #TODO Figure out what this is supposed to do
    ranking = models.CharField("Ranking", help_text="What is the ranking of this applicant?", max_length=20)
    likely_institute = models.CharField("Likely Institute", help_text="What institute would this applicant be a part of?", max_length=80)
    decision_action = models.CharField("Decision", help_text="Final decision on applicant", max_length=20) #TODO Choice for this
    comments = models.TextField("Admin Comments", help_text="Comments on Applicant")
    application_completeness = models.TextField("Application Completeness", help_text="Anything missing?")
    correspondence = models.TextField("Correspondence", help_text="Correspondence")
    year_created = models.DateField("Created Year", help_text="Year Created")
    #########End Administrative fields ###########################################################

class Intern(models.Model):
    application = models.ForeignKey(Applicant, verbose_name="Intern Application")
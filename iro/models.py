from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
from iro.choices import *
from django.core.exceptions import ValidationError
import uuid
from django.utils.timezone import now
from django.core.mail import send_mail
from reu_utility.settings import EMAIL_HOST_USER
# Allow only one model to be created (For Setup)
def validate_only_one_instance(obj):
    model = obj.__class__
    if (model.objects.count() > 0 and
                obj.id != model.objects.get().id):
        raise ValidationError("Can only create 1 %s instance" % model.__name__)


# Create your models here.

class Institute(models.Model):
    name = models.CharField(max_length=200)
    street = models.CharField("Street", help_text="Enter street name", max_length=200, null=True)
    city = models.CharField("City", help_text="Enter your city's name", max_length=200, null=True)
    state = models.CharField("State", help_text="Enter your state", max_length=200, null=True)
    zipcode = models.CharField("Zip Code", help_text="Enter ZIP Code", max_length=200, null=True)
    discipline = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Faculty(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    faculty_name = models.CharField(max_length=200)
    email_template = models.TextField("Email Template", help_text="Enter a template for emails", null=True)
    correspondence = models.TextField("Correspondence", help_text="Correspondence with Professor", null=True)
    institute = models.ForeignKey(Institute, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.faculty_name


class Mentor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    mentor_name = models.CharField(max_length=200)
    professor = models.ManyToManyField(Faculty, verbose_name="Mentors")

    def __str__(self):
        return self.mentor_name


class Abstract(models.Model):
    title = models.TextField("Abstract Title", help_text="Title of Abstract")
    last_updated = models.DateField("Last Updated", help_text="Timestamp of last modification", auto_now=True)
    content = models.TextField("Abstract", help_text="Enter the abstract here")

    def __str__(self):
        return self.title


class Applicant(models.Model):
    ############## Basic Info ###############################
    first_name = models.CharField("Applicant First Name", help_text="Enter your first name", max_length=20)
    last_name = models.CharField("Applicant Last Name", help_text="Enter your last name", max_length=40)
    applicant_name = models.CharField("Applicant Full Name", help_text="Enter your full name", max_length=200)
    date_of_birth = models.DateField("Applicant Date of Birth", help_text="Please choose date of birth")
    sex = models.CharField("Applicant Sex", help_text="Please choose your sex", max_length=6, choices=SEX_CHOICES,
                           default=DECLINE)
    ethnic_background = models.CharField("Ethnic Background", help_text="Please choose your ethnic background",
                                         max_length=30, choices=ETHNIC_CHOICES, default=OTHER)
    ethnic_background_other = models.CharField("Ethinc Background Other",
                                               help_text="If 'Multiracial' or 'Other', please explain", max_length=150)
    disadvantaged = models.CharField("Disadvantaged Status", help_text="Do you claim Disadvantaged Status?",
                                     max_length=25,
                                     choices=DISADVANTAGED_CHOICES, default=NO)
    disadvantaged_other = models.CharField("Disadvantaged Other", help_text="If 'Other or multiple', please explain",
                                           max_length=200)
    citizenship = models.CharField("Citizenship", help_text="Enter your citizenship", choices=CITIZEN_CHOICES,
                                   default=AMERICAN, max_length=100)

    ##### College Info #####
    college = models.CharField("College", help_text="Enter the name of your college or university", max_length=70)
    college_class = models.CharField("Class", help_text="What year are you in college?", choices=CLASS_CHOICES,
                                     default=FRESHMAN, max_length=15)
    expected_graduation = models.DateField("Expected Graduation", help_text="Choose your expected graduation time")
    transfer = models.CharField("Transfer?", help_text="If you transferred from another institution, please list.",
                                max_length=100)
    gpa = models.FloatField("GPA", help_text="Please type your current GPA.")
    stem_gpa = models.FloatField("STEM GPA", help_text="Please enter your current STEM (Science, Technology, Engineerin"
                                                       "g, Math) GPA")
    major = models.CharField("Major", help_text="Please enter your major", max_length=100)
    program = models.CharField("Program Applied To", help_text="What program are you applying to?",
                               choices=PROGRAM_CHOICES, default=PROGRAM_1, max_length=20)
    available_start = models.DateField("Available Start Date", help_text="Choose what date you are available to start")
    available_end = models.DateField("Available End Date", help_text="Choose the last date you are available")
    relevant_coursework = models.CharField("Relevant Coursework", help_text="Course work relevant to program",
                                           max_length=400, null=True)

    ###### End College Info ####

    ###### Misc Info ########
    learned_of = models.CharField("Learned of Program", help_text="How did you learn about this program?",
                                  choices=LEARNED_ABOUT_CHOICES, default=OTHER, max_length=15)
    previous_program = models.BooleanField("Previous Program?",
                                           help_text="Have you participated previously in a summer undergraduate research program at another institution?")
    previous_program_other = models.CharField("Previous Program Other",
                                              help_text="If so, list name of the Program and Institution",
                                              max_length=200)
    marc_current = models.BooleanField("MARC?", help_text="Are you currently a MARC Scholar?")
    marc_past = models.BooleanField("MARC (past)?", help_text="Did you used to be a MARC Scholar?")
    research_career = models.CharField("Research Career?", help_text="Do you want to pursue a career in research?",
                                       choices=RESEARCH_LIFE_CHOICES, default=UNSURE, max_length=6)
    gre_mcat = models.CharField("GRE/MCAT",
                                help_text="Do you plan to take the GRE, MCAT or other graduate/professional school admissions standardized exam?",
                                choices=EXAM_CHOICES, default=NO, max_length=6)
    date_of_test = models.DateField("GRE/MCAT Date", help_text="When did you take the GRE/MCAT (if applicable)?",
                                    null=True)

    ########### Degree section of application model ##############
    advanced_degree = models.CharField("Advanced Degree", max_length=50,
                                       choices=ADVANCED_DEGREE_CHOICES, default=OTHER_DEGREE)
    advanced_degree_other = models.CharField("Other Advanced Degree", help_text="If 'Other', please specify",
                                             max_length=20)
    ########## End Degree Section ###################################

    ###### End Misc Info ####

    ############## End Basic Info ###########################

    ########Contact Info ########################################
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField("Applicant Phone Number", validators=[phone_regex], blank=True,
                                    max_length=15)  # validators should be a list
    cell_phone_number = models.CharField("Applicant Cell Phone Number", validators=[phone_regex], blank=True,
                                         max_length=15)  # validators should be a list
    applicant_email = models.EmailField("Applicant Email", help_text="Enter your email address")
    street = models.CharField("Street", help_text="Enter street name", max_length=200, null=True)
    city = models.CharField("City", help_text="Enter your city's name", max_length=200, null=True)
    state = models.CharField("State", help_text="Enter your state", max_length=200, null=True)
    zipcode = models.CharField("Zip Code", help_text="Enter ZIP Code", max_length=200, null=True)
    perm_street = models.CharField(" Permanent Street", help_text="Enter permanent street name", max_length=200,
                                   null=True)
    perm_city = models.CharField("Permanent City", help_text="Enter your permanent city's name", max_length=200,
                                 null=True)
    perm_state = models.CharField("Permanent State", help_text="Enter your permanent state of residence",
                                  max_length=200, null=True)
    perm_zipcode = models.CharField("Permanent Zip Code", help_text="Enter Permanent ZIP Code", max_length=200,
                                    null=True)

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
    first_choice = models.CharField("1st Choice", help_text="Write your first choice for this program.",
                                    choices=SCIENCE_CHOICE, default=CHOICE_1, max_length=50)
    first_choice_importance = models.CharField("1st Importance", help_text="How important is this choice?",
                                               choices=IMPORTANCE_CHOICES, default=MEDIUM, max_length=12)
    second_choice = models.CharField("2nd Choice", help_text="Write your second choice for this program.",
                                     choices=SCIENCE_CHOICE, default=CHOICE_1, max_length=50)
    second_choice_importance = models.CharField("2nd Importance", help_text="How important is this choice?",
                                                choices=IMPORTANCE_CHOICES, default=MEDIUM, max_length=12)
    third_choice = models.CharField("3rd Choice", help_text="Write your third choice for this program.",
                                    choices=SCIENCE_CHOICE, default=CHOICE_1, max_length=50)
    third_choice_importance = models.CharField("3rd Importance", help_text="How important is this choice?",
                                               choices=IMPORTANCE_CHOICES, default=MEDIUM, max_length=12)
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
    ########## End Question Fields and preferences ############################################

    ######### Administrative fields ###########################################################
    mentors = models.ManyToManyField(Mentor, verbose_name="Possible Mentors", symmetrical=False)
    possible_pis = models.ManyToManyField(Faculty, verbose_name="Possible PIs", symmetrical=False)
    triage = models.CharField("Triage", max_length=10)  # TODO Figure out what this is supposed to do
    ranking = models.CharField("Ranking", help_text="What is the ranking of this applicant?", max_length=20)
    likely_institute = models.CharField("Likely Institute",
                                        help_text="What institute would this applicant be a part of?", max_length=80)
    decision_action = models.CharField("Decision", help_text="Final decision on applicant", choices=DECISION_CHOICES,
                                       null=True, max_length=10)
    comments = models.TextField("Admin Comments", help_text="Comments on Applicant")
    application_completeness = models.TextField("Application Completeness", help_text="Anything missing?")
    correspondence = models.TextField("Correspondence", help_text="Correspondence", null=True)
    year_created = models.DateField("Created Year", help_text="Year Created", default=now)
    short_list = models.CharField("Short List?", choices=SHORT_LIST_CHOICES, default=UNSURE, max_length=10)
    transcript = models.FileField('Transcript', upload_to='transcripts', null=True)
    uuid = models.TextField("UUID", default=uuid.uuid4(), null=False)
    #########End Administrative fields ###########################################################

    def __str__(self):
        return self.applicant_name

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Applicant._meta.fields]


class Intern(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    name = models.CharField("Applicant Full Name", help_text="Enter your full name", max_length=200, null=True)
    application = models.OneToOneField(Applicant, verbose_name="Intern Application")  # Deleted if Applicant is deleted
    program = models.CharField("Program", help_text="Program the intern is participating in.", max_length=40)
    arrival_date = models.DateField("Arrives", help_text="Date of arrival", null=True)
    departure_date = models.DateField("Departs", help_text="Date of departure", null=True)
    professor = models.ForeignKey(Faculty, verbose_name="Professor", on_delete=models.SET_NULL, null=True)
    mentors = models.ManyToManyField(Mentor, verbose_name="Mentors")
    institute = models.ForeignKey(Institute, verbose_name="Institute", on_delete=models.SET_NULL, null=True)
    symposium_session = models.CharField("Sympo. Session", help_text="Symposium Session", max_length=100, null=True)
    picture = models.ImageField(upload_to='interns', null=True)
    student_id = models.CharField("Student ID", help_text="Student ID number", max_length=11)
    abstract = models.OneToOneField(Abstract, verbose_name="Abstract", null=True, on_delete=models.SET_NULL)
    presentation_oral = models.URLField("Oral Presentation URL", help_text="URL to oral presentation", null=True)
    presentation_poster = models.URLField("Poster Presentation URL", help_text="URL to poster presentation", null=True)

    def __str__(self):
        return self.name


class ReferenceLetter(models.Model):
    name = models.CharField("Name", max_length=150)
    email = models.EmailField("Email")
    institution = models.CharField("Institution", max_length=150)
    department = models.CharField("Department", max_length=150)
    status = models.CharField("Status", help_text="Status of Letter of Rec", choices=LETTER_CHOICES,
                              default=WAITING_LETTER, max_length=10)
    letter = models.FileField("Letter of Rec", help_text="Recommendation Letter", upload_to="references")
    comments = models.TextField("Comments", help_text="Any comments on Letter of Recommendation?", null=True)
    applicant = models.ForeignKey(Applicant, verbose_name="Letter of Reference",
                                  help_text="Which Applicant is this letter for?")  # Deleted if Applicant is deleted

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.id:
            # So if the model already exists...
            old_letter = ReferenceLetter.objects.get(pk=self.id)
            if old_letter.status == WAITING_LETTER and self.status == REQUESTED_LETTER:
                send_mail('Reference Letter Request', 'Here is the message.', EMAIL_HOST_USER,
                          [self.email], fail_silently=False)
        else:
            send_mail('Reference Letter Request', 'Here is the message.', EMAIL_HOST_USER,
                      [self.email], fail_silently=False)
            self.status = REQUESTED_LETTER
        super(ReferenceLetter, self).save()

    def __str__(self):
        return self.applicant.applicant_name + " Letter"


class ProgressReport(models.Model):
    last_updated = models.DateField("Last Updated", help_text="Last modified timestamp", auto_now=True)
    content = models.TextField("Progress Report", help_text="Enter your progress report")
    week = models.PositiveSmallIntegerField("Week", help_text="Which week is this progress report for?")
    intern = models.ForeignKey(Intern, verbose_name="Intern")  # Deleted if Intern is deleted


class PISurvey(models.Model):
    evaluator = models.CharField("Evaluator Name", help_text="Evaluator's name", max_length=50)
    intern = models.CharField("Intern Name", help_text="Intern's name", max_length=50)
    submission_date = models.DateField("Date of Submission", help_text="Submission Date")
    comments = models.TextField("Other Comments", help_text="Enter any comments here", null=True)
    # TODO Rest of the survey, including Intern, Mentor, and Program fields


class InternSurvey(models.Model):
    evaluator = models.CharField("Evaluator Name", help_text="Evaluator's name", max_length=50)
    submission_date = models.DateField("Date of Submission", help_text="Submission Date")
    comments = models.TextField("Other Comments", help_text="Enter any comments here", null=True)
    # TODO Rest of the survey, including Overall experience, Lab Support, Porgram Support, Recreation and Living, Other


class MentorSurvey(models.Model):
    evaluator = models.CharField("Evaluator Name", help_text="Evaluator's name", max_length=50)
    intern = models.CharField("Intern Name", help_text="Intern's name", max_length=50)
    submission_date = models.DateField("Date of Submission", help_text="Submission Date")
    comments = models.TextField("Other Comments", help_text="Enter any comments here", null=True)
    # TODO Rest of the survey, including Overall Experience, Mentoring, Intern, PI Support, and Program


class IroSetup(models.Model):
    program_name = models.CharField("Program Name", help_text="Enter the name of the program", max_length=50)
    acronym = models.CharField("Program Acronym", help_text="Enter the acronym of the program, if any", max_length=20,
                               null=True)
    base_url = models.URLField("URL of site", help_text="Enter the main URL of the program (e.x. spur.uoregon.edu)")
    university_name = models.CharField("Name of University", max_length=100, null=True)
    program_email = models.EmailField("Program Email", null=True)
    program_director = models.CharField("Program Director", max_length=200, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    program_phone_number = models.CharField("Program Phone Number", validators=[phone_regex], blank=True, max_length=15)
    program_fax_number = models.CharField("Program Fax Number (Optional)", validators=[phone_regex], blank=True,
                                          max_length=15)
    logo = models.FileField("Program Logo", upload_to="logo", null=True)

    def clean(self):
        validate_only_one_instance(self)

    def __str__(self):
        return self.program_name

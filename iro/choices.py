__author__ = 'jacob'
'''
This file contains all the choices for use within the IRO app, especially for the models
'''

OTHER = "Other"
DECLINE = "Decline Response"
NO = "No"
YES = "Yes"
MULTIPLE = "Multiple"

## Sex Choices ###
MALE = "Male"
FEMALE = "Female"

SEX_CHOICES = (
    (MALE, MALE),
    (FEMALE, FEMALE),
    (DECLINE, DECLINE)
)

### Ethnic Background/ Race  ####
AFRICAN = "African American"
ALASKAN = "Alaska Native"
ASIAN = "Asian"
HISPANIC = "Hispanic"
NATIVE = "Native American"
ISLANDER = "Pacific Islander"
WHITE = "White"
MULTIRACIAL = "Multiracial"

ETHNIC_CHOICES = (
    (AFRICAN, AFRICAN),
    (ALASKAN, ALASKAN),
    (ASIAN, ASIAN),
    (HISPANIC, HISPANIC),
    (NATIVE, NATIVE),
    (ISLANDER, ISLANDER),
    (WHITE, WHITE),
    (MULTIRACIAL, MULTIRACIAL),
    (OTHER, OTHER),
    (DECLINE, DECLINE)
)


#### Disadvantaged #####

FIRST = "First Generation College"
INCOME = "Low Income"

DISADVANTAGED_CHOICES = (
    (NO, NO),
    (FIRST, FIRST),
    (INCOME, INCOME),
    (OTHER, OTHER),
    (MULTIPLE, MULTIPLE)
)

##### Learned About Program Choices ######

INTERNET = "Internet"
ABRCMS = "ABRCMS"
SACNAS = "SACNAS"
AISES = "AISES"
ADVISOR = "College Advisor"
MAILING = "Mailing"
POSTER = "Poster"

LEARNED_ABOUT_CHOICES = (
    (INTERNET, INTERNET),
    (ABRCMS, ABRCMS),
    (SACNAS, SACNAS),
    (AISES, AISES),
    (ADVISOR, ADVISOR),
    (MAILING, MAILING),
    (POSTER, POSTER),
    (OTHER, OTHER)
)

###### Research Career Choices #######

UNSURE = "Unsure"

RESEARCH_LIFE_CHOICES = (
    (YES, YES),
    (NO, NO),
    (UNSURE, UNSURE)
)

####### Exam Choices ########

GRE = "GRE"
MCAT = "MCAT"
LSAT = "LSAT"
GMAT = "GMAT"
DAT = "DAT"
VCAT = "VCAT"

EXAM_CHOICES = (
    (NO, NO),
    (GRE, GRE),
    (MCAT, MCAT),
    (LSAT, LSAT),
    (GMAT, GMAT),
    (DAT, DAT),
    (VCAT, VCAT),
    (OTHER, OTHER),
    (UNSURE, UNSURE)
)

######## Degree Choices #########

MD = 'MD'
POSSIBLE_PHD = 'Possibly PhD'
PHD_MD = 'PhD and MD'
MASTERS = 'Masters'
PHD = 'PhD'
OTHER_DEGREE = "Other Professional Degree, e.g. DDS, DVM"
ADVANCED_DEGREE_CHOICES = (
    (NO, NO),
    (UNSURE, UNSURE),
    (MASTERS, MASTERS),
    (MD, MD),
    (PHD_MD, PHD_MD),
    (PHD, PHD),
    (OTHER_DEGREE, OTHER_DEGREE)
)

######### Importance Choices ##########

HIGH = "High"
MEDIUM = "Medium"
LOW = "Low"

IMPORTANCE_CHOICES = (
    (HIGH, HIGH),
    (MEDIUM, MEDIUM),
    (LOW, LOW)
)

########## Science Choices ##########

CHOICE_1 = "Choice 1"
CHOICE_2 = "Choice 2"
CHOICE_3 = "Choice 3"
CHOICE_4 = "Choice 4"
CHOICE_5 = "Choice 5"
CHOICE_6 = "Choice 6"
CHOICE_7 = "Choice 7"

SCIENCE_CHOICE = (
    (CHOICE_1, CHOICE_1),
    (CHOICE_2, CHOICE_2),
    (CHOICE_3, CHOICE_3),
    (CHOICE_4, CHOICE_4),
    (CHOICE_5, CHOICE_5),
    (CHOICE_6, CHOICE_6),
    (CHOICE_7, CHOICE_7)
)

########### Decision Choice ############

DECISION_CHOICES = (
    (YES, YES),
    (UNSURE, UNSURE),
    (NO, NO)
)

############ Program Choices ############

PROGRAM_1 = "Program 1"
PROGRAM_2 = "Program 2"
PROGRAM_3 = "Program 3"
PROGRAM_4 = "Program 4"
PROGRAM_5 = "Program 5"

PROGRAM_CHOICES = (
    (PROGRAM_1, PROGRAM_1),
    (PROGRAM_2, PROGRAM_2),
    (PROGRAM_3, PROGRAM_3),
    (PROGRAM_4, PROGRAM_4),
    (PROGRAM_5, PROGRAM_5)
)

############# Rec Letter Choices ##############
REQUESTED_LETTER = "Requested"
LETTER_UPLOADED = "Uploaded"
WAITING_LETTER = "Waiting"

LETTER_CHOICES = (
    (REQUESTED_LETTER, REQUESTED_LETTER),
    (LETTER_UPLOADED, LETTER_UPLOADED),
    (WAITING_LETTER, WAITING_LETTER)
)
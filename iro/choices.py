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
    (MALE, "Male"),
    (FEMALE, "Female")
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
    (AFRICAN, "African American"),
    (ALASKAN, "Alaska Native"),
    (ASIAN, "Asian"),
    (HISPANIC, "Hispanic"),
    (NATIVE, "Native American"),
    (ISLANDER, "Pacific Islander"),
    (WHITE, "White"),
    (MULTIRACIAL, "Multiracial"),
    (OTHER, "Other"),
    (DECLINE, "Decline Response")
)


#### Disadvantaged #####

FIRST = "First Generation College"
INCOME = "Low Income"

DISADVANTAGED_CHOICES = (
    (NO, "No"),
    (FIRST, "First Generation College"),
    (INCOME, "Low Income"),
    (OTHER, "Other"),
    (MULTIPLE, "Multiple")
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

)
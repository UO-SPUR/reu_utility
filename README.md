# REU Utility
A utility to make REU (Research Experiences For Undergraduates) administration easier.

Built on Django, this implementation of the original REU utility, located here: https://github.com/sarahyablok/reu-utility, uses only open-source and free software
by default. 

# TODO
Forms, setup page, some encryption(i.e. SSN)

# Authentication
Authentication, when implemented, will work like this: 
    - Applicants apply, and if accepted, sign up for an account allowing them access to progress reports, intern-specific things
    - Faculty will also be able to create accounts, again giving them access to faculty-specific things
    - Mentors are the same
    - Program administrators will also be able to make generic Intern, Faculty, Mentor accounts which can function similar 
    to the University of Oregon's REU administration, where only a passowrd is needed to sign in for each the Intern, 
    Faculty, Mentor pages
    - Program administrators are superusers
# REU Utility
A utility to make REU (Research Experiences For Undergraduates) administration easier.

Built on Django, this implementation of the original REU utility, located here: https://github.com/sarahyablok/reu-utility, uses only open-source and free software
by default. 

# Purpose
The purpose of this project is to create an open-source, simple way to manage REU programs, reducing the time needed for administration of said programs and allowing administrators, faculty, menotrs, and interns to spend more time on the research and other aspects of an REU program, instead of the paperwork side of things.

# Installation
## Simplest
The simplest way to install this program is to make sure that Python 3 is installed, and download this project. Once the project is downloaded follow the steps below:
1. go into the folder containing the downloaded program
2. open up a Terminal or Command Prompt windows
3. type ```pip install -r requirements.txt``` to install Django and other required components
4. Once Python is finished installing the dependencies, run ```python3 manage.py migrate``` to create the database
5. To start the basic server, run ```python3 manage.py runserver```

## Docker
### In the process of being implemented
If you are familiar with Docker, it might be easier to deploy the application using the Dockerfile.
 
## Vagrant
### In the process of being implemented
If you want the program to run on its own virtual machine, Vagrant is a great option and can get this program up and running very easily.

# Authentication
Authentication works like this: 
    - Applicants apply, and if accepted, sign up for an account allowing them access to progress reports, intern-specific things
    - Faculty will also be able to create accounts, again giving them access to faculty-specific things
    - Mentors are the same
    - Program administrators are superusers
    - Uses [Django-registration-redux](https://github.com/macropin/django-registration) for account creation and authenitication

# Customizing The Program
## Email settings
- Sign in as a superuser (e.g. program administrator) into the admin console
- Find and click on Configuration
- Change the entry named Backend to the appropriate values
## Authentication Schemes
## Fields
## Questions, Survey, Application
## Colors, styling, etc

# TODO
PDF Generation, Correct email templates, CSS styling

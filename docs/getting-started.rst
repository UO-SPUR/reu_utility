Getting Started
===============

.. _installation:
Installation
------------

There are multiple options to install and set up the IRO utility, including cloning the repo, using Vagrant or Docker,
as well as using ``pip`` to install it.

1. Easiest Method: ``pip``
++++++++++++++++++++++++++
    1. Open up a terminal (on Linux or OSX), or Command Prompt (On Windows)
    2. Run ``pip install django-iro`` to install the utility and associated dependencies
2. Cloning the Repository
+++++++++++++++++++++++++
    1. Open up a terminal (on Linux or OSX), or Command Prompt (On Windows)
    2. Run ``git clone git://github.com/UO-SPUR/iro`` to clone the repository to the current machine
    3. Type ``cd iro`` to change directory to the IRO utility
    4. Run ``pip install -r requirements.txt`` to install the dependencies
3. Using Docker
+++++++++++++++
    If you have Docker installed, you can use the included Dockerfile to build the utility
    1. Download fromm GitHub the Dockerfile
4. Using Vagrant
++++++++++++++++
    If Vagrant is more your thing, the included Vagrant files can be used to run the utility in a virtual machine
    1. Download the Vagrant file from GitHub
    2. Open up a terminal (on Linux or OSX), or Command Prompt (On Windows) in the directory where the vagrant file was downloaded
    3. Run ``vagrant up`` to build the virtual machine

.. _initial-setup:
Initial Setup
-------------

After IRO is installed, follow the steps below to setup the database and get a working utility (Ignore if using Docker or Vagrant):

1. Go to the directory where
2. Open up a terminal (on Linux or OSX), or Command Prompt (On Windows)
3. Run ``python3 manage.py migrate`` to create the database
4. To start the basic server then, run ``python3 manage.py runserver``
5. To create a superuser, which gives access to the administration panel, run ``python3 manage.py createsuperuser`` and follow the prompts onscreen
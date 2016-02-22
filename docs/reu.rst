.. _prepare-for-reu:

Preparing for REU:
------------------

A few steps have to be completed before the utility is ready for prime time. They include adding institutions, changing
some choices for the application, and adding Faculty and Mentors, among others.

.. _add-institute:

Adding an Institute
-------------------

A lab, institute, research group, or other organization which a participating faculty member is a part of are all called
Institutes in the IRO program. To add one to the utility, follow the steps below.

#. Login as an administrator to the admin panel (if a superuser has not been created, follow these steps :ref:`initial-setup`.
#. Click on the Institutes section.
#. Click on 'Add Institute'
#. Fill out all parts of the form
#. Click 'Save' to save the Institute to the database


.. _add-faculty:

Adding a Faculty
----------------

To add a researcher, PI, faculty member, or whomever is going to be a PI for an intern, a Faculty user has to be created.

#. Once the relevant Institutes are created, direct the faculty members to the URL '<your university>/accounts/register/faculty'
#. Have the Faculty member fill out the form and submit it.
#. Make sure the Faculty member activates their account by clicking on a link sent to them in an activation email.
#. Congratulations! The Faculty member is now part of the utility! They should be visible under the 'Facultys' section of the
administration console.

.. _add-mentor:

Adding a Mentor
---------------

To add a mentor, a Mentor user has to be created. This follows very similar steps to :ref:`add-faculty`.

#. Once the relevant Faculty are created, direct the mentors to the URL '<your university>/accounts/register/mentors'
#. Have the Mentor fill out the form and submit it.
#. Make sure the Mentor activates their account by clicking on a link sent to them in an activation email.
#. Congratulations! The Mentor is now part of the utility and Interns can be assigned to them. They should be visible under
the 'Mentors' section of the administration console.

.. _add-intern:

Adding an Intern
----------------

To add an intern to the utility:

#. Make sure the Intern has submitted an application.
#. In the administration console, navigate to the 'Applications' section.
#. Choose the Application corresponding to the new Intern.
#. On the Application overview, change the 'Decision Action' to 'Yes'
#. An email will be sent to the Applicant's email.
#. They can follow that link to the url '<your-university>/accounts/register/interns/?uuid=<unique id for application>'
#. Once they fill out the Intern registration form, the procedure is the same as for :ref:`add-mentor` and :ref:`add-faculty`

.. _application:

Application
-----------

The Application is the basis for the whole REU system. It is what tells the utility to send the Reference Letters to,
each Application is linked to an Intern, with many of the Intern fields being auto-filled by Application data.

Here are the
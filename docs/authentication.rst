.. _authentication:
Authentication
==============

The IRO utility uses five different levels of authentication by default. There are the Admins, or superusers, with access
to every part of the utility; Faculty, who have access to Faculty pages and some Intern and Mentor information; Mentors,
who have access to Mentor pages and some Intern and Faculty information; Interns, who have access to Intern information,
and anonymous users, who only have access to the public aspects of the utility and website, such as the Application page.

.. _authentication-methods:
Methods
-------

The main way of restricting access of users to sensitive parts of the site is by seeing if the user's profile is part of
a valid group with access to the page. For example, to access to Intern Overview Page, the user must be logged in and their
profile must be a member of the group Faculty or Mentor.


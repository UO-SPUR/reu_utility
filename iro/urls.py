__author__ = 'jacob'

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^application', views.get_application, name='application'),
    url(r'^faculty-sign-up', views.get_faculty, name='faculty-sign-up'),
    url(r'^mentor-sign-up', views.get_mentor, name='mentor-sign-up'),
    url(r'^thanks', views.thanks, name='thanks'),
    url(r'intern', views.intern_view, name='intern'),
    url(r'faculty', views.faculty_view, name='faculty'),
    url(r'mentor', views.mentor_view, name='mentor'),
    url(r'intern-overview', views.intern_overview, name='intern overview'),
    url(r'faculty-overview', views.faculty_overview, name='faculty overview'),
    url(r'mentor-overview', views.mentor_overview, name='mentor overview'),
]
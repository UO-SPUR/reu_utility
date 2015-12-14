__author__ = 'jacob'

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^application', views.get_application, name='application'),
    url(r'^faculty-sign-up', views.get_faculty, name='faculty-sign-up'),
    url(r'^mentor-sign-up', views.get_mentor, name='mentor-sign-up'),
    url(r'^thanks', views.thanks, name='thanks'),
]
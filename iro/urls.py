__author__ = 'jacob'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.get_application, name='application'),
    url(r'^$', views.get_faculty, name='faculty-sign-up'),
    url(r'^$', views.get_mentor, name='mentor-sign-up')
]
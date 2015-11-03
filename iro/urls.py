__author__ = 'jacob'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.get_application, name='application'),
]
"""reu_utility URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
import iro.regbackend as regbackend

urlpatterns = [
    url(r'^iro/', include('iro.urls')),
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')), # registration-redux URLS
    url(r'^accounts/register/mentors', regbackend.MentorRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/register/faculty', regbackend.FacultyRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/register/interns', regbackend.InternRegistrationView.as_view(), name='registration_register'),
    url('^auth/', include('django.contrib.auth.urls')),
    url(r'^', TemplateView.as_view(template_name='index.html'), name='index')
]

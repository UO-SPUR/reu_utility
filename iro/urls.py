__author__ = 'jacob'

from django.conf.urls import url, include
from . import views
from iro.views import ApplicationMultiView

urlpatterns = [
    #url(r'^application/$', views.get_application, name='application'),
    url(r'^application/$', ApplicationMultiView.as_view(template_name="application-improved.html"), name='application'),
    url(r'^thanks/$', views.thanks, name='thanks'),
    url(r'reference-letter/$', views.get_reference, name='reference letter upload'),
    url(r'^faculty/$', include([
        url(r'^survey/$', views.faculty_survey, name='faculty survey'),
        url(r'^overview/$', views.faculty_overview, name='faculty overview'),
        url(r'applicant-pdf/$', views.application_view_html, name='applicant-PDFs'),
        url(r'^$', views.faculty_view, name='faculty'),
    ])),
    url(r'^mentor/$', include([
        url(r'^survey/$', views.mentor_survey, name='mentor survey'),
        url(r'^overview/$', views.mentor_overview, name='mentor overview'),
        url(r'^$', views.mentor_view, name='mentor'),
    ])),
    url(r'^intern/$', include([
        url(r'^progress-report/$', views.progress_report_add, name='intern progress report'),
        url(r'^abstract/$', views.intern_abstract_edit, name='intern abstract'),
        url(r'^survey/$', views.intern_survey, name='intern survey'),
        url(r'^overview/$', views.intern_overview, name='intern overview'),
        url(r'^$', views.intern_view, name='intern'),
    ]))
]
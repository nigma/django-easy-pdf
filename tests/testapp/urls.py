# coding=utf-8

from __future__ import absolute_import, division, print_function, unicode_literals

from django.conf.urls import url

from easy_pdf.views import PDFTemplateView
from .views import DemoPDFView

urlpatterns = [
    url(r'^demo/$', DemoPDFView.as_view()),
    url(r'^simple/$', PDFTemplateView.as_view(template_name='simple.html')),
]

#-*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

from django.conf.urls import patterns, url

from easy_pdf.views import PDFTemplateView

urlpatterns = patterns("",
    url(r"^simple/", PDFTemplateView.as_view(template_name="simple.html")),
)

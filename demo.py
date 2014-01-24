#!/bin/env python
#-*- coding: utf-8 -*-

"""
Demo script. Run:

python.exe demo.py
"""

from __future__ import absolute_import, division, print_function, unicode_literals

import os
import logging

logging.basicConfig()

from django.conf import settings
from django.conf.urls import patterns, url
from django.core.wsgi import get_wsgi_application
from django.utils.timezone import now as tznow

basename = os.path.splitext(os.path.basename(__file__))[0]


def rel(*path):
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), *path)
    ).replace("\\", "/")


if not settings.configured:
    settings.configure(
        DEBUG=True,
        TIMEZONE="UTC",
        INSTALLED_APPS=["easy_pdf"],
        TEMPLATE_DIRS=[rel("tests", "templates")],
        STATIC_ROOT=os.path.abspath(rel("tests", "static")),
        ROOT_URLCONF=basename,
        WSGI_APPLICATION="{}.application".format(basename),
    )

from easy_pdf.views import PDFTemplateView


class HelloPDFView(PDFTemplateView):
    template_name = "hello.html"

    def get_context_data(self, **kwargs):
        return super(HelloPDFView, self).get_context_data(
            pagesize="A4",
            title="Hi there!",
            today=tznow(),
            **kwargs
        )

urlpatterns = patterns("",
    url(r"^$", HelloPDFView.as_view())
)

application = get_wsgi_application()


if __name__ == "__main__":
    from django.core.management import call_command
    call_command("runserver", "8000")

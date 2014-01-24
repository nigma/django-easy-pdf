#-*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

from django.conf import settings
from django.test.testcases import TestCase
from django.test.client import RequestFactory, Client


class EasyPDFTestCase(TestCase):

    def test_pdf_rendering(self):
        response = self.client.get("/simple/")
        content = response.content
        self.assertEqual(content[:4], "%PDF")

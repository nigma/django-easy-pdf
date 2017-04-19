# coding=utf-8

from __future__ import absolute_import, division, print_function, unicode_literals

from django.contrib.auth import get_user_model
from django.test.testcases import TestCase


class EasyPDFViewTestCase(TestCase):
    def test_simple_pdf_rendering(self):
        response = self.client.get('/simple/')
        content = response.content
        self.assertEqual(content[:4], b'%PDF')

    def test_invoice_pdf_rendering(self):
        response = self.client.get('/demo/')
        content = response.content
        self.assertEqual(content[:4], b'%PDF')


class PDFDetailViewTestCase(TestCase):
    def setUp(self):
        super(PDFDetailViewTestCase, self).setUp()
        model = get_user_model()
        self.obj = model.objects.create(username='joe', first_name='Joe', last_name='Cool')

    def test_pdf_rendering(self):
        response = self.client.get('/user/{}/'.format(self.obj.pk))
        content = response.content
        self.assertEqual(content[:4], b'%PDF')

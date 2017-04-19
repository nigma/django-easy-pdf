# coding=utf-8

from django.contrib.auth import get_user_model
from django.test.testcases import TestCase
from django.utils.timezone import now
from django.conf import settings

from easy_pdf.rendering import render_to_content_file


class EasyPDFViewTestCase(TestCase):
    def test_simple_pdf_rendering(self):
        response = self.client.get('/simple/')
        content = response.content
        self.assertEqual(content[:4], b'%PDF')

    def test_invoice_pdf_rendering(self):
        response = self.client.get('/demo/')
        content = response.content
        self.assertEqual(content[:4], b'%PDF')


class EasyPDFDetailViewTestCase(TestCase):
    def setUp(self):
        super(EasyPDFDetailViewTestCase, self).setUp()
        model = get_user_model()
        self.obj = model.objects.create(username='joe', first_name='Joe', last_name='Cool')

    def test_pdf_rendering(self):
        response = self.client.get('/user/{}/'.format(self.obj.pk))
        content = response.content
        self.assertEqual(content[:4], b'%PDF')


class ContentFileTestCase(TestCase):
    def test_simple_pdf_rendering(self):
        context = {'today': now(), 'title': 'hello'}
        base_url = 'file://{}/'.format(settings.STATIC_ROOT)
        content = render_to_content_file('hello.html', context, base_url=base_url)
        self.assertEqual(content.read(4), b'%PDF')

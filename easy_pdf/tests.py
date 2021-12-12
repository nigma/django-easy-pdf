from django.test import RequestFactory
from django.test.testcases import TestCase

from .rendering import html_to_pdf, render_to_pdf, render_to_pdf_response
from .views import PDFTemplateView


class EasyPDFBasicTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.template_name = 'easy_pdf/base.html'

    def test_pdf_rendering(self):
        content = html_to_pdf('<html><body><div>hello</div></body></html>')
        self.assertEqual(content[:4], b'%PDF')

    def test_template_rendering(self):
        content = render_to_pdf(self.template_name, {'greeting': 'hello'})
        self.assertEqual(content[:4], b'%PDF')

    def test_response_rendering(self):
        request = self.factory.get('/sample/')
        response = render_to_pdf_response(request, self.template_name, {'greeting': 'hello'})
        self.assertEqual(response.content[:4], b'%PDF')

    def test_view_rendering(self):
        request = self.factory.get('/sample/')
        view = PDFTemplateView.as_view(template_name=self.template_name)
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content[:4], b'%PDF')

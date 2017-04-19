# coding=utf-8

from django.utils.timezone import now

from easy_pdf.views import PDFTemplateView


class DemoPDFView(PDFTemplateView):
    template_name = 'hello.html'

    pdf_filename = 'hello.pdf'

    def get_context_data(self, **kwargs):
        return super(DemoPDFView, self).get_context_data(
            pagesize='A4',
            title='Hi there!',
            today=now(),
            **kwargs
        )

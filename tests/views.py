# coding=utf-8

from django.contrib.auth import get_user_model
from django.utils.timezone import now
from django.views.generic import DetailView

from easy_pdf.views import PDFTemplateResponseMixin, PDFTemplateView


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


class PDFUserDetailView(PDFTemplateResponseMixin, DetailView):
    model = get_user_model()
    template_name = 'user_detail.html'

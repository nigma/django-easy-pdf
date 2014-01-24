#-*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

import copy

from django.views.generic.base import TemplateResponseMixin, ContextMixin, View

from .rendering import render_to_pdf_response


class PDFTemplateResponseMixin(TemplateResponseMixin):
    """
    A mixin class that implements PDF rendering and Django response construction.
    """

    #: Optional name of the PDF file for download. Leave blank for display in browser.
    pdf_filename = None

    #: Additional params passed to :func:`render_to_pdf_response`
    pdf_kwargs = None

    def get_pdf_filename(self):
        """
        Returns :attr:`pdf_filename` value by default.

        If left blank the browser will display the PDF inline.
        Otherwise it will pop up the "Save as.." dialog.

        :rtype: :func:`str`
        """
        return self.pdf_filename

    def get_pdf_kwargs(self):
        """
        Returns :attr:`pdf_kwargs` by default.

        The kwargs are passed to :func:`render_to_pdf_response` and
        :func:`xhtml2pdf.pisa.pisaDocument`.

        :rtype: :class:`dict`
        """
        if self.pdf_kwargs is None:
            return {}
        return copy.copy(self.pdf_kwargs)

    def get_pdf_response(self, context, **response_kwargs):
        """
        Renders PDF document and prepares response.

        :returns: Django HTTP response
        :rtype: :class:`django.http.HttpResponse`
        """
        return render_to_pdf_response(
            request=self.request,
            template=self.get_template_names(),
            context=context,
            filename=self.get_pdf_filename(),
            **self.get_pdf_kwargs()
        )

    def render_to_response(self, context, **response_kwargs):
        return self.get_pdf_response(context, **response_kwargs)


class PDFTemplateView(PDFTemplateResponseMixin, ContextMixin, View):
    """
    Concrete view for serving PDF files.

    .. code-block:: python

        class HelloPDFView(PDFTemplateView):
            template_name = "hello.html"
    """

    def get(self, request, *args, **kwargs):
        """
        Handles GET request and returns HTTP response.
        """
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

# coding=utf-8

from __future__ import absolute_import, division, print_function, unicode_literals

try:
    # noinspection PyUnresolvedReferences
    from typing import Any, Dict, Optional, Text, Type
except ImportError:
    pass

from django.http import HttpResponse, HttpRequest
from django.views.generic.base import ContextMixin, TemplateResponseMixin, View

from .rendering import render_to_pdf_response, CONTENT_TYPE


class PDFTemplateResponseMixin(TemplateResponseMixin):
    """
    A mixin class that implements PDF rendering and Django response construction.
    """

    #: Optional name of the PDF file for download. Leave blank for display in browser.
    download_filename = None  # type: Optional[Text]

    #: Base URL for referencing relative images, fonts and stylesheet resources.
    base_url = None  # type: Optional[Text]

    #: Response class. Defaults to :class:`django.http.HttpResponse`.
    response_class = HttpResponse  # type: Type[HttpResponse]

    #: Response content type. Default is ``'application/pdf'``.
    content_type = CONTENT_TYPE  # type: Text

    def get_download_filename(self):  # type: () -> Optional[Text]
        """
        Returns :attr:`download_filename` value by default.

        If left blank the browser will display the PDF inline.
        Otherwise it will pop up the "Save as.." dialog.

        :rtype: :class:`str` or None
        """
        return self.download_filename

    def get_base_url(self):  # type: () -> Optional[Text]
        """
        Returns :attr:`base_url` value by default.

        :rtype: :class:`str` or None
        """
        return self.base_url

    def get_render_kwargs(self):  # type: () -> Dict[Text, Any]
        """
        The render kwargs are passed to :func:`~easy_pdf.rendering.html_to_pdf`.

        """
        return {
            'download_filename': self.get_download_filename(),
            'base_url': self.get_base_url()
        }

    def get_pdf_response(self, context):  # type: (Dict) -> HttpResponse
        """
        Renders PDF document and prepares response.

        :returns: Django HTTP response
        :rtype: :class:`django.http.HttpResponse`
        """
        return render_to_pdf_response(
            request=self.request,
            template=self.get_template_names(),
            context=context,
            using=self.template_engine,
            response_class=self.response_class,
            content_type=self.content_type,
            **self.get_render_kwargs()
        )

    def render_to_response(self, context, **response_kwargs):  # type: (Dict, Any) -> HttpResponse
        # response_kwargs.setdefault('content_type', self.content_type)
        return self.get_pdf_response(context)


class PDFTemplateView(PDFTemplateResponseMixin, ContextMixin, View):
    """
    A view that renders template to PDF document
    in a way similar to Django's :class:`~django.views.generic.base.TemplateView`

    .. code-block:: python

        class HelloPDFView(PDFTemplateView):
            template_name = "hello.html"
    """

    def get(self, request, *args, **kwargs):  # type: (HttpRequest, Any, Any) -> HttpResponse
        """
        Handles GET request and returns HTTP response.
        """
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

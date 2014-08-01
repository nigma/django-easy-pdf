#-*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

import logging
import os

from django.conf import settings
from django.template import loader, Context, RequestContext
from django.http import HttpResponse
from django.utils.http import urlquote
from django.utils.six import BytesIO

import xhtml2pdf.default
from xhtml2pdf import pisa

from .exceptions import UnsupportedMediaPathException, PDFRenderingError

logger = logging.getLogger("app.pdf")
logger_x2p = logging.getLogger("app.pdf.xhtml2pdf")


def fetch_resources(uri, rel):
    """
    Retrieves embeddable resource from given ``uri``.

    For now only local resources (images, fonts) are supported.

    :param str uri: path or url to image or font resource
    :returns: path to local resource file.
    :rtype: str
    :raises: :exc:`~easy_pdf.exceptions.UnsupportedMediaPathException`
    """
    # For protocol relative, http and https URLs, we need to short circuit to skip 
    # path checking at the end of function
    if uri.startswith('//') or uri.startswith('http://') or uri.startswith('https://'):
        return uri
    elif settings.STATIC_URL and uri.startswith(settings.STATIC_URL):
        path = os.path.join(settings.STATIC_ROOT, uri.replace(settings.STATIC_URL, ""))
    elif settings.MEDIA_URL and uri.startswith(settings.MEDIA_URL):
        path = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ""))
    else:
        path = os.path.join(settings.STATIC_ROOT, uri)

    if not os.path.isfile(path):
        raise UnsupportedMediaPathException(
            "media urls must start with {} or {}".format(
                settings.MEDIA_ROOT, settings.STATIC_ROOT
            )
        )

    return path.replace("\\", "/")


def html_to_pdf(content, encoding="utf-8",
                link_callback=fetch_resources, **kwargs):
    """
    Converts html ``content`` into PDF document.

    :param unicode content: html content
    :returns: PDF content
    :rtype: :class:`bytes`
    :raises: :exc:`~easy_pdf.exceptions.PDFRenderingError`
    """
    src = BytesIO(content.encode(encoding))
    dest = BytesIO()

    pdf = pisa.pisaDocument(src, dest, encoding=encoding,
                            link_callback=link_callback, **kwargs)
    if pdf.err:
        logger.error("Error rendering PDF document")
        for entry in pdf.log:
            if entry[0] == xhtml2pdf.default.PML_ERROR:
                logger_x2p.error("line %s, msg: %s, fragment: %s", entry[1], entry[2], entry[3])
        raise PDFRenderingError("Errors rendering PDF", content=content, log=pdf.log)

    if pdf.warn:
        for entry in pdf.log:
            if entry[0] == xhtml2pdf.default.PML_WARNING:
                logger_x2p.warning("line %s, msg: %s, fragment: %s", entry[1], entry[2], entry[3])

    return dest.getvalue()


def encode_filename(filename):
    """
    Encodes filename part for ``Content-Disposition: attachment``.

    >>> print(encode_filename("abc.pdf"))
    filename=abc.pdf
    >>> print(encode_filename("aa bb.pdf"))
    filename*=UTF-8''aa%20bb.pdf
    >>> print(encode_filename(u"zażółć.pdf"))
    filename*=UTF-8''za%C5%BC%C3%B3%C5%82%C4%87.pdf
    """
    # TODO: http://greenbytes.de/tech/webdav/rfc6266.html
    # TODO: http://greenbytes.de/tech/tc2231/

    quoted = urlquote(filename)
    if quoted == filename:
        return "filename=%s" % filename
    else:
        return "filename*=UTF-8''%s" % quoted


def make_response(content, filename=None, content_type="application/pdf"):
    """
    Wraps content into HTTP response.

    If ``filename`` is specified then ``Content-Disposition: attachment``
    header is added to the response.

    Default ``Content-Type`` is ``application/pdf``.

    :param bytes content: response content
    :param str filename: optional filename for file download
    :param str content_type: response content type
    :rtype: :class:`django.http.HttpResponse`
    """
    response = HttpResponse(content, content_type=content_type)
    if filename is not None:
        response["Content-Disposition"] = "attachment; %s" % encode_filename(filename)
    return response


def render_to_pdf(template, context, encoding="utf-8", **kwargs):
    """
    Create PDF document from Django html template.

    :param str template: path to Django template
    :param context: template context
    :type context: :class:`dict` or :class:`django.template.Context`

    :returns: rendered PDF
    :rtype: :class:`bytes`

    :raises: :exc:`~easy_pdf.exceptions.PDFRenderingError`, :exc:`~easy_pdf.exceptions.UnsupportedMediaPathException`
    """
    if not isinstance(context, Context):
        context = Context(context)

    content = loader.render_to_string(template, context)
    return html_to_pdf(content, encoding, **kwargs)


def render_to_pdf_response(request, template, context, filename=None,
                           encoding="utf-8", **kwargs):
    """
    Renders a PDF response using given ``request``, ``template`` and ``context``.

    If ``filename`` param is specified then the response ``Content-Disposition``
    header will be set to ``attachment`` making the browser display
    a "Save as.." dialog.

    :param request: Django request
    :type request: :class:`django.http.HttpRequest`
    :param str template: path to Django template
    :param context: template context
    :type context: :class:`dict` or :class:`django.template.Context`
    :rtype: :class:`django.http.HttpResponse`
    """

    if not isinstance(context, Context):
        if request is not None:
            context = RequestContext(request, context)
        else:
            context = Context(context)

    try:
        pdf = render_to_pdf(template, context, encoding=encoding, **kwargs)
        return make_response(pdf, filename)
    except PDFRenderingError as e:
        logger.exception(e.message)
        return HttpResponse(e.message)

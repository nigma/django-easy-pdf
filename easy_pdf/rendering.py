# coding=utf-8

from __future__ import absolute_import, division, print_function, unicode_literals

from django.core.files.base import ContentFile
from django.http import HttpResponse
from django.template import Context, RequestContext, loader
from django.utils.http import urlquote
from django.utils.six import BytesIO
from weasyprint import HTML, default_url_fetcher

__all__ = [
    'html_to_pdf', 'encode_filename', 'make_response',
    'render_to_pdf', 'render_to_pdf_response', 'render_to_content_file'
]

CONTENT_TYPE = 'application/pdf'


def html_to_pdf(content, stylesheets=None, base_url=None, url_fetcher=default_url_fetcher, media_type='print'):
    """
    Converts HTML ``content`` into PDF document.

    The HTML document can contain references to image, font and style resources provided
    as absolute or relative URLs. If resources are referenced by relative URLs the
    ``base_url`` param must also be specified so the ``url_fetcher`` is able to load the files.

    Resource URLs can use either external ``http://`` or ``https://`` protocol
    or local ``file://`` protocol (for example when embedding images from ``STATIC_ROOT`` directory).

    Keep that in mind and always specify and validate URLs for linked resources in case
    of user generated content is rendered to PDF documents to avoid potential security issues.

    :param str content: HTML content to render
    :type stylesheets: list of :class:`weasyprint.CSS` or :obj:`None`
    :param stylesheets:
            Additional :class:`weasyprint.CSS` stylesheets or :obj:`None`.
            See https://weasyprint.readthedocs.io/en/latest/tutorial.html#stylesheet-origins.
    :param base_url:
            The base used to resolve relative URLs. See WeasyPrint docs.
    :param url_fetcher:
            A function or other callable with the same signature
            as :func:`weasyprint.default_url_fetcher` called to fetch external resources
            such as stylesheets and images.
            See https://weasyprint.readthedocs.io/en/latest/tutorial.html#url-fetchers.
    :param media_type:
            The media type to use for ``@media``. Defaults to ``'print'``.

    :rtype: :class:`bytes`
    :returns: PDF content
    """

    html = HTML(string=content, base_url=base_url, url_fetcher=url_fetcher, media_type=media_type)
    dest = BytesIO()
    html.write_pdf(dest, stylesheets=stylesheets)
    return dest.getvalue()


def encode_filename(filename):
    """
    Encodes filename part for ``Content-Disposition: attachment``.

    :param str filename: Filename to encode

    :rtype: str
    :returns: Encoded filename for use in ``Content-Disposition`` header

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


def make_response(content, download_filename=None, content_type=CONTENT_TYPE, response_class=HttpResponse):
    """
    Wraps file content into HTTP response.

    If ``filename`` is specified then ``Content-Disposition: attachment``
    header is added to the response.

    Default ``Content-Type`` is ``'application/pdf'``.

    :param bytes content: Response content
    :param str download_filename: Optional filename for file download
    :param str content_type: Response content type
    :param response_class: Response class to instantiate

    :rtype: :class:`django.http.HttpResponse`
    :returns: Django response
    """
    response = response_class(content, content_type=content_type)
    if download_filename is not None:
        response["Content-Disposition"] = "attachment; %s" % encode_filename(download_filename)
    return response


def render_to_pdf(template, context, using=None, **render_kwargs):
    """
    Creates PDF document from Django HTML template.

    :param str template: Path to Django template
    :param context: Template context
    :type context: :class:`dict` or :class:`django.template.Context`
    :param using: Optional Django template engine

    :rtype: :class:`bytes`
    :returns: Rendered PDF document

    Additional ``**render_kwargs`` are passed to :func:`html_to_pdf`.
    """
    if not isinstance(context, Context):
        context = Context(context)

    content = loader.render_to_string(template, context, using=using)
    return html_to_pdf(content, **render_kwargs)


def render_to_pdf_response(request, template, context, using=None,
                           download_filename=None, content_type=CONTENT_TYPE,
                           response_class=HttpResponse,
                           **render_kwargs):
    """
    Renders a PDF response using given ``request``, ``template`` and ``context``.

    If ``download_filename`` param is specified then the response ``Content-Disposition``
    header will be set to ``attachment`` making the browser display
    a "Save as.." dialog.

    :param request: Django HTTP request
    :type request: :class:`django.http.HttpRequest`
    :param str template: Path to Django template
    :param context: Template context
    :type context: :class:`dict` or :class:`django.template.Context`
    :param using: Optional Django template engine
    :param str download_filename: Optional filename to use for file download
    :param str content_type: Response content type
    :param response_class: Default is :class:`django.http.HttpResponse`

    :rtype: :class:`django.http.HttpResponse`
    :returns: Django HTTP response

    Additional ``**render_kwargs`` are passed to :func:`html_to_pdf`.
    """

    if not isinstance(context, Context):
        if request is not None:
            context = RequestContext(request, context)
        else:
            context = Context(context)

    pdf = render_to_pdf(template, context, using=using, **render_kwargs)
    return make_response(pdf, download_filename, content_type=content_type, response_class=response_class)


def render_to_content_file(template, context, using=None, **render_kwargs):
    """
    Example:

        >>> content = render_to_content_file('doc.html')

    Then save to Django storage:

        >>> from django.core.files.storage import default_storage
        >>> default_storage.save('file.pdf', content)

    Or attach to a model instance:

        >>> instance.attachment.save('file.pdf', content, save=True)

    :param str template: Path to Django template
    :param context: Template context
    :type context: :class:`dict` or :class:`django.template.Context`
    :param using: Optional Django template engine

    :rtype: :class:`django.core.files.base.ContentFile`
    :returns: Django content file

    Additional ``**render_kwargs`` are passed to :func:`html_to_pdf`.
    """
    content = render_to_pdf(template, context, using=using, **render_kwargs)
    return ContentFile(content)

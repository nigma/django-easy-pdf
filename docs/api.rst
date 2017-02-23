.. _api:

============
API Overview
============

Views
=====

.. automodule:: easy_pdf.views

PDFTemplateResponseMixin
------------------------

.. autoclass:: PDFTemplateResponseMixin
   :show-inheritance:
   :members:

PDFTemplateView
---------------

.. autoclass:: PDFTemplateView
   :show-inheritance:
   :members:


.. _rendering_functions:

PDF rendering functions
=======================

.. automodule:: easy_pdf.rendering

.. autofunction:: render_to_pdf
.. autofunction:: render_to_pdf_response(request, template, context, using=None, download_filename=None, content_type='application/pdf', response_class=HttpResponse, **render_kwargs)
.. autofunction:: render_to_content_file

Other lower-level helpers
-------------------------

.. autofunction:: html_to_pdf(content, stylesheets=None, base_url=None, url_fetcher=default_url_fetcher, media_type='print')
.. autofunction:: make_response(content, download_filename=None, content_type='application/pdf', response_class=HttpResponse)
.. autofunction:: encode_filename

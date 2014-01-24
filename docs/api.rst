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
.. autofunction:: render_to_pdf_response

Other lower-level helpers
-------------------------

.. autofunction:: html_to_pdf(content, dest, encoding="utf-8", link_callback=fetch_resources, **kwargs)
.. autofunction:: fetch_resources
.. autofunction:: make_response
.. autofunction:: encode_filename


Exceptions
==========

.. automodule:: easy_pdf.exceptions
   :members:
   :show-inheritance:

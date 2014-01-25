===============
django-easy-pdf
===============

.. image:: https://pypip.in/v/django-easy-pdf/badge.png
    :target: https://pypi.python.org/pypi/django-easy-pdf/
    :alt: Latest Version

.. image:: https://pypip.in/d/django-easy-pdf/badge.png
    :target: https://pypi.python.org/pypi/django-easy-pdf/
    :alt: Downloads

.. image:: https://pypip.in/license/django-easy-pdf/badge.png
    :target: https://pypi.python.org/pypi/django-easy-pdf/
    :alt: License

Django PDF rendering, the easy way.

Developed at `en.ig.ma software shop <http://en.ig.ma>`_.


Overview
--------

This app makes rendering PDF files in Django really easy.
It can be used to create invoices, bills and other documents
from simple HTML markup and CSS styles. You can even embed images
and use custom fonts.

The library provides both Class-Based View that is almost a drop-in
replacement for Django's ``TemplateView`` as well as helper functions
to render PDFs in the backend outside the request scope
(i.e. using Celery workers).


Quickstart
----------

1. Include ``django-easy-pdf`` and ``git+https://github.com/chrisglass/xhtml2pdf.git``
   in your ``requirements.txt`` file.

2. Add ``easy_pdf`` to ``INSTALLED_APPS``.

3. Create HTML template for PDF document and add a view that will render it:

    .. code-block:: css+django

        {% extends "easy_pdf/base.html" %}

        {% block content %}
            <div id="content">
                <h1>Hi there!</h1>
            </div>
        {% endblock %}

    .. code-block:: python

        from easy_pdf.views import PDFTemplateView

        class HelloPDFView(PDFTemplateView):
            template_name = "hello.html"


Documentation
-------------

The full documentation is at `django-easy-pdf.rtfd.org <http://django-easy-pdf.rtfd.org>`_.

A live demo is at `easy-pdf.herokuapp.com <https://easy-pdf.herokuapp.com/>`_.
You can run it locally after installing dependencies by running ``python demo.py``
script from the cloned repository.

Dependencies
------------

``django-easy-pdf`` depends on:

    - ``django>=1.5.1``
    - ``git+https://github.com/chrisglass/xhtml2pdf.git``


License
-------

``django-easy-pdf`` is released under the MIT license.


Other Resources
---------------

- GitHub repository - https://github.com/nigma/django-easy-pdf
- PyPi Package site - http://pypi.python.org/pypi/django-easy-pdf


Commercial Support
------------------

This app and many other help us build better software
and focus on delivering quality projects faster.
We would love to help you with your next project so get in touch
by dropping an email at en@ig.ma.

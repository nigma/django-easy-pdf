Django PDF rendering
====================

Django PDF rendering, the easy way.

.. image:: https://secure.travis-ci.org/nigma/django-easy-pdf.svg?branch=master
    :target: https://secure.travis-ci.org/nigma/django-easy-pdf
    :alt: Build Status
.. image:: https://img.shields.io/pypi/v/django-easy-pdf.svg
    :target: https://pypi.python.org/pypi/django-easy-pdf/
    :alt: Latest Version
.. image:: https://img.shields.io/badge/wheel-yes-green.svg
    :target: https://pypi.python.org/pypi/django-easy-pdf/
    :alt: Wheel
.. image:: https://img.shields.io/pypi/l/django-easy-pdf.svg
    :target: https://pypi.python.org/pypi/django-easy-pdf/
    :alt: License

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

1. Include ``django-easy-pdf>=0.2.0`` and ``WeasyPrint>=0.34`` in your ``requirements.txt`` file
   and install necessary system packages.

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
            template_name = 'hello.html'


Documentation
-------------

The full documentation is at `django-easy-pdf.rtfd.org <https://django-easy-pdf.rtfd.org>`_.

A live demo is at `easy-pdf.herokuapp.com <https://easy-pdf.herokuapp.com/>`_.
You can run it locally after installing dependencies by running ``python demo.py``
script from the cloned repository or through Docker with ``make demo``.


Dependencies
------------

``django-easy-pdf`` depends on:

    - ``django>=1.10``
    - ``WeasyPrint>=0.34``
    - ``WeasyPrint`` dependencies (https://weasyprint.readthedocs.io/en/latest/install.html)


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

Django PDF rendering
====================

Django PDF rendering, the easy way.

.. image:: https://circleci.com/gh/nigma/django-easy-pdf/tree/master.svg?style=svg
    :target: https://circleci.com/gh/nigma/django-easy-pdf/tree/master
    :alt: Build Status
.. image:: https://img.shields.io/pypi/v/django-easy-pdf3/
    :target: https://pypi.python.org/pypi/django-easy-pdf3/
    :alt: Latest Version
.. image:: https://img.shields.io/badge/wheel-yes-green.svg
    :target: https://pypi.python.org/pypi/django-easy-pdf3/
    :alt: Wheel
.. image:: https://img.shields.io/pypi/l/django-easy-pdf3
    :target: https://pypi.python.org/pypi/django-easy-pdf3/
    :alt: License

Developed at `en.ig.ma software shop <http://en.ig.ma>`_.

Development Version
-------------------
Note: This fork support Django>=3.0 with "xhtml2pdf" as rendering backend! Support with WeasyPrint is not tested!
Note: A new PDF rendering backend using WeasyPrint for more accurate rendering is in development under the develop branch.
See https://github.com/nigma/django-easy-pdf/pull/34 for changes, testing and discussion.

If you rely on the ``xhtml2pdf`` rendering backend and templates pin the package version to ``django-easy-pdf>=0.1.1<0.2.0``.

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

1. Include ``django-easy-pdf3``, ``xhtml2pdf`` in your ``requirements.txt`` file.
   If you are on Python 3 you need to install the latest version of Reportlab and the beta version of xhtml2pdf::

    $ pip install xhtml2pdf>=0.2b1

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

4. You can also use a mixin to output PDF from Django generic views:

    .. code-block:: python

        class PDFUserDetailView(PDFTemplateResponseMixin, DetailView):
            model = get_user_model()
            template_name = 'user_detail.html'

Documentation
-------------

The full documentation is at `django-easy-pdf.readthedocs.io <https://django-easy-pdf.readthedocs.io/>`_.

A live demo is at `easy-pdf.herokuapp.com <https://easy-pdf.herokuapp.com/>`_.
You can run it locally after installing dependencies by running ``python demo.py``
script from the cloned repository or through Docker with ``make demo``.


Dependencies
------------

``django-easy-pdf3`` depends on:

    - ``django>=2.0``
    - ``xhtml2pdf>=0.2b1``
    - ``reportlab``


License
-------

``django-easy-pdf3`` is released under the MIT license.


Other Resources
---------------

- GitHub repository - https://github.com/olksndrdevhub/django-easy-pdf3
- PyPi Package site - https://pypi.python.org/pypi/django-easy-pdf3
- Docs - https://django-easy-pdf.readthedocs.io/


Commercial Support
------------------

This app and many other help us build better software
and focus on delivering quality projects faster.
We would love to help you with your next project so get in touch
by dropping an email at en@ig.ma.

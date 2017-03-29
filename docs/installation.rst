============
Installation
============

Add ``django-easy-pdf=<version>`` and ``git+https://github.com/chrisglass/xhtml2pdf.git``
to your ``requirements.txt`` file or install it directly from the command line by invoking::

    $ pip install django-easy-pdf
    $ pip install "xhtml2pdf>=0.0.6" "reportlab>=2.7,<3"

If you are on Python 3 you need to install the latest version of Reportlab
and the beta version of xhtml2pdf::

    $ pip install --pre xhtml2pdf

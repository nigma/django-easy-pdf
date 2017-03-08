============
Installation
============

1. Add ``django-easy-pdf==0.2.0`` and ``WeasyPrint>=0.34``
   to your ``requirements.txt`` file or install it directly from the command line by invoking::

        $ pip install -U django-easy-pdf WeasyPrint

2. Install WeasyPrint system dependencies specific to your platform.

   On Debian/Ubuntu install::

      apt-get install -y --no-install-recommends gettext libcairo2 libffi-dev libpango1.0-0 \
        libgdk-pixbuf2.0-0 libxml2-dev libxslt1-dev shared-mime-info

   For install instructions on other platforms see http://weasyprint.readthedocs.io/en/latest/install.html.

   If you are using Docker to deploy your application you can consult the included `Dockerfile`.

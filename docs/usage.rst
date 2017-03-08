=====
Usage
=====

Prepare HTML Templates
----------------------

Create a Django HTML template with embedded CSS style. You can use special
style attributes to format the PDF output.

For more information on the supported HTML and CSS rules
see docs at https://weasyprint.readthedocs.io/en/latest/features.html

You can also use custom embeddable resources like images and fonts.
They can be referenced locally via the ``file://`` protocol or fetched
from web over ``http://`` or ``https://``.

.. code-block:: css+django

    {% extends "easy_pdf/base.html" %}

    {% block extra_style %}
        <style type="text/css">
            body {
                font-family: "Helvetica", "sans-serif";
                color: #333333;
            }
        </style>
    {% endblock %}

    {% block content %}
        <div id="content">
            <div class="main">
                <h1>Hi there!</h1>
                <img src="file:///STATIC_ROOT/img/hello.png" />
            </div>
        </div>
    {% endblock %}


Create PDF rendering views
--------------------------

This part is easy. The PDF rendering view inherits from
:class:`~django.views.generic.base.TemplateResponseMixin`
so it works in the same way as Django's
:class:`~django.views.generic.base.TemplateView`.
Just point it to a HTML template and define
:meth:`~django.views.generic.base.ContextMixin.get_context_data`
method to pass any extra variables to the template:

.. code-block:: python

    from django.conf import settings
    from easy_pdf.views import PDFTemplateView

    class HelloPDFView(PDFTemplateView):
        template_name = 'hello.html'

        base_url = 'file://' + settings.STATIC_ROOT
        download_filename = 'hello.pdf'

        def get_context_data(self, **kwargs):
            return super(HelloPDFView, self).get_context_data(
                pagesize='A4',
                title='Hi there!',
                **kwargs
            )

Notice the ``base_url`` attribute that can be used to specify base URL for
all files referenced in the template by relative URLs.

Then add the view to your url config and start serving PDF files
rendered from the HTML template.

.. code-block:: python

    urlpatterns = [
        url(r'^hello.pdf$', HelloPDFView.as_view())
    ]


Rendering PDF outside of Django views
-------------------------------------

See :ref:`rendering_functions`.

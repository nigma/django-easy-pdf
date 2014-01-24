=====
Usage
=====

Prepare HTML Templates
----------------------

Create a Django HTML template with embedded CSS style. You can use special
style attributes to format the PDF output.

For more information on the supported HTML and CSS rules
see docs at https://github.com/chrisglass/xhtml2pdf/blob/master/doc/usage.rst

You can also use custom embeddable resources like images and fonts.
Put them inside Django's ``STATIC_ROOT`` directory and make sure
they are available locally on the server even if you
are serving your static files from S3 or other CDN.

For now only local resources are supported.

.. code-block:: css+django

    {% extends "easy_pdf/base.html" %}

    {% block extra_style %}
        <style type="text/css">
            @font-face { font-family: Lato; src: url(fonts/Lato-Reg.ttf); }
            body {
                font-family: "Lato", "Helvetica", "sans-serif";
                color: #333333;
            }
        </style>
    {% endblock %}

    {% block content %}
        <div id="content">
            <div class="main">
                <h1>Hi there!</h1>
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

    from easy_pdf.views import PDFTemplateView

    class HelloPDFView(PDFTemplateView):
        template_name = "hello.html"

        def get_context_data(self, **kwargs):
            return super(HelloPDFView, self).get_context_data(
                pagesize="A4",
                title="Hi there!",
                **kwargs
            )


Then add the view to your url config and start serving PDF files
rendered from the HTML template.

.. code-block:: python

    urlpatterns = patterns("",
        url(r"^hello.pdf$", HelloPDFView.as_view())
    )


Rendering PDF outside Django views
----------------------------------

See :ref:`rendering_functions`.

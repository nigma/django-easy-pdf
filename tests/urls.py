# coding=utf-8

from django.urls import re_path

from easy_pdf.views import PDFTemplateView
from .views import DemoPDFView, PDFUserDetailView

urlpatterns = [
    re_path(r'^demo/$', DemoPDFView.as_view()),
    re_path(r'^simple/$', PDFTemplateView.as_view(template_name='simple.html')),
    re_path(r'^user/(?P<pk>\d+)/$', PDFUserDetailView.as_view()),
]

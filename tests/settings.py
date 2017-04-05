# coding=utf-8

from __future__ import absolute_import, division, print_function, unicode_literals

import logging
import os
import sys

logging.basicConfig(level=logging.DEBUG)

basename = os.path.splitext(os.path.basename(__file__))[0]


def rel(*path):
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), *path)
    ).replace("\\", "/")


sys.path.append(rel('..'))

DEBUG = True
SECRET_KEY = 'none'
TIMEZONE = 'UTC'
INSTALLED_APPS = ['easy_pdf', 'testapp']
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [rel('templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
            ],
        },
    },
]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
STATIC_ROOT = os.path.abspath(rel('static'))
STATIC_URL = '/static/'
ROOT_URLCONF = 'testapp.urls'

TEST_RUNNER = 'tests.runner.NoDbTestRunner'

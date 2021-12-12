import logging
import os
import sys

logging.basicConfig(level=logging.INFO)

basename = os.path.splitext(os.path.basename(__file__))[0]


def rel(*path):
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), *path)
    ).replace("\\", "/")


sys.path.append(rel('..'))

DEBUG = True
SECRET_KEY = 'none'
TIMEZONE = 'UTC'
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django_nose',
    'easy_pdf',
    'tests'
]
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
ROOT_URLCONF = 'tests.urls'

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

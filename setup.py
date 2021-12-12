#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import setuptools

version = "0.1.4"

if sys.argv[-1] == "publish":
    os.system("python setup.py sdist bdist_wheel upload")
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open("README.rst").read()
history = open("HISTORY.rst").read().replace(".. :changelog:", "")

setuptools.setup(
    name="django-easy-pdf3",
    version=version,
    description="""Django PDF views, the easy way""",
    license="MIT",
    author="Filip Wasilewski",
    author_email="en@ig.ma",
    maintainer='Romaniuk Oleksandr',
    maintainer_email='oleksandr.romaniuk@protonmail.com',
    url="https://github.com/olksndrdevhub/django-easy-pdf3",
    project_urls={
        "Bug Tracker": "https://github.com/olksndrdevhub/django-easy-pdf3/issues",
    },
    long_description=readme + "\n\n" + history,
    packages=[
        "easy_pdf",
    ],
    include_package_data=True,
    install_requires=[
        "django",
        "xhtml2pdf",
        "reportlab"
    ],
    extras_require={
        'test': (
            'django-nose',
            'coverage',
            'flake8',
            'isort',
            'mccabe',
            'pycodestyle',
            'pyflakes',
            'mypy',
            'tox',
            'twine',
        )
    },
    zip_safe=False,
    keywords="django-easy-pdf3",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
)

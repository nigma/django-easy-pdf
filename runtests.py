#-*- coding: utf-8 -*-

import os
import sys
from optparse import OptionParser

from django.conf import settings


def rel(*path):
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), *path)
    ).replace("\\", "/")


if not settings.configured or not os.environ.get("DJANGO_SETTINGS_MODULE"):
    settings.configure(
        DEBUG=True,
        USE_TZ=True,
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
            }
        },
        INSTALLED_APPS=[
            "easy_pdf"
        ],
        TEMPLATE_DIRS=[rel("tests", "templates")],
        STATIC_ROOT=os.path.abspath(rel("tests", "static")),
        ROOT_URLCONF="tests.urls",
    )

from django.test.utils import get_runner


def run_tests(verbosity, interactive, failfast, test_labels):
    if not test_labels:
        test_labels = ["tests"]

    if not hasattr(settings, "TEST_RUNNER"):
        settings.TEST_RUNNER = "django.test.runner.DiscoverRunner"
    TestRunner = get_runner(settings)

    test_runner = TestRunner(
        verbosity=verbosity,
        interactive=interactive,
        failfast=failfast
    )

    failures = test_runner.run_tests(test_labels)
    if failures:
        sys.exit(bool(failures))


if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("--failfast", action="store_true",
                      default=False, dest="failfast")
    parser.add_option("--verbosity", action="store",
                      default=1, type=int, dest="verbosity")
    (options, args) = parser.parse_args()
    run_tests(options.verbosity, options.failfast, False, args)

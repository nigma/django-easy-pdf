# coding=utf-8

from django.test.runner import DiscoverRunner as BaseRunner


class NoDbTestRunner(BaseRunner):
    """ A test runner to test without database creation """

    def setup_databases(self, **kwargs):
        """ Override the database creation defined in parent class """
        pass

    def teardown_databases(self, old_config, **kwargs):
        """ Override the database teardown defined in parent class """
        pass

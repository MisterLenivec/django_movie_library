from django.apps import apps
from django.test import TestCase

from movies.apps import MoviesConfig


class MoviesConfigTests(TestCase):
    """
    App config name test
    """
    def test_apps(self):
        """
        App config name is movies
        """
        self.assertEqual('movies', MoviesConfig.name)
        self.assertEqual('movies', apps.get_app_config('movies').name)

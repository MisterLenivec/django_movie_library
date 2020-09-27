from django.apps import apps

from movies.apps import MoviesConfig


class TestMoviesConfig:
    """
    App config name test
    """
    def test_apps(self):
        """
        App config name is movies
        """
        assert 'movies' == MoviesConfig.name, "App config name should be movies"
        assert 'movies' == apps.get_app_config('movies').name, \
            "App config name should be movies"

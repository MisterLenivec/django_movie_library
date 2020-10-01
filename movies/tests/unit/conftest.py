import pytest
import os
from django_movie_library import local_settings


@pytest.fixture(scope='session')
def django_db_setup():
    local_settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('movie_lib_db_name'),
        'USER': os.environ.get('movie_lib_db_user'),
        'PASSWORD': os.environ.get('movie_lib_db_password'),
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }

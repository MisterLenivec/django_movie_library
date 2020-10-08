import pytest
import os

from django.db import connections

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def run_sql(sql):
    conn = psycopg2.connect(
        database=os.environ.get("movie_lib_db_name"),
        user=os.environ.get('movie_lib_db_user'),
        password=os.environ.get('movie_lib_db_password'),
        host='127.0.0.1',
        port='5432',
    )
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    cur.execute(sql)
    conn.close()


@pytest.yield_fixture(scope='session')
def django_db_setup():
    from django.conf import settings

    settings.DATABASES['default']['NAME'] = 'the_copied_db'

    run_sql('DROP DATABASE IF EXISTS the_copied_db')
    run_sql(f'CREATE DATABASE the_copied_db TEMPLATE {os.environ.get("movie_lib_db_name")}')

    yield

    for connection in connections.all():
        connection.close()

    run_sql('DROP DATABASE the_copied_db')


@pytest.fixture(scope="function")
def admin_login(client):
    client.get("/admin/login/")
    client.login(username=os.environ.get("movie_lib_admin_login"),
                 password=os.environ.get("movie_lib_admin_password"))
    yield client
    client.get("/admin/logout/")

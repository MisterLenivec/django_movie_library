import pytest

from movies.models import Movie, Actor


# After /json-filter/ film slug urls
@pytest.mark.parametrize('page_url', [
    "/",
    "/filter/",
    "/json-filter/",
    "/frozen-2/",
    "/terminator/",
    "/terminator-2/",
    "/terminator-3/",
    "/frozen/",
    "/terminator-4/",
])
@pytest.mark.django_db
class TestUrlStatusCode:
    """
    Tests for task urls status code
    """
    def test_get_base_page_status_code(self, client, page_url):
        page = client.get(page_url)
        assert page.status_code == 200, \
            f"'{page_url}' status code is not 200, but should be"


# Dont do like that
@pytest.mark.django_db
class TestUrlStatusCodeForActors:
    """
    Tests for task actor urls status code
    """
    def test_get_base_page_status_code_for_actors(self, client):
        for actor in Actor.objects.all():
            page = client.get(f"/actor/{actor.name}/")
            assert page.status_code == 200, \
                f"'/actor/{actor.name}/' status code is not 200, but should be"


@pytest.mark.parametrize('template_name', [
    "base.html",
    "movies/movie_list.html",
    "include/header.html",
    "include/footer.html",
    "include/pagination.html",
    "movies/base.html",
    "include/sidebar.html",
    "movies/tags/last_movie.html",
    "contact/tags/form.html"
])
@pytest.mark.django_db
class TestsTemplatePresence:
    """
    Tests for task template presence
    """
    def test_page_is_base_page(self, client, template_name):
        page = client.get("/")
        assert template_name in (template.name for template in page.templates), \
            f"{template_name} should be on this url, but it's not"


@pytest.mark.xfail(reason="This templates should not be on page")
@pytest.mark.parametrize('template_name', [
    "pages/about.html",
    "movies/actor.html",
    "movies/movie_detail.html"
])
@pytest.mark.django_db
def test_pages_template_not_from_this_url(client, template_name):
    page = client.get("/")
    assert template_name in (template.name for template in page.templates), \
        f"{template_name} page on the main url, but should not be"

from django.test import TestCase


class TemplatePresenceTests(TestCase):
    """
    Tests for task template presence
    """
    def setUp(self) -> None:
        self.page = self.client.get("/")

    def test_get_base_page_status_code(self):
        """
        Check index page status code
        """
        self.assertEqual(self.page.status_code, 200)

    def test_page_is_base_page(self):
        """
        Checking a base template by URL
        """
        self.assertTemplateUsed(self.page, "base.html")

    def test_page_is_list_page(self):
        """
        Checking a list page template by URL
        """
        self.assertTemplateUsed(self.page, 'movies/movie_list.html')

    def test_page_is_header_page(self):
        """
        Checking a header page template by URL
        """
        self.assertTemplateUsed(self.page, 'include/header.html')

    def test_page_is_footer_page(self):
        """
        Checking a footer page template by URL
        """
        self.assertTemplateUsed(self.page, 'include/footer.html')

    def test_page_is_pagination_page(self):
        """
        Checking a pagination page template by URL
        """
        self.assertTemplateUsed(self.page, 'include/pagination.html')

    def test_page_is_movies_base_page(self):
        """
        Checking a movies_base page template by URL
        """
        self.assertTemplateUsed(self.page, "movies/base.html")

    def test_page_is_sidebar_page(self):
        """
        Checking a sidebar page template by URL
        """
        self.assertTemplateUsed(self.page, 'include/sidebar.html')

    def test_page_is_last_movies_page(self):
        """
        Checking a last_movies page template by URL
        """
        self.assertTemplateUsed(self.page, 'movies/tags/last_movie.html')

    def test_page_is_contact_form_page(self):
        """
        Checking a contact_form page template by URL
        """
        self.assertTemplateUsed(self.page, 'contact/tags/form.html')

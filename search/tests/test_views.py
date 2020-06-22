from django.apps import apps
from django.test import TestCase
from tour_store.models import Destinations

class TestSearchView(TestCase):
    '''Test the search view'''

    def test_do_search_view_with_not_existing_query(self):
        '''test the search view'''
        page = self.client.get("/search/", {'q': 'q'}, follow=True)

        # check if status code is 200
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "destinations.html")

from django.test import TestCase
from tour_store.models import Destinations

class TestSearchView(TestCase):

    def test_do_search_view(self):
        #test the search view
        page = self.client.get("/search/", {'q': 'hello'})

        # check if status code is 200
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "destinations.html")

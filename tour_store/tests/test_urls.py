from django.test import SimpleTestCase
from django.urls import reverse, resolve
#url names
from tour_store.views import destinations, destination_details

class TestUrls(SimpleTestCase):

    def test_destination_url_is_resolves(self):
        #destination url name
        url = reverse('destination')
        print(resolve(url))
        self.assertEquals(resolve(url).func, destinations)

    def test_destination_details_url_is_resolves(self):
        #destination_details url name
        #args will define the <int:id> for the test 
        url = reverse('destinationDetails', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, destination_details)

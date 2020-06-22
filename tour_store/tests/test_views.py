from django.test import TestCase, Client
from django.urls import reverse
from tour_store.models import Destinations
from django.utils import timezone

class TestViews(TestCase):
#test_main_view_GET test is displayed on the main url in main_tour_folder
    def test_home_page(self):
        page = self.client.get('/')
        self.assertEquals(page.status_code, 200)
        self.assertTemplateUsed(page, 'main.html')

    def test_destinations_GET(self):
        client = Client()
        response = client.get(reverse('destination'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'destinations.html')

    def test_detail_GET(self):
        """
        will create a destination post and assign to
        the url as id
        """
        client = Client()
        destination = Destinations.objects.create(
            tour_title='hello',
            booking_start_date=timezone.now(),
            booking_end_date= timezone.now(),
            price=2000,
            description='whatever',
            author='whatever',
            image='image.png')
        id = destination.id

        #response = client.get("/destination-details/{0}".format(id))
        response = client.get(reverse('destinationDetails', args=[id]))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'details.html')

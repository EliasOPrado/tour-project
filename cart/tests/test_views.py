from django.test import TestCase, Client
from django.urls import reverse
from tour_store.models import Destinations
from django.utils import timezone
from django.contrib.auth.models import User

class TestView(TestCase):

    def test_view_cart_redirection(self):
        page = self.client.get("/cart/view-cart")

        self.assertEqual(page.status_code, 302)
    

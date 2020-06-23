from django.test import TestCase
from django.urls import reverse, resolve
#url names
from checkout.views import checkout

class TestUrls(TestCase):

    def test_checkout_url_is_resolved(self):
        #destination url name
        url = reverse('checkout')
        print(resolve(url))
        self.assertEquals(resolve(url).func, checkout)

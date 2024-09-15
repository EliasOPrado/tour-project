from django.test import TestCase
from django.urls import reverse, resolve

# url names
from cart.views import view_cart, add_to_cart, adjust_cart


class TestUrls(TestCase):

    def test_view_cart_url_is_resolved(self):
        # destination url name
        url = reverse("view_cart")
        self.assertEquals(resolve(url).func, view_cart)

    def test_add_to_cart_url_is_resolved(self):
        # destination url name
        # args will define the <int:id> for the test
        url = reverse("add_to_cart", args=[1])
        self.assertEquals(resolve(url).func, add_to_cart)

    def test_adjust_cart_url_is_resolved(self):
        # destination url name
        # args will define the <int:id> for the test
        url = reverse("adjust_cart", args=[1])
        self.assertEquals(resolve(url).func, adjust_cart)

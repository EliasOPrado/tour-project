from django.test import TestCase
from django.urls import reverse, resolve

# url names
from accounts.views import register, logout, login


class TestUrls(TestCase):

    def test_register_url_is_resolved(self):
        # destination url name
        url = reverse("register")
        self.assertEquals(resolve(url).func, register)

    def test_logout_url_is_resolved(self):
        # destination url name
        url = reverse("logout")
        self.assertEquals(resolve(url).func, logout)

    def test_login_url_is_resolved(self):
        # destination url name
        url = reverse("login")
        self.assertEquals(resolve(url).func, login)

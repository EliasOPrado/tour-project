from django.test import TestCase, Client
from django.urls import reverse
from tour_store.models import Destinations
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import get_messages

class TestView(TestCase):

     def test_get_register_customer_page(self):
         #test if the register view is working
        page = self.client.get("/accounts/register/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "register.html")

     def test_registering_a_new_user(self):
        # test if the register form is working for user
        page = self.client.get('/accounts/register/',
                                data={'username': 'test',
                                'email': 'test@email.com',
                                 'password1': '@testpassword123',
                                 'password2': '@testpassword123'},
                                )
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "register.html")

     def test_get_login_customer_page(self):
        # test login url directs to login.html
        # url to login
        page = self.client.get("/accounts/login/")
        # check for a status code 200
        self.assertEqual(page.status_code, 200)
        # check Template Used is login.html
        self.assertTemplateUsed(page, "login.html")

     def test_login_view_when_someone_logged_in(self):
        ''' test trying to login when someone is already logged in '''

        # create a user
        user = User.objects.create_user('username',
                                        'test@test.com',
                                        'password')
        # login the user
        self.client.login(username='username',
                          password='password')
        # url to login
        page = self.client.get("/accounts/login/")
        # check for a status code 200
        self.assertEqual(page.status_code, 200)
        # check Template Used is profile.html
        self.assertTemplateUsed(page, reverse('index'))

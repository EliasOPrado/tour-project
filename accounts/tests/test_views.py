from django.test import TestCase, Client
from django.shortcuts import redirect
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
        

     def test_get_login_page(self):
        # test login url directs to login.html
        # url to login
        page = self.client.get("/accounts/login/")
        # check for a status code 200
        self.assertEqual(page.status_code, 200)
        # check Template Used is login.html
        self.assertTemplateUsed(page, "login.html")

     def test_login_view_when_a_user_is_log_in(self):

        # create a user
        user = User.objects.create_user('username',
                                        'test@test.com',
                                        'password')
        # login
        self.client.login(username='username',
                          password='password')
        # url to the login page
        page = self.client.get("/accounts/login/")
        # check for a status code 200
        self.assertEqual(page.status_code, 200)
        # check Template Used is profile.html
        self.assertTemplateUsed(page, 'login.html')

     def test_logout_view_after_user_already_logged_in(self):
        #test logout view

        # create a user
        user = User.objects.create_user('username',
                                        'test@email.com',
                                        '@Password123')
        # login
        self.client.login(username='username',
                          password='@Password123')
        # url to the logout page
        page = self.client.get("/accounts/logout/", follow=True)
        # check for a status code 302
        self.assertEqual(page.status_code, 200)
        # check Template Used is main.html page
        self.assertTemplateUsed(page, 'main.html')
        # check the message stored is equal to the expected message
        messages = list(get_messages(page.wsgi_request))
        self.assertEqual(str(messages[0]),
                         'You have successfully logged out')

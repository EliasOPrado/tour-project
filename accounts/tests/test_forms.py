from django.test import TestCase
from accounts.forms import ( UserLoginForm, UserRegistrationForm )
from django import forms



class TestForms(TestCase):

    def test_user_login_form(self):
        #test if the form is valid
        form = UserLoginForm(data={
            'username_or_email':'test@email.com',
            'password': '123',
        })
        self.assertTrue(form.is_valid())

    def test__invalid_user_login_form(self):
        #test if the form is valid
        form = UserLoginForm(data={
            'username_or_email':'test@email.com',
            'password': '',
        })
        self.assertFalse(form.is_valid())

    def test_user_registration_form(self):
        #test if the form is valid
        form = UserRegistrationForm(data={
            'username':'test',
            'email': 'test@email.com',
            'password1': '@Password123',
            'password2': '@Password123',
        })
        self.assertTrue(form.is_valid())

    def test_unvalid_user_registration_form(self):
        #test if the form is valid
        form = UserRegistrationForm(data={
            'username':'test',
            'email': 'test@email.com',
            'password1': 'testing',
            'password2': 'testing',
        })
        self.assertFalse(form.is_valid())

    def test_missing_email_user_registration_form(self):
        #test if the form is valid
        form = UserRegistrationForm(data={
            'username':'test',
            'email': '',
            'password1': 'testing',
            'password2': 'testing',
        })
        self.assertFalse(form.is_valid())

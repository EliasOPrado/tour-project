from django.test import TestCase
from checkout.forms import MakePaymentForm, OrderForm
from django import forms


class TestForms(TestCase):

    def test_payment_form(self):
        # test if the form is valid
        form = MakePaymentForm(
            data={
                "credit_card_number": "4242424242424242",
                "cvv": "123",
                "expiry_month": 3,
                "expiry_year": 2022,
                "stripe_id": "tok_visa",
            }
        )
        self.assertTrue(form.is_valid())

    def test_payment_form_not_valid(self):
        # test if the form is not valid
        form = MakePaymentForm(
            data={
                # expirY_month and 'expiry_year' already have its values.
                "credit_card_number": "",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_order_form_form(self):
        # test if the form is valid
        form = OrderForm(
            data={
                "full_name": "john test testing",
                "phone_number": "12345678",
                "country": "Brazil",
                "postcode": "98u887y776",
                "town_or_city": "Guarulhos",
                "street_address1": "Av Jetulio Vargas",
                "street_address2": "Mooca",
                "county": "Praca da republica",
            }
        )
        self.assertTrue(form.is_valid())

    def test_order_form_form(self):
        # test if the form is not valid
        form = OrderForm(
            data={
                "full_name": "",
                "phone_number": "",
                "country": "",
                # postcode is not required
                #'postcode': '98u887y776',
                "town_or_city": "",
                "street_address1": "",
                # street_adress2 is not required
                #'street_address2':'Mooca',
                "county": "",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 6)

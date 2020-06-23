# from django.test import TestCase, Client
# from django.urls import reverse
# from tour_store.models import Destinations
# from checkout.views import checkout
# from django.contrib.auth.models import User
# from django.utils import timezone
# from django.contrib.messages import get_messages
#
# class TestViews(TestCase):
# #test_main_view_GET test is displayed on the main url in main_tour_folder
#     def test_order_checkout_page(self):
#
#         #  create a user
#         user = User.objects.create_user(username='username',email='any@email.com',password='password')
#         # login the user
#         self.client.login(username='username', password='password')
#
#         item = Destinations.objects.create(tour_title='tour',
#                                            booking_start_date = timezone.now(),
#                                            booking_end_date = timezone.now(),
#                                            price='2000'
#                                            )
#         self.client.post("/cart/add/{0}/".format(item.id),
#                          data={'quantity': '2'})
#
#         # get the stripe publisable key
#         stripe_id = 'tok_visa'
#         page = self.client.post("/checkout/",
#                                 {'full_name': 'name',
#                                  'phone_number': '000',
#                                  'street_address1': 'address 1',
#                                  'street_address2': 'address 2',
#                                  'town_or_city': 'city',
#                                  'county': 'county',
#                                  'country': 'country',
#                                  'postcode': 'code13',
#                                  'credit_card_number': '4242424242424242',
#                                  'cvv': '123',
#                                  'expiry_month': '2',
#                                  'expiry_year': '2022',
#                                  'stripe_id': stripe_id},
#                                 )
#         # Messages in checkout function needs to be changed from error to success() or warning()
#         messages = list(page.context['messages'])
#         self.assertEqual(len(messages), 1)
#         self.assertEqual(str(messages[0]),'You have successfully paid.')
#         # check the page status is ok

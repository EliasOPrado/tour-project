from django.test import TestCase
from checkout.models import Order, OrderLineItem
from tour_store.models import Destinations
from django.utils import timezone
import datetime
from unittest.mock import patch


class TestModels(TestCase):

    def test_order_model(self):
        # test if Destinations model is passing correctly its values
        with patch.object(
            timezone, "now", return_value=datetime.datetime(2020, 1, 8, 11, 00)
        ) as mock_now:
            order = Order.objects.create(
                full_name="John test testing",
                phone_number="0987654321",
                country="Ireland",
                postcode="0o9i8u7y6t5r",
                town_or_city="Dublin",
                street_address1="4 Leinster avenue",
                street_address2="Park Groove",
                county="Dublin 99",
                date=timezone.now(),
            )
            order.save()
            self.assertEquals(order.full_name, "John test testing")
            self.assertEquals(order.phone_number, "0987654321")
            self.assertEquals(order.country, "Ireland")
            self.assertEquals(order.postcode, "0o9i8u7y6t5r")
            self.assertEquals(order.town_or_city, "Dublin")
            self.assertEquals(order.street_address1, "4 Leinster avenue")
            self.assertEquals(order.county, "Dublin 99")
            self.assertEquals(order.date, timezone.now())

    def test_order_line_item_model(self):
        with patch.object(
            timezone, "now", return_value=datetime.datetime(2020, 1, 8, 11, 00)
        ) as mock_now:
            order = Order.objects.create(
                full_name="John test testing",
                phone_number="0987654321",
                country="Ireland",
                postcode="0o9i8u7y6t5r",
                town_or_city="Dublin",
                street_address1="4 Leinster avenue",
                street_address2="Park Groove",
                county="Dublin 99",
                date=timezone.now(),
            )
            order.save()
            destination = Destinations.objects.create(
                tour_title="test1",
                booking_start_date="2021-05-30",
                booking_end_date="2022-05-30",
                price=2000,
                description="test1",
                author="test1",
                image="image.png",
            )
            destination.save()
            order_line_item = OrderLineItem.objects.create(
                order=order, destination=destination, quantity=1
            )
            # test if OrderLineItem.order field is related to order model
            self.assertEquals(order_line_item.order, order)
            # test if OrderLineItem.destination field is related to order model
            self.assertEquals(order_line_item.destination, destination)
            self.assertEquals(order_line_item.quantity, 1)

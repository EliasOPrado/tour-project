from django.test import TestCase
from tour_store.models import Destinations, Comment, Contact
from django.utils import timezone
import datetime
from mock import patch

class TestModels(TestCase):

    def test_destinations_model(self):
        #test if Destinations model is passing correctly its values
        destination = Destinations.objects.create(
            tour_title = 'test1',
            booking_start_date='2021-05-30',
            booking_end_date= '2022-05-30',
            price=2000,
            description='test1',
            author='test1',
            image='image.png'
        )
        destination.save()
        self.assertEquals(destination.tour_title, 'test1')
        self.assertEquals(destination.booking_start_date, '2021-05-30')
        self.assertEquals(destination.booking_end_date, '2022-05-30')
        self.assertEquals(destination.price, 2000)
        self.assertEquals(destination.description, 'test1')
        self.assertEquals(destination.author, 'test1')
        self.assertEquals(destination.image, 'image.png')

    def test_comment_model(self):
        #test if Comment model is related to Destinations model
        destination = Destinations.objects.create(
            tour_title = 'test1',
            booking_start_date ='2021-05-30',
            booking_end_date= '2022-05-30',
            price = 2000,
            description = 'test1',
            author = 'test1',
            image = 'image.png'
        )
        destination.save()
        comment = Comment.objects.create(
            #the relation between both models
            post = destination,
            name = 'John',
            email = 'any@email.com',
            comment = 'test1',
            created_on = timezone.now(),
            active = False,
        )
        comment.save()
        self.assertEquals(destination, comment.post)

    def test_cotact_model(self):
        # Add mock and patch to match both datetime.
        #for the model and the assertEquals
        with patch.object(timezone, 'now', return_value=datetime.datetime(2015, 1, 8, 11, 00)) as mock_now:
            contact = Contact.objects.create(
                name = 'neil',
                email='neil@email.com',
                subject= 'this is a test.',
                message = 'test',
                created_on = timezone.now(),
                active = False,
            )
            contact.save()
            self.assertEquals(contact.name, 'neil')
            self.assertEquals(contact.email, 'neil@email.com')
            self.assertEquals(contact.subject, 'this is a test.')
            self.assertEquals(contact.message, 'test')
            self.assertEquals(contact.created_on, timezone.now())
            self.assertEquals(contact.active, False)

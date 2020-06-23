from django.test import TestCase
from tour_store.forms import CommentForm, ContactForm

class TestForms(TestCase):

    def test_comment_form(self):
        #test if the form is valid
        form = CommentForm(data={
            'name': 'John',
            'email': 'john@email.com',
            'comment': 'this is a comment.'
        })
        self.assertTrue(form.is_valid())

    def test_comment_form_no_data(self):
        #test if the form can validate Empty
        #test if the form sends an error messaage for each field
        form = CommentForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),3)

    def test_contact_form(self):
        #test if the form is valid
        form = ContactForm(data={
            'name': 'John',
            'email': 'john@email.com',
            'subject': 'this is a title.',
            'message': 'this is a message'
        })
        self.assertTrue(form.is_valid())

    def test_contact_form_no_data(self):
        #test if the form can validate Empty
        #test if the form sends an error messaage for each field
        form = ContactForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),4)

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class Destinations(models.Model):

    author = models.CharField(max_length=200, unique=False)
    tour_title = models.CharField(max_length=250)
    description = RichTextUploadingField()
    image = models.ImageField(upload_to='tour_images', blank=True)
    location = models.CharField(max_length=250)
    booking_start_date = models.DateField()
    booking_end_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.tour_title

class Comment(models.Model):
    post = models.ForeignKey(Destinations,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.comment, self.name)

class Contact(models.Model):
    name = models.CharField(max_length=80, blank=False)
    email = models.EmailField(blank=False)
    subject = models.CharField(max_length=40, blank=False)
    message = models.TextField(blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Contact {} by {}'.format(self.contact, self.name)

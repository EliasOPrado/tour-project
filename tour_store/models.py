from django.db import models

# Create your models here.


class tour_destinations(models.Model):
    """This is a model to create destinations by the owner. """
    author = models.CharField(max_length=200, unique=True)
    tour_title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='tour_images', blank=True)
    location = models.CharField(max_length=250)
    booking_start_date = models.DateField()
    booking_end_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.tour_title

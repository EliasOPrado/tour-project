from django.db import models

# Create your models here.


class tour_destinations(models.Model):
    """This is a model to create destinations by the owner. """
    author = models.CharField(max_length=200 unique=True)
    tour_title = models.CharField(max_length=250)
    description = models.CharField(blank=True)
    image = models.ImageField(upload_to='product', blank=True)
    location = models.CharField(max_length=250)
    booking_start_date = models.DateField(u"Begin of the retreat", help_text="Begin of the retreat")
    booking_end_date = models.DateField(u"End of the retreat", help_text="End of the retreat")
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.tour_title

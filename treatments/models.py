from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Treatment(models.Model):
    '''
    models for clinic treatments
    '''
    featured_image = CloudinaryField('image')
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

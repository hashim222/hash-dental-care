'''
Treatments models
'''
from django.db import models
from cloudinary.models import CloudinaryField


class Treatment(models.Model):
    '''
    Models for clinic treatments template.
    Where i can add title, images and descritpion by using admin panel.
    '''
    featured_image = CloudinaryField('image')
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return str(self.title)

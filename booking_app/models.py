from django.db import models
from django.contrib.auth.models import User
from treatments.models import Treatment


# Create your models here.
STATUS = ((0, 'Pending'), (1, 'Approved'))


class BookAppointmentModel(models.Model):
    '''
    book appoinment models
    '''
    user_title = [
        ('mr', 'Mr'),
        ('mrs', 'Mrs'),
        ('miss', 'Miss')
    ]
    title = models.CharField(max_length=5, choices=user_title)
    patient = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='choose_treatment')
    name = models.CharField(max_length=40, )
    phone = models.CharField(max_length=11)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    your_request = models.TextField()
    treatments = models.ForeignKey(
        Treatment, on_delete=models.CASCADE, related_name='treatments_title')
    status = models.IntegerField(choices=STATUS, default=0)
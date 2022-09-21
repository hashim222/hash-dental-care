from django.db import models
from django.contrib.auth.models import User
from treatments.models import Treatment


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
        User, on_delete=models.CASCADE, related_name='user_booking', null=True, blank=True)
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=254)
    created_date = models.DateField()
    update_date = models.DateTimeField(auto_now=True)
    treatments = models.ForeignKey(
        Treatment, on_delete=models.CASCADE, related_name='treatments_title')
    your_request = models.TextField(max_length=500, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    admin_decision = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_date']
        verbose_name = ("Book Appointment Model")

    def __str__(self):
        return self.name

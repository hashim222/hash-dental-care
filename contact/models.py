from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class ContactModel(models.Model):
    '''
    Contact forms models
    '''
    name = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    phone = PhoneNumberField(region="GB")

    class Meta:
        verbose_name = ("Contact Model")

    def __str__(self):
        return self.name

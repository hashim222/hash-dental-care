from typing_extensions import Required
from django.db import models


class ContactModel(models.Model):
    name = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.fullname

from django.db import models


class Contacts(models.Model):
    full_name = models.CharField(max_length=30)
    relationship = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name

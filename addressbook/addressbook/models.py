from django.db import models
from django.db.models import DO_NOTHING


class PhoneNumber(models.Model):
    """Phone numbers object model."""
    country_code = models.CharField(max_length=5, null=True, blank=True)
    number = models.CharField(max_length=50)

    def __str__(self):
        return self.number


class Address(models.Model):
    """Address object model"""
    line_1 = models.CharField(max_length=255, null=True, blank=True)
    line_2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=50)
    post_code = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.post_code


class Contacts(models.Model):
    """Contacts model object."""
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100)
    phone_number = models.ForeignKey(
        PhoneNumber,
        related_name="+",
        on_delete=DO_NOTHING,
    )
    address = models.ForeignKey(
        Address,
        related_name="+",
        on_delete=DO_NOTHING,
    )

    def __str__(self):
        return "{first_name} {last_name}".format(
            first_name=self.first_name,
            last_name=self.last_name
        )

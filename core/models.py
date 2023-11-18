from django.db import models
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver

class Leadz_Reup(models.Model):
    facebook_username = models.CharField(max_length=10000, null=True, blank=True)
    instagram_username = models.CharField(max_length=10000, null=True, blank=True)
    pinterest_username = models.CharField(max_length=10000, null=True, blank=True)
    linkedin_username = models.CharField(max_length=10000, null=True, blank=True)
    x_username = models.CharField(max_length=10000, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    email = models.CharField(max_length=10000, null=True, blank=True)
    phone_number = models.CharField(max_length=10000, null=True, blank=True)


class Contact_Form_Submission(models.Model):
    name = models.CharField(max_length=10000)
    phone_number = models.CharField(max_length=10000)
    email = models.CharField(max_length=10000)
    services = models.CharField(max_length=10000)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - Contact Details"
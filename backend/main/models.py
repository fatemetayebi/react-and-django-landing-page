from django.db import models

from django.db import models


class Product(models.Model):
    id = models.IntegerField(null=False, blank=False, unique=True, primary_key=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    video = models.FileField(upload_to='videos_uploaded', null=True, blank=True)
    title = models.CharField(max_length=100, null=False, blank=False)
    intro = models.TextField(max_length=151, null=True, blank=True)
    link = models.TextField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True, null=False, blank=False)

    def __str__(self):
        return self.title


class Contact(models.Model):
    email = models.EmailField(null=True, blank=True)
    subject = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    phone = models.TextField(null=True, blank=True)
    name = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.email


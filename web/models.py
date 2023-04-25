from django.db import models
from versatileimagefield.fields import VersatileImageField
from tinymce.models import HTMLField
# Create your models here.

class Service(models.Model):
    # left
    title = models.CharField(max_length=100, blank=True, null=True)
    image = VersatileImageField(upload_to="service",blank=True, null=True)
    sub_head = models.CharField(max_length=50,blank=True, null=True)
    detail = models.TextField(blank=True, null=True)

    # right
    title2 = models.CharField(max_length=100, blank=True, null=True)
    image2 = VersatileImageField(upload_to="service",blank=True, null=True)
    sub_head2 = models.CharField(max_length=50,blank=True, null=True)
    detail2 = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title or self.title2
    

class Package(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    image = VersatileImageField(upload_to="service",blank=True, null=True)
    detail = models.TextField(blank=True, null=True)

class Gallery(models.Model):
    image=VersatileImageField()

    

class Package(models.Model):
    # left
    title = models.CharField(max_length=100, blank=True, null=True)
    image = VersatileImageField(upload_to="service",blank=True, null=True)
    sub_head = models.CharField(max_length=50,blank=True, null=True)
    detail = models.TextField(blank=True, null=True)

    # right
    title2 = models.CharField(max_length=100, blank=True, null=True)
    image2 = VersatileImageField(upload_to="service",blank=True, null=True)
    sub_head2 = models.CharField(max_length=50,blank=True, null=True)
    detail2 = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title or self.title2

from ctypes import addressof
import email
from unicodedata import name
from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    phoneNumber = models.IntegerField(max_length=11)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
# Create your models here.

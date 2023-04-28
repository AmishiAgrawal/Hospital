from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    USER_CHOICES = [
        ('Doctor', 'Doctor'),
        ('Patient', 'Patient'),
    ]

    
    email = models.EmailField(max_length=50,null=True)
    profile_img = models.ImageField(upload_to='Myprofile/images')
    address = models.CharField(max_length=200)
    city  = models.CharField(max_length=15,blank=True,null=True)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=1500)
    role = models.CharField(max_length=10,choices=USER_CHOICES,default='Patient')


    def __str__(self):
        return self.username
from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

  
    ph_no = models.BigIntegerField(null=True, blank=True)
    location = models.TextField(null=True, blank=True)
    image = models.ImageField(
        upload_to='user_images/',
        null=True,
        blank=True,
        default='user_images/default.png'
    )

             


from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
        email = models.EmailField(unique=True)
        bio = models.TextField(blank=True, null=True)
        
        def __str__(self):  
            return self.username


# Create your models here.

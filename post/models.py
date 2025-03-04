from django.db import models
from user_registration.models import CustomUser

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)

    contenue = models.TextField(max_length=300)
    auteur = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name='posts')


# Create your models here.

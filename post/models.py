from django.db import models
from user_registration.models import CustomUser


#Creation du modèle post qui a une foreginkey qui la relie a un utilisateur
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)

    content = models.TextField(max_length=300)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name='posts')


# Create your models here.

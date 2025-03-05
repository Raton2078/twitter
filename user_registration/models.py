from django.db import models
from django.contrib.auth.models import AbstractUser

#Creation d'un modele utilisateur abstrait permettant de modifier le modèle User de base présent sur Django
class CustomUser(AbstractUser):
        email = models.EmailField(unique=True)
        bio = models.TextField(blank=True, null=True)
        
        def __str__(self):  
            return self.username


# Create your models here.

#Modèle fais uniquement de foreign key permettant de gérer toute la partie abonnement entre les différents utilisateurs
class Subscription(models.Model):
      subscriber = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='subscriptions')

      subscribed_to = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='subscribers')
      class Meta:
            unique_together  = ('subscriber','subscribed_to')
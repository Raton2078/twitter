from django.db import models
from django.contrib.auth.models import AbstractUser

#Creation d'un modele utilisateur abstrait permettant de modifier le modèle User de base présent sur Django
class CustomUser(AbstractUser):
        email = models.EmailField(unique=True)
        bio = models.TextField(blank=True, null=True)
        follows = models.ManyToManyField("self",
        related_name="Followed_by",
        symmetrical=False,
        blank=True)

        def __str__(self):  
            return self.username


        def followers_list(self):
            return CustomUser.objects.filter(id__in=Subscription.objects.filter(subscribed_to=self).values_list('subscriber', flat=True))

        def following_list(self):
             return CustomUser.objects.filter(id__in=Subscription.objects.filter(subscriber=self).values_list('subscribed_to', flat=True))

        def is_following(self,user):
           return Subscription.objects.filter(subscriber=self,subscribed_to=user).exists()

        def follow(self,user):
             if self != user and not self.is_following(user):  # Simplification du test booléen
                Subscription.objects.create(subscriber=self, subscribed_to=user)
        def unfollow(self,user):
            Subscription.objects.filter(subscriber=self,subscribed_to=user).delete()

        def subcribe_number(self):
             followers = self.followers_list()
             
             return len(followers)
        
        def subscribed_to_number(self):
             following = self.following_list()
             return len(following)
             
             

# Create your models here.

#Modèle fais uniquement de foreign key permettant de gérer toute la partie abonnement entre les différents utilisateurs
class Subscription(models.Model):
      subscriber = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='subscriptions')

      subscribed_to = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='subscribers')
      class Meta:
            unique_together  = ('subscriber','subscribed_to')
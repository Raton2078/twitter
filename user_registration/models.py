from django.db import models
from django.contrib.auth.models import AbstractUser

# Création d'un modèle utilisateur personnalisé basé sur AbstractUser.
# Permet d'ajouter des champs supplémentaires tout en conservant les fonctionnalités de base de Django.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  # Champ email unique pour chaque utilisateur
    bio = models.TextField(blank=True, null=True)  # Biographie optionnelle

    # Relation ManyToMany pour gérer les abonnements entre utilisateurs.
    # "symmetrical=False" permet de créer une relation unidirectionnelle (A suit B mais B ne suit pas forcément A).
    follows = models.ManyToManyField("self", related_name="Followed_by", symmetrical=False, blank=True)

    def __str__(self):
        return self.username  # Retourne le nom d'utilisateur lors de l'affichage d'un objet CustomUser


    # Récupère la liste des utilisateurs qui suivent l'utilisateur actuel.
    def followers_list(self):
        return CustomUser.objects.filter(
            id__in=Subscription.objects.filter(subscribed_to=self).values_list('subscriber', flat=True)
        )


    # Récupère la liste des utilisateurs que l'utilisateur actuel suit.
    def following_list(self):
        return CustomUser.objects.filter(
            id__in=Subscription.objects.filter(subscriber=self).values_list('subscribed_to', flat=True)
        )


    # Vérifie si l'utilisateur suit un autre utilisateur.
    # Retourne True si une relation d'abonnement existe, False sinon.
    def is_following(self, user):
        return Subscription.objects.filter(subscriber=self, subscribed_to=user).exists()


    # Ajoute une relation d'abonnement si elle n'existe pas déjà.
    def follow(self, user):
        if self != user and not self.is_following(user):  # Vérifie que l'utilisateur ne s'abonne pas à lui-même
            Subscription.objects.create(subscriber=self, subscribed_to=user)


    # Supprime une relation d'abonnement existante.
    def unfollow(self, user):
        Subscription.objects.filter(subscriber=self, subscribed_to=user).delete()


    # Retourne le nombre d'abonnés (followers) de l'utilisateur actuel.
    def subcribe_number(self):
        followers = self.followers_list()
        return len(followers)


    # Retourne le nombre d'utilisateurs suivis par l'utilisateur actuel.
    def subscribed_to_number(self):
        following = self.following_list()
        return len(following)


# Modèle permettant de gérer les abonnements entre les utilisateurs.
# Utilise des clés étrangères vers CustomUser pour définir une relation unidirectionnelle (subscriber -> subscribed_to).
class Subscription(models.Model):
    subscriber = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='subscriptions')  # L'utilisateur qui suit
    subscribed_to = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='subscribers')  # L'utilisateur suivi

    class Meta:
        unique_together = ('subscriber', 'subscribed_to')  # Empêche un utilisateur de suivre plusieurs fois la même personne

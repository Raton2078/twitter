from django.shortcuts import render, redirect
from .models import Post
from . import forms
from django.contrib.auth.decorators import login_required


# Fonction permettant de créer un post associé à un utilisateur.
# - Vérifie si la requête est en POST.
# - Valide le formulaire avant d'enregistrer le post.
# - Associe automatiquement l'auteur au post avant de l'enregistrer.
# - Redirige l'utilisateur vers la page d'accueil après la création du post.
def create_post(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST)
        if form.is_valid():
            newpost = form.save(commit=False)  # On ne sauvegarde pas encore en base
            newpost.author = request.user  # Associe le post à l'utilisateur connecté
            newpost.save()  # Sauvegarde en base
            return redirect('/')  # Redirection après création du post
    
    else:
        form = forms.CreatePost()  # Instancie un formulaire vide

    return render(request, "post/create_post.html", {"form": form})  # Affiche le formulaire



# Fonction permettant d'afficher tous les posts de tous les utilisateurs.
# - Récupère tous les objets Post depuis la base de données.
# - Passe ces posts au template `all_posts.html` pour affichage.
def see_all_post(request):
    posts = Post.objects.all()  # Récupère tous les posts
    return render(request, 'post/all_posts.html', {'posts': posts})  # Envoie les posts au template



# Fonction permettant d'afficher uniquement les posts de l'utilisateur connecté.
# - Utilise le décorateur `@login_required` pour empêcher l'accès aux utilisateurs non connectés.
# - Récupère les posts filtrés par l'auteur (`request.user`).
# - Passe ces posts au template `self_posts.html` pour affichage.
@login_required
def see_self_post(request):
    posts = Post.objects.filter(author=request.user)  # Filtre les posts de l'utilisateur connecté
    print(posts)  # Debug : affiche les posts dans la console du serveur (à retirer en production)
    return render(request, 'post/self_posts.html', {'posts': posts})  # Envoie les posts au template


# Create your views here.

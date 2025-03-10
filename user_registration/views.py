
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm
from .models import CustomUser, Subscription
from django.contrib.auth.forms import AuthenticationForm
from django.template.loader import get_template
from django.contrib.auth import login, logout 
from django.contrib.auth.decorators import login_required



# Fonction permettant à un nouvel utilisateur de créer un compte sur le site web
# Si la requête est en POST, on traite le formulaire d'inscription.
# Si le formulaire est valide, on crée l'utilisateur et on le connecte automatiquement.
# Ensuite, on le redirige vers la page "/posts/self_posts".
# Sinon, on affiche simplement le formulaire vide.
def register_view(request):
    if  request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
           user = form.save()
           login(request,user)
           return redirect('/posts/self_posts')
        
    else:
        form = SignUpForm()
    return render(request, 'user_registration/register.html', {'form': form})



# Fonction permettant à un utilisateur de se connecter au site web s'il est bien enregistré.
# Si la requête est en POST, on vérifie les informations d'identification via AuthenticationForm.
# Si elles sont valides, on connecte l'utilisateur et on le redirige vers la page d'accueil "/".
# Sinon, on affiche simplement le formulaire de connexion.
def login_view(request):
    if request.method ==  'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            login(request,form.get_user())
            return redirect('/')
        
    else:
        form = AuthenticationForm()
    return render(request, 'user_registration/login.html', {'form': form})



# Fonction permettant de déconnecter un utilisateur lorsqu'il appuie sur le bouton de déconnexion.
# Cette fonction n'accepte que les requêtes POST pour éviter les déconnexions accidentelles.
# Après la déconnexion, l'utilisateur est redirigé vers la page d'accueil "/".
def logout_view(request):
     if request.method == 'POST':
          logout(request)
          return redirect('/')
     
     
     
# Fonction permettant de voir le profil d'un utilisateur passé en paramètre (via son username).
# L'accès à cette page est restreint aux utilisateurs connectés grâce au décorateur @login_required.
# Si l'utilisateur n'est pas connecté, il est redirigé vers "/need_login/".
# On récupère les informations de l'utilisateur, son nombre d'abonnés et d'abonnements.
def see_profil(request,username):
    user = get_object_or_404(CustomUser,username=username)
    exist= request.user.is_following(user)
    followers_number = user.subcribe_number()
    following_number = user.subscribed_to_number()
    return render(request, 'user_registration/profil.html',
                   {'user': user,
                    'exist': exist,
                    'followers_number': followers_number,
                    'following_number': following_number,})
                                                              
                                                            


# Fonction permettant à un utilisateur de s'abonner à un autre utilisateur.
# On récupère les objets CustomUser correspondant au subscriber et au subscribed_to.
# Si user1 (l'utilisateur connecté) ne suit pas encore user2, il effectue l'abonnement.
# Après l'action, l'utilisateur est redirigé vers la page précédente.
def subscription_to(request, subscriber,subscribed_to):
    user1 = CustomUser.objects.get(username=subscriber)
    user2 = CustomUser.objects.get(username=subscribed_to)

    if user1.is_following(user2) == False:
         user1.follow(user2)

    return redirect(request.META.get('HTTP_REFERER', request.path))



# Fonction permettant à un utilisateur de se désabonner d'un autre utilisateur.
# On récupère les objets CustomUser correspondant au subscriber et au subscribed_to.
# L'utilisateur se désabonne en appelant la méthode unfollow().
# Après l'action, il est redirigé vers la page précédente.
def unfollow(request, subscriber,subscribed_to ):
    user1 = CustomUser.objects.get(username=subscriber)
    user2 = CustomUser.objects.get(username=subscribed_to)
    user1.unfollow(user2)
    return redirect(request.META.get('HTTP_REFERER', request.path))

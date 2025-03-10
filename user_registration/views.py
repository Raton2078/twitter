from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm
from .models import CustomUser, Subscription
from django.contrib.auth.forms import AuthenticationForm
from django.template.loader import get_template
from django.contrib.auth import login, logout


#Fonction permettant a un nouvel utilisateur de créer un compte sur le site web 
def register_view(request):
    if  request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
           user = form.save()
           login(request,user)
           return redirect('/posts/self_posts')
        else:
            print("non valide")
    else:
        form = SignUpForm()
    return render(request, 'user_registration/register.html', {"form": form})

#Fonction permettant la connexion sur le site web si l'utilisateur est bien enregistré
def login_view(request):
    if request.method ==  'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request,form.get_user())
            return redirect('/')

    else:
        form = AuthenticationForm()
    return render(request, 'user_registration/login.html', {"form": form})


#Fonction permettant de déconnecter l'utilisateur si il appui sur le boutton formulaire
def logout_view(request):
     if request.method == 'POST':
          logout(request)
          return redirect("/")
     
#Foncction permettant de voir le profile de l'utilisateur passé en paramètre 
def see_profil(request,username):
    user = get_object_or_404(CustomUser,username=username)
    exist= request.user.is_following(user)
    followers_number = user.subcribe_number()
    following_number = user.subscribed_to_number()
    return render(request, 'user_registration/profil.html', {'user': user,
                                                             'exist': exist,
                                                              'followers_number': followers_number,
                                                              'following_number': following_number,
                                                              }
                                                               )

#Fonction permettant l'abonnement entre utilisateur
def subscription_to(request, subscriber,subscribed_to):
    user1 = CustomUser.objects.get(username=subscriber)
    user2 = CustomUser.objects.get(username=subscribed_to)

    if user1.is_following(user2) == False:
        #subscription = Subscription.objects.create(subscriber=user1, subscribed_to=user2)
         user1.follow(user2)
    test = user2.followers_list()
    return redirect('/')

def unfollow(request, subscriber,subscribed_to ):
    user1 = CustomUser.objects.get(username=subscriber)
    user2 = CustomUser.objects.get(username=subscribed_to)
    user1.unfollow(user2)
    return redirect('/')


"""
def subscriber_page(request):

    user = CustomUser.objects.get(username="Toto")

    ish =  user.subscriptions.all()
    s = user.subscribers.all()

    return render(request, 'user_registration/abonnement.html', 
                  {'user': user,                                       
                  'poire': ish,
                  's':s}
                  )    """
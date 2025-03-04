from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm
from django.template.loader import get_template
from django.contrib.auth import login, logout

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


def login_view(request):
    if request.method ==  'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request,form.get_user())
            return redirect('/')

    else:
        form = AuthenticationForm()

    return render(request, 'user_registration/login.html', {"form": form})

def logout_view(request):
     if request.method == 'POST':
          logout(request)
          return redirect("/")
     

def see_profil(request,username):
    user = get_object_or_404(CustomUser,username=username)
    return render(request, 'user_registration/profil.html', {'user': user} )

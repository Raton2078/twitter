from django.shortcuts import render, redirect
from .models import Post
from . import forms
from django.contrib.auth.decorators import login_required


#Fonction d'initialisation d'un post associé a un utilisateur qui vérifie si le post est valide
def create_post(request):
    if request.method == 'POST':
      form = forms.CreatePost(request.POST)
      if form.is_valid():
         newpost = form.save(commit=False)
         newpost.author = request.user
         newpost.save()
         return redirect('/')
    else:
       form = forms.CreatePost()
       return render(request, "post/create_post.html", {"form": form})  

#Fonction permettant de voir tous les posts de tous les utilisateur que all_posts.html
def see_all_post(request):
   posts = Post.objects.all()
   return render(request, 'post/all_posts.html', {'posts': posts})




   


#Fonction permettant de voir exclusivement ses propres posts et qui vérifie si on est bien connecté
@login_required 
def see_self_post(request):

    posts = Post.objects.filter(author=request.user)
    print(posts)
    return render(request, 'post/self_posts.html',{'posts': posts})

# Create your views here.
